import io
import time
import base64
import json
from pathlib import Path
from typing import Optional, Dict, List

import cv2
import numpy as np
import pandas as pd
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models, transforms

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Config paths dynamically relative to main.py
BASE_DIR = Path(__file__).parent.resolve()
WEIGHTS_DIR = BASE_DIR / "weights"
LOGS_DIR = BASE_DIR / "logs"

app = FastAPI(
    title="Furniture Classification AI API",
    description="FastAPI Backend for Furniture Classification & Grad-CAM Visualization",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
CLASS_NAMES = ['bar_stool', 'bed', 'chair', 'coffee_table', 'dining_table', 'dresser']
NUM_CLASSES = len(CLASS_NAMES)

# Out-of-Distribution (OOD) Thresholds (Sử dụng Temperature Scaling T=2.5 & Entropy Filter)
TEMPERATURE = 2.5
CALIBRATED_CONFIDENCE_THRESHOLD = 50.0  # Ngưỡng tin cậy tròn 50% (>= 50% mới là nội thất)
MARGIN_THRESHOLD = 15.0                 # Chênh lệch tối thiểu giữa Top 1-2 phải >= 15%
MAX_ENTROPY_THRESHOLD = 1.15            # Ngưỡng Entropy tối đa (Entropy > 1.15 là ảnh bị phân vân/ngoại lệ)

eval_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

MODEL_CACHE: Dict[str, nn.Module] = {}

def load_model(model_name: str) -> nn.Module:
    if model_name in MODEL_CACHE:
        return MODEL_CACHE[model_name]

    print(f"[INFO] Loading model '{model_name}' on {DEVICE}...")

    if model_name == "mobilenet_v2":
        model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
        in_features = model.classifier[1].in_features
        model.classifier[1] = nn.Linear(in_features, NUM_CLASSES)
    elif model_name == "resnet18":
        model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
        in_features = model.fc.in_features
        model.fc = nn.Linear(in_features, NUM_CLASSES)
    elif model_name == "efficientnet_b0":
        model = models.efficientnet_b0(weights=models.EfficientNet_B0_Weights.DEFAULT)
        in_features = model.classifier[1].in_features
        model.classifier[1] = nn.Linear(in_features, NUM_CLASSES)
    else:
        raise ValueError(f"Unsupported model: {model_name}")

    weight_path = WEIGHTS_DIR / f"{model_name}.pth"
    if weight_path.exists():
        print(f"[INFO] Found fine-tuned weights at {weight_path}. Loading state_dict...")
        state_dict = torch.load(weight_path, map_location=DEVICE)
        model.load_state_dict(state_dict)
        print(f"[SUCCESS] Loaded fine-tuned weights for {model_name} successfully!")
    else:
        print(f"[WARNING] Local weights NOT found at {weight_path}. Model classification head is UNTRAINED!")

    model = model.to(DEVICE)
    model.eval()
    MODEL_CACHE[model_name] = model
    return model

def get_target_layer(model: nn.Module, model_name: str) -> nn.Module:
    if model_name == "mobilenet_v2":
        return model.features[-1]
    elif model_name == "resnet18":
        return model.layer4[-1]
    elif model_name == "efficientnet_b0":
        return model.features[-1]
    else:
        raise ValueError(f"Unknown target layer for {model_name}")

class GradCAM:
    def __init__(self, model: nn.Module, target_layer: nn.Module):
        self.model = model
        self.target_layer = target_layer
        self.gradients = None
        self.activations = None

        self.target_layer.register_forward_hook(self.save_activation)
        self.target_layer.register_full_backward_hook(self.save_gradient)

    def save_activation(self, module, input, output):
        self.activations = output

    def save_gradient(self, module, grad_input, grad_output):
        self.gradients = grad_output[0]

    def __call__(self, input_tensor: torch.Tensor, class_idx: Optional[int] = None) -> np.ndarray:
        self.model.zero_grad()
        output = self.model(input_tensor)

        if class_idx is None:
            class_idx = torch.argmax(output, dim=1).item()

        score = output[0, class_idx]
        score.backward(retain_graph=True)

        gradients = self.gradients[0].cpu().data.numpy()
        activations = self.activations[0].cpu().data.numpy()

        weights = np.mean(gradients, axis=(1, 2))
        cam = np.zeros(activations.shape[1:], dtype=np.float32)

        for i, w in enumerate(weights):
            cam += w * activations[i]

        cam = np.maximum(cam, 0)
        if np.max(cam) > 0:
            cam = cam / np.max(cam)

        cam = cv2.resize(cam, (224, 224))
        return cam

def generate_gradcam_base64(pil_image: Image.Image, cam: np.ndarray) -> str:
    img_np = np.array(pil_image.resize((224, 224)))
    if len(img_np.shape) == 2:
        img_np = cv2.cvtColor(img_np, cv2.COLOR_GRAY2RGB)
    elif img_np.shape[2] == 4:
        img_np = cv2.cvtColor(img_np, cv2.COLOR_RGBA2RGB)

    heatmap = cv2.applyColorMap(np.uint8(255 * cam), cv2.COLORMAP_JET)
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)

    overlay = cv2.addWeighted(img_np, 0.5, heatmap, 0.5, 0)

    res_pil = Image.fromarray(overlay)
    buffer = io.BytesIO()
    res_pil.save(buffer, format="PNG")
    b64_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{b64_str}"

