import os
import sys
import json
import time
import copy
import numpy as np
import pandas as pd
from pathlib import Path

# Ep encoding UTF-8 cho stdout/stderr tren Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, average_precision_score, confusion_matrix
)
from sklearn.preprocessing import label_binarize

# Config paths
DATASET_DIR = Path(r"S:\Thực tập tốt nghiệp\dataset")
WEIGHTS_DIR = Path(r"S:\Thực tập tốt nghiệp\weights")
LOGS_DIR = Path(r"S:\Thực tập tốt nghiệp\logs")
PLOTS_DIR = Path(r"S:\Thực tập tốt nghiệp\plots")

WEIGHTS_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)
PLOTS_DIR.mkdir(parents=True, exist_ok=True)

# Hyperparameters
BATCH_SIZE = 32
NUM_CLASSES = 6
STAGE1_EPOCHS = 10
STAGE2_EPOCHS = 20
NUM_WORKERS = 0  # 0 worker trên Windows
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Data Transformations
data_transforms = {
    'train': transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'test': transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

def safe_pil_loader(path):
    with open(path, 'rb') as f:
        img = Image.open(f)
        return img.convert('RGB')

def get_dataloaders():
    image_datasets = {
        x: datasets.ImageFolder(DATASET_DIR / x, data_transforms[x], loader=safe_pil_loader)
        for x in ['train', 'val', 'test']
    }

    dataloaders = {
        x: DataLoader(image_datasets[x], batch_size=BATCH_SIZE, shuffle=(x == 'train'), num_workers=NUM_WORKERS, pin_memory=True)
        for x in ['train', 'val', 'test']
    }

    class_names = image_datasets['train'].classes
    return dataloaders, image_datasets, class_names

def get_model(model_name, num_classes=NUM_CLASSES):
    if model_name == "mobilenet_v2":
        model = models.mobilenet_v2(weights=models.MobileNet_V2_Weights.DEFAULT)
        in_features = model.classifier[1].in_features
        model.classifier[1] = nn.Linear(in_features, num_classes)
        return model, "classifier"
    elif model_name == "resnet18":
        model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
        in_features = model.fc.in_features
        model.fc = nn.Linear(in_features, num_classes)
        return model, "fc"
    elif model_name == "efficientnet_b0":
        model = models.efficientnet_b0(weights=models.EfficientNet_B0_Weights.DEFAULT)
        in_features = model.classifier[1].in_features
        model.classifier[1] = nn.Linear(in_features, num_classes)
        return model, "classifier"
    else:
        raise ValueError(f"Unknown model_name: {model_name}")

def format_time(seconds):
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h > 0:
        return f"{h}h{m:02d}m{s:02d}s"
    elif m > 0:
        return f"{m:02d}m{s:02d}s"
    else:
        return f"{s:02d}s"

def train_model(model_name, dataloaders, image_datasets, class_names):
    print(f"\n==========================================")
    print(f"=== Start Training Model: {model_name} (30 Epochs) ===")
    print(f"==========================================")

    save_path = WEIGHTS_DIR / f"{model_name}.pth"

    model, head_name = get_model(model_name)
    model = model.to(DEVICE)
    criterion = nn.CrossEntropyLoss()

    history = {
        "train_loss": [], "val_loss": [],
        "train_acc": [], "val_acc": []
    }

    # ------------------ STAGE 1: Freeze backbone ------------------
    print(f"\n--- Stage 1: Freeze Backbone & Train Head ({STAGE1_EPOCHS} Epochs, LR=1e-3) ---")
    for name, param in model.named_parameters():
        if head_name not in name:
            param.requires_grad = False
        else:
            param.requires_grad = True

    optimizer = optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=1e-3)

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0
    total_epochs = STAGE1_EPOCHS + STAGE2_EPOCHS

    for epoch in range(1, STAGE1_EPOCHS + 1):
        epoch_start_time = time.time()
        phase_times = {}

        for phase in ['train', 'val']:
            phase_start_time = time.time()

            if phase == 'train':
                model.train()
            else:
                model.eval()

            running_loss = 0.0
            running_corrects = 0
            total_batches = len(dataloaders[phase])

            print(f"\n-> [{phase.upper()}] Phase | Epoch {epoch:02d}/{total_epochs:02d} ({total_batches} batches)")

            for step, (inputs, labels) in enumerate(dataloaders[phase], start=1):
                inputs = inputs.to(DEVICE)
                labels = labels.to(DEVICE)

                optimizer.zero_grad()

                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)

                # Cập nhật thông báo có thời gian trôi qua (Elapsed) & thời gian dự kiến còn lại (ETA)
                if step % 20 == 0 or step == total_batches:
                    elapsed_phase = time.time() - phase_start_time
                    avg_time_per_batch = elapsed_phase / step
                    eta_phase = avg_time_per_batch * (total_batches - step)

                    curr_loss = running_loss / (step * BATCH_SIZE)
                    curr_acc = (running_corrects.double() / (step * BATCH_SIZE)).item()
                    percent = (step / total_batches) * 100
                    current_lr = optimizer.param_groups[0]['lr']

                    print(f"   [{phase.upper()}] Step {step:03d}/{total_batches:03d} ({percent:5.1f}%) | Time: {format_time(elapsed_phase)} (ETA: {format_time(eta_phase)}) | Loss: {curr_loss:.4f} | Acc: {curr_acc:.4f} | LR: {current_lr:.1e}", flush=True)

            phase_times[phase] = time.time() - phase_start_time
            epoch_loss = running_loss / len(image_datasets[phase])
            epoch_acc = (running_corrects.double() / len(image_datasets[phase])).item()

            if phase == 'train':
                history["train_loss"].append(epoch_loss)
                history["train_acc"].append(epoch_acc)
            else:
                history["val_loss"].append(epoch_loss)
                history["val_acc"].append(epoch_acc)

                if epoch_acc > best_acc:
                    best_acc = epoch_acc
                    best_model_wts = copy.deepcopy(model.state_dict())

        total_epoch_time = time.time() - epoch_start_time
        print(f"\n=> [SUMMARY Epoch {epoch:02d}/{total_epochs:02d}] Total Time: {format_time(total_epoch_time)} (Train: {format_time(phase_times['train'])}, Val: {format_time(phase_times['val'])})")
        print(f"   Train Loss: {history['train_loss'][-1]:.4f} | Train Acc: {history['train_acc'][-1]:.4f}")
        print(f"   Val Loss  : {history['val_loss'][-1]:.4f} | Val Acc  : {history['val_acc'][-1]:.4f} (Best Val Acc: {best_acc:.4f})")

    # ------------------ STAGE 2: Unfreeze backbone ------------------
    print(f"\n--- Stage 2: Unfreeze Backbone & Fine-tune All Layers ({STAGE2_EPOCHS} Epochs, LR=1e-5) ---")
    for param in model.parameters():
        param.requires_grad = True

    optimizer = optim.Adam(model.parameters(), lr=1e-5)

    for epoch in range(STAGE1_EPOCHS + 1, total_epochs + 1):
        epoch_start_time = time.time()
        phase_times = {}

        for phase in ['train', 'val']:
            phase_start_time = time.time()

            if phase == 'train':
                model.train()
            else:
                model.eval()

            running_loss = 0.0
            running_corrects = 0
            total_batches = len(dataloaders[phase])

            print(f"\n-> [{phase.upper()}] Phase | Epoch {epoch:02d}/{total_epochs:02d} ({total_batches} batches)")

            for step, (inputs, labels) in enumerate(dataloaders[phase], start=1):
                inputs = inputs.to(DEVICE)
                labels = labels.to(DEVICE)

                optimizer.zero_grad()

                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)

                # Cập nhật thông báo có thời gian trôi qua (Elapsed) & thời gian dự kiến còn lại (ETA)
                if step % 20 == 0 or step == total_batches:
                    elapsed_phase = time.time() - phase_start_time
                    avg_time_per_batch = elapsed_phase / step
                    eta_phase = avg_time_per_batch * (total_batches - step)

                    curr_loss = running_loss / (step * BATCH_SIZE)
                    curr_acc = (running_corrects.double() / (step * BATCH_SIZE)).item()
                    percent = (step / total_batches) * 100
                    current_lr = optimizer.param_groups[0]['lr']

                    print(f"   [{phase.upper()}] Step {step:03d}/{total_batches:03d} ({percent:5.1f}%) | Time: {format_time(elapsed_phase)} (ETA: {format_time(eta_phase)}) | Loss: {curr_loss:.4f} | Acc: {curr_acc:.4f} | LR: {current_lr:.1e}", flush=True)

            phase_times[phase] = time.time() - phase_start_time
            epoch_loss = running_loss / len(image_datasets[phase])
            epoch_acc = (running_corrects.double() / len(image_datasets[phase])).item()

            if phase == 'train':
                history["train_loss"].append(epoch_loss)
                history["train_acc"].append(epoch_acc)
            else:
                history["val_loss"].append(epoch_loss)
                history["val_acc"].append(epoch_acc)

                if epoch_acc > best_acc:
                    best_acc = epoch_acc
                    best_model_wts = copy.deepcopy(model.state_dict())

        total_epoch_time = time.time() - epoch_start_time
        print(f"\n=> [SUMMARY Epoch {epoch:02d}/{total_epochs:02d}] Total Time: {format_time(total_epoch_time)} (Train: {format_time(phase_times['train'])}, Val: {format_time(phase_times['val'])})")
        print(f"   Train Loss: {history['train_loss'][-1]:.4f} | Train Acc: {history['train_acc'][-1]:.4f}")
        print(f"   Val Loss  : {history['val_loss'][-1]:.4f} | Val Acc  : {history['val_acc'][-1]:.4f} (Best Val Acc: {best_acc:.4f})")

    # Load best weights & Save
    model.load_state_dict(best_model_wts)
    torch.save(model.state_dict(), save_path)
    print(f"\n[SUCCESS] Saved best weights to {save_path.name} (Best Val Acc: {best_acc:.4f})")

    # Save history json
    history_file = LOGS_DIR / f"{model_name}_history.json"
    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(history, f, indent=4)

    # ------------------ EVALUATE ON TEST SET ------------------
    metrics = evaluate_on_test(model, model_name, dataloaders, class_names)
    return metrics

