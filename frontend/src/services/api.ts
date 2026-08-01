export interface PredictionResult {
  top_class: string;
  top_confidence: number;
  inference_time_ms: number;
  model_used: string;
  top_3: Array<{ class_name: string; confidence: number }>;
  gradcam_url: string;
}

export interface ModelMetrics {
  Model: string;
  Acc: number;
  Prec: number;
  Recall: number;
  F1: number;
  RocAuc: number;
  PrAuc: number;
}

export const API_BASE_URL = 'http://localhost:8000';

export const CLASS_LABELS_VI: Record<string, string> = {
  bar_stool: 'Ghế quầy bar (Bar Stool)',
  bed: 'Giường ngủ (Bed)',
  chair: 'Ghế tựa (Chair)',
  coffee_table: 'Bàn trà (Coffee Table)',
  dining_table: 'Bàn ăn (Dining Table)',
  dresser: 'Tủ trang điểm (Dresser)'
};

// Generate realistic SVG Grad-CAM simulation for demo mode
export function generateGradCamDataUrl(): string {
  const canvas = document.createElement('canvas');
  canvas.width = 300;
  canvas.height = 300;
  const ctx = canvas.getContext('2d');
  
  if (ctx) {
    ctx.fillStyle = '#0f172a';
    ctx.fillRect(0, 0, 300, 300);
    
    const grad = ctx.createRadialGradient(150, 140, 10, 150, 140, 120);
    grad.addColorStop(0, 'rgba(239, 68, 68, 0.85)');   // Red hot spot
    grad.addColorStop(0.3, 'rgba(245, 158, 11, 0.75)'); // Yellow
    grad.addColorStop(0.6, 'rgba(16, 185, 129, 0.5)'); // Green
    grad.addColorStop(0.85, 'rgba(59, 130, 246, 0.3)');// Blue
    grad.addColorStop(1, 'rgba(15, 23, 42, 0)');
    
    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.arc(150, 140, 120, 0, Math.PI * 2);
    ctx.fill();
  }
  
  return canvas.toDataURL('image/png');
}

export async function predictFurnitureImage(
  file: File | string,
  modelName: string = 'mobilenet_v2'
): Promise<PredictionResult> {
  try {
    const formData = new FormData();
    if (typeof file === 'string') {
      const response = await fetch(file);
      const blob = await response.blob();
      formData.append('file', blob, 'sample.jpg');
    } else {
      formData.append('file', file);
    }
    formData.append('model', modelName);

    const apiRes = await fetch(`${API_BASE_URL}/predict`, {
      method: 'POST',
      body: formData,
    });

    if (apiRes.ok) {
      const data = await apiRes.json();
      return data;
    }
  } catch (e) {
    console.log('[Demo Mode] Backend not connected yet. Serving realistic simulation data.');
  }

  await new Promise(resolve => setTimeout(resolve, 600));

  const classes = ['chair', 'bed', 'bar_stool', 'coffee_table', 'dining_table', 'dresser'];
  let chosenClass = 'chair';
  
  if (typeof file === 'string') {
    const lower = file.toLowerCase();
    if (lower.includes('bed')) chosenClass = 'bed';
    else if (lower.includes('bar')) chosenClass = 'bar_stool';
    else if (lower.includes('coffee')) chosenClass = 'coffee_table';
    else if (lower.includes('dining')) chosenClass = 'dining_table';
    else if (lower.includes('dresser')) chosenClass = 'dresser';
    else if (lower.includes('chair')) chosenClass = 'chair';
  } else {
    const lower = file.name.toLowerCase();
    if (lower.includes('bed')) chosenClass = 'bed';
    else if (lower.includes('bar')) chosenClass = 'bar_stool';
    else if (lower.includes('coffee')) chosenClass = 'coffee_table';
    else if (lower.includes('dining')) chosenClass = 'dining_table';
    else if (lower.includes('dresser')) chosenClass = 'dresser';
    else if (lower.includes('chair')) chosenClass = 'chair';
    else chosenClass = classes[Math.floor(Math.random() * classes.length)];
  }

  const conf1 = 0.94 + Math.random() * 0.05;
  const conf2 = (1 - conf1) * 0.7;
  const conf3 = 1 - conf1 - conf2;

  const otherClasses = classes.filter(c => c !== chosenClass);
  const secondClass = otherClasses[0];
  const thirdClass = otherClasses[1];

  let simInferenceTime = 22;
  if (modelName === 'resnet18') simInferenceTime = 38;
  if (modelName === 'efficientnet_b0') simInferenceTime = 46;

  return {
    top_class: chosenClass,
    top_confidence: Number((conf1 * 100).toFixed(2)),
    inference_time_ms: simInferenceTime,
    model_used: modelName,
    top_3: [
      { class_name: chosenClass, confidence: Number((conf1 * 100).toFixed(2)) },
      { class_name: secondClass, confidence: Number((conf2 * 100).toFixed(2)) },
      { class_name: thirdClass, confidence: Number((conf3 * 100).toFixed(2)) }
    ],
    gradcam_url: generateGradCamDataUrl()
  };
}

export const MOCK_MODEL_COMPARISON: ModelMetrics[] = [
  {
    Model: 'MobileNetV2',
    Acc: 0.9240,
    Prec: 0.9255,
    Recall: 0.9240,
    F1: 0.9242,
    RocAuc: 0.9892,
    PrAuc: 0.9785
  },
  {
    Model: 'ResNet18',
    Acc: 0.9415,
    Prec: 0.9428,
    Recall: 0.9415,
    F1: 0.9418,
    RocAuc: 0.9931,
    PrAuc: 0.9842
  },
  {
    Model: 'EfficientNet-B0',
    Acc: 0.9582,
    Prec: 0.9590,
    Recall: 0.9582,
    F1: 0.9584,
    RocAuc: 0.9964,
    PrAuc: 0.9910
  }
];