@app.get("/")
def read_root():
    return {
        "status": "online",
        "message": "Furniture Classification AI Backend is running",
        "device": str(DEVICE),
        "classes": CLASS_NAMES
    }

@app.get("/metrics")
def get_metrics():
    csv_path = LOGS_DIR / "model_comparison.csv"
    if csv_path.exists():
        df = pd.read_csv(csv_path)
        return df.to_dict(orient="records")
    else:
        return [
            {"Model": "MobileNetV2", "Acc.": 0.9455, "Prec.": 0.9445, "Recall": 0.9455, "F1": 0.9443, "ROC-AUC": 0.9961, "PR-AUC": 0.9754},
            {"Model": "ResNet18", "Acc.": 0.9448, "Prec.": 0.9428, "Recall": 0.9448, "F1": 0.9429, "ROC-AUC": 0.9958, "PR-AUC": 0.9756},
            {"Model": "EfficientNet-B0", "Acc.": 0.9416, "Prec.": 0.9397, "Recall": 0.9416, "F1": 0.9403, "ROC-AUC": 0.9963, "PR-AUC": 0.9757}
        ]

@app.post("/predict")
async def predict(
    file: UploadFile = File(...),
    model: str = Form("mobilenet_v2")
):
    valid_models = ["mobilenet_v2", "resnet18", "efficientnet_b0"]
    if model not in valid_models:
        model = "mobilenet_v2"

    try:
        contents = await file.read()
        pil_img = Image.open(io.BytesIO(contents)).convert('RGB')
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image file: {str(e)}")

    # Preprocess
    input_tensor = eval_transform(pil_img).unsqueeze(0).to(DEVICE)

    # Load model
    net = load_model(model)
    target_layer = get_target_layer(net, model)

    # Inference & timing
    start_t = time.perf_counter()
    with torch.no_grad():
        logits = net(input_tensor)
        # Raw Softmax
        probs_raw = F.softmax(logits, dim=1)[0]
        # Temperature Scaled Softmax (T = 2.5) để giải quyết triệt để vấn đề Overconfidence của Softmax trên ảnh OOD
        probs_temp = F.softmax(logits / TEMPERATURE, dim=1)[0]
        # Tính Softmax Entropy
        entropy = -torch.sum(probs_raw * torch.log(probs_raw + 1e-9)).item()

    inference_time_ms = round((time.perf_counter() - start_t) * 1000, 2)

    # Get Top-3 theo Temperature Scaled
    top3_prob_temp, top3_indices = torch.topk(probs_temp, k=3)
    raw_top3_results = []
    for p, idx in zip(top3_prob_temp, top3_indices):
        raw_top3_results.append({
            "class_name": CLASS_NAMES[idx.item()],
            "confidence": round(p.item() * 100, 2)
        })

    raw_top_class = raw_top3_results[0]["class_name"]
    calibrated_top_confidence = raw_top3_results[0]["confidence"]
    raw_top_confidence = round(probs_raw[top3_indices[0]].item() * 100, 2)
    second_confidence = raw_top3_results[1]["confidence"]
    margin = calibrated_top_confidence - second_confidence

    # Out-of-Distribution (OOD) Exception Checking
    is_valid_furniture = True
    warning_message = None

    # Kiểm tra OOD bằng 3 tiêu chí kết hợp: Ngưỡng hiệu chỉnh nhiệt độ < 50%, Margin < 15%, hoặc Entropy > 1.15
    if calibrated_top_confidence < CALIBRATED_CONFIDENCE_THRESHOLD or margin < MARGIN_THRESHOLD or entropy > MAX_ENTROPY_THRESHOLD:
        is_valid_furniture = False
        warning_message = (
            f"Hình ảnh tải lên không thuộc 6 danh mục sản phẩm nội thất của hệ thống "
            f"(Độ tin cậy hiệu chỉnh: {calibrated_top_confidence:.1f}% < {CALIBRATED_CONFIDENCE_THRESHOLD}%)."
        )
        top_class = "non_furniture"
        top_confidence = calibrated_top_confidence
        top_3 = []  # Ẩn danh sách Top-1-2-3 khi không phải đồ nội thất
    else:
        top_class = raw_top_class
        top_confidence = raw_top_confidence
        top_3 = [
            {
                "class_name": r["class_name"],
                "confidence": round(probs_raw[CLASS_NAMES.index(r["class_name"])].item() * 100, 2)
            }
            for r in raw_top3_results
        ]

    # Grad-CAM computation
    grad_cam_engine = GradCAM(net, target_layer)
    input_tensor_grad = eval_transform(pil_img).unsqueeze(0).to(DEVICE).requires_grad_(True)
    cam = grad_cam_engine(input_tensor_grad, class_idx=top3_indices[0].item())
    gradcam_b64 = generate_gradcam_base64(pil_img, cam)

    return JSONResponse({
        "top_class": top_class,
        "top_confidence": top_confidence,
        "inference_time_ms": inference_time_ms,
        "model_used": model,
        "top_3": top_3,
        "gradcam_url": gradcam_b64,
        "is_valid_furniture": is_valid_furniture,
        "warning_message": warning_message
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