def evaluate_on_test(model, model_name, dataloaders, class_names):
    print(f"\n--- Evaluating Model {model_name} on Test Set ---")
    model.eval()

    all_preds = []
    all_targets = []
    all_probs = []

    softmax = nn.Softmax(dim=1)

    with torch.no_grad():
        for inputs, labels in dataloaders['test']:
            inputs = inputs.to(DEVICE)
            outputs = model(inputs)
            probs = softmax(outputs)
            _, preds = torch.max(outputs, 1)

            all_preds.extend(preds.cpu().numpy())
            all_targets.extend(labels.numpy())
            all_probs.extend(probs.cpu().numpy())

    all_preds = np.array(all_preds)
    all_targets = np.array(all_targets)
    all_probs = np.array(all_probs)

    y_test_bin = label_binarize(all_targets, classes=list(range(NUM_CLASSES)))

    acc = accuracy_score(all_targets, all_preds)
    prec = precision_score(all_targets, all_preds, average='weighted')
    rec = recall_score(all_targets, all_preds, average='weighted')
    f1 = f1_score(all_targets, all_preds, average='weighted')
    roc_auc = roc_auc_score(y_test_bin, all_probs, multi_class='ovr', average='weighted')
    pr_auc = average_precision_score(y_test_bin, all_probs, average='weighted')

    cm = confusion_matrix(all_targets, all_preds).tolist()

    metrics = {
        "Model": model_name,
        "Acc.": round(float(acc), 4),
        "Prec.": round(float(prec), 4),
        "Recall": round(float(rec), 4),
        "F1": round(float(f1), 4),
        "ROC-AUC": round(float(roc_auc), 4),
        "PR-AUC": round(float(pr_auc), 4)
    }

    eval_file = LOGS_DIR / f"{model_name}_metrics.json"
    eval_data = {
        "metrics": metrics,
        "confusion_matrix": cm,
        "class_names": class_names,
        "targets": all_targets.tolist(),
        "probabilities": all_probs.tolist()
    }
    with open(eval_file, 'w', encoding='utf-8') as f:
        json.dump(eval_data, f, indent=4)

    print(f"Metrics for {model_name}:")
    print(f"  Accuracy : {acc:.4f}")
    print(f"  Precision: {prec:.4f}")
    print(f"  Recall   : {rec:.4f}")
    print(f"  F1-Score : {f1:.4f}")
    print(f"  ROC-AUC  : {roc_auc:.4f}")
    print(f"  PR-AUC   : {pr_auc:.4f}")

    return metrics

def main():
    print(f"[INFO] Using device: {DEVICE}")
    dataloaders, image_datasets, class_names = get_dataloaders()
    print(f"[INFO] Class names ({len(class_names)}): {class_names}")

    models_to_train = ["mobilenet_v2", "resnet18", "efficientnet_b0"]
    all_metrics = []

    for m in models_to_train:
        m_metrics = train_model(m, dataloaders, image_datasets, class_names)
        all_metrics.append(m_metrics)

    df = pd.DataFrame(all_metrics)
    csv_path = LOGS_DIR / "model_comparison.csv"
    df.to_csv(csv_path, index=False, encoding='utf-8-sig')

    print(f"\n==========================================")
    print(f"=== ALL 3 MODELS EVALUATION COMPLETED ===")
    print(f"==========================================")
    print(df.to_string(index=False))
    print(f"\nSaved CSV log to: {csv_path}")

if __name__ == "__main__":
    main()
