<template>
  <div class="space-y-8 py-4">
    
    <!-- Header -->
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 glass-panel p-6 rounded-2xl border border-slate-800">
      <div>
        <h1 class="text-2xl sm:text-3xl font-extrabold text-white flex items-center gap-2">
          <ScanSearch class="w-7 h-7 text-indigo-400" />
          <span>Dự Đoán Phân Loại & Grad-CAM</span>
        </h1>
        <p class="text-xs sm:text-sm text-slate-400 mt-1">
          Upload ảnh sản phẩm nội thất để hệ thống nhận diện và hiển thị bản đồ vùng chú ý
        </p>
      </div>

      <!-- Model Selector -->
      <div class="bg-slate-950 p-1.5 rounded-xl border border-slate-800 flex items-center space-x-1">
        <button
          v-for="m in modelOptions"
          :key="m.id"
          @click="selectedModel = m.id"
          :class="[
            'px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center space-x-1.5',
            selectedModel === m.id
              ? 'bg-indigo-600 text-white shadow-md shadow-indigo-500/20'
              : 'text-slate-400 hover:text-slate-200'
          ]"
        >
          <Cpu class="w-3.5 h-3.5" />
          <span>{{ m.label }}</span>
        </button>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
      
      <!-- Left Column: Upload & Control Panel -->
      <div class="lg:col-span-5 space-y-6">
        
        <!-- Drag and Drop Dropzone -->
        <div
          @dragover.prevent="isDragging = true"
          @dragleave.prevent="isDragging = false"
          @drop.prevent="handleDrop"
          :class="[
            'relative rounded-2xl border-2 border-dashed p-6 text-center transition-all duration-300 flex flex-col items-center justify-center min-h-[300px]',
            isDragging
              ? 'border-indigo-500 bg-indigo-500/10 scale-[1.01]'
              : selectedImagePreview
              ? 'border-slate-700 bg-slate-900/60'
              : 'border-slate-800 bg-slate-900/40 hover:border-slate-700'
          ]"
        >
          <input
            type="file"
            ref="fileInputRef"
            accept="image/*"
            class="hidden"
            @change="handleFileChange"
          />

          <!-- Preview Mode -->
          <div v-if="selectedImagePreview" class="relative w-full h-64 rounded-xl overflow-hidden group">
            <img :src="selectedImagePreview" class="w-full h-full object-cover rounded-xl" alt="Preview" />
            <div class="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center space-x-3">
              <button
                @click="triggerFileInput"
                class="px-3 py-2 rounded-lg bg-indigo-600 text-white text-xs font-bold flex items-center gap-1 hover:bg-indigo-500"
              >
                <Upload class="w-4 h-4" /> Đổi Ảnh
              </button>
              <button
                @click="clearImage"
                class="px-3 py-2 rounded-lg bg-red-600/80 text-white text-xs font-bold flex items-center gap-1 hover:bg-red-500"
              >
                <Trash2 class="w-4 h-4" /> Xoá
              </button>
            </div>
          </div>

          <!-- Empty Upload Prompt -->
          <div v-else class="space-y-4 cursor-pointer" @click="triggerFileInput">
            <div class="w-16 h-16 rounded-2xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400 mx-auto">
              <UploadCloud class="w-8 h-8" />
            </div>
            <div>
              <p class="text-sm font-bold text-white">Kéo thả ảnh vào đây hoặc bấm để chọn</p>
              <p class="text-xs text-slate-500 mt-1">Hỗ trợ định dạng JPG, PNG, WEBP (Tối đa 10MB)</p>
            </div>
          </div>
        </div>

        <!-- Sample Presets (Click to Test Instantly) -->
        <div class="glass-panel p-4 rounded-xl border border-slate-800 space-y-3">
          <p class="text-xs font-bold text-slate-300 flex items-center gap-1.5">
            <Sparkles class="w-3.5 h-3.5 text-indigo-400" />
            <span>Ảnh mẫu kiểm thử nhanh (Click chọn thử):</span>
          </p>

          <div class="grid grid-cols-3 gap-2">
            <button
              v-for="sample in sampleImages"
              :key="sample.id"
              @click="selectSampleImage(sample)"
              :class="[
                'p-2 rounded-lg border text-left text-xs transition-all flex items-center space-x-2',
                selectedSampleId === sample.id
                  ? 'border-indigo-500 bg-indigo-500/20 text-white'
                  : 'border-slate-800 bg-slate-900/60 text-slate-400 hover:border-slate-700'
              ]"
            >
              <span class="text-base">{{ sample.emoji }}</span>
              <span class="truncate font-semibold">{{ sample.name }}</span>
            </button>
          </div>
        </div>

        <!-- Predict Button -->
        <button
          @click="runPrediction"
          :disabled="!selectedImagePreview || isLoading"
          class="w-full py-4 rounded-2xl font-bold text-sm bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 text-white shadow-xl shadow-indigo-500/25 hover:opacity-95 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 flex items-center justify-center space-x-2"
        >
          <Loader2 v-if="isLoading" class="w-5 h-5 animate-spin" />
          <ScanSearch v-else class="w-5 h-5" />
          <span>{{ isLoading ? 'Đang Suy Luận Mô Hình...' : 'Phân Loại & Xuất Grad-CAM' }}</span>
        </button>

      </div>

      <!-- Right Column: Results & Grad-CAM Panel -->
      <div class="lg:col-span-7 space-y-6">
        
        <!-- Placeholder when no result -->
        <div v-if="!result && !isLoading" class="glass-panel p-12 rounded-2xl border border-slate-800 text-center space-y-4">
          <div class="w-16 h-16 rounded-full bg-slate-800/50 flex items-center justify-center text-slate-500 mx-auto">
            <Activity class="w-8 h-8" />
          </div>
          <h3 class="text-lg font-bold text-slate-300">Chưa Có Kết Quả Nhận Diện</h3>
          <p class="text-xs text-slate-500 max-w-sm mx-auto">
            Vui lòng chọn hoặc tải ảnh lên ở bảng bên trái và bấm nút <strong class="text-slate-400">"Phân Loại & Xuất Grad-CAM"</strong>
          </p>
        </div>

        <!-- Loading Skeleton -->
        <div v-else-if="isLoading" class="glass-panel p-8 rounded-2xl border border-slate-800 space-y-6 animate-pulse">
          <div class="h-8 bg-slate-800 rounded-lg w-1/3"></div>
          <div class="h-24 bg-slate-800/60 rounded-xl"></div>
          <div class="space-y-3">
            <div class="h-4 bg-slate-800 rounded w-1/2"></div>
            <div class="h-6 bg-slate-800/40 rounded"></div>
            <div class="h-6 bg-slate-800/40 rounded"></div>
          </div>
        </div>

        <!-- Active Prediction Result -->
        <div v-else-if="result" class="space-y-6">
          
          <!-- Primary Class Result Header -->
          <div class="glass-panel p-6 rounded-2xl border border-indigo-500/30 bg-indigo-950/20 relative overflow-hidden">
            <div class="flex items-start justify-between">
              <div>
                <span class="text-xs font-semibold text-indigo-400 bg-indigo-500/10 px-2.5 py-1 rounded-lg border border-indigo-500/20">
                  Top-1 Nhận Diện Nhiều Nhất
                </span>
                <h2 class="text-2xl sm:text-3xl font-black text-white mt-2">
                  {{ CLASS_LABELS_VI[result.top_class] || result.top_class }}
                </h2>
                <p class="text-xs text-slate-400 mt-1">Mã Lớp: <code class="text-indigo-300">{{ result.top_class }}</code></p>
              </div>

              <div class="text-right">
                <div class="text-3xl font-black text-emerald-400">{{ result.top_confidence }}%</div>
                <div class="text-[11px] text-slate-400 font-medium">Confidence Score</div>
              </div>
            </div>
          </div>

          <!-- Performance Quick Badge -->
          <div class="grid grid-cols-3 gap-3">
            <div class="glass-panel p-3.5 rounded-xl border border-slate-800 text-center">
              <div class="text-xs text-slate-400">Inference Time</div>
              <div class="text-base font-extrabold text-indigo-400 mt-0.5">{{ result.inference_time_ms }} ms</div>
            </div>
            <div class="glass-panel p-3.5 rounded-xl border border-slate-800 text-center">
              <div class="text-xs text-slate-400">Mô Hình Sử Dụng</div>
              <div class="text-base font-extrabold text-purple-400 mt-0.5 uppercase">{{ result.model_used }}</div>
            </div>
            <div class="glass-panel p-3.5 rounded-xl border border-slate-800 text-center">
              <div class="text-xs text-slate-400">Input Size</div>
              <div class="text-base font-extrabold text-emerald-400 mt-0.5">224 × 224</div>
            </div>
          </div>

          <!-- Top-3 Confidence Breakdown -->
          <div class="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
              <BarChart3 class="w-4 h-4 text-indigo-400" />
              <span>Top-3 Dự Đoán Hàng Đầu</span>
            </h3>

            <div class="space-y-3">
              <div v-for="(item, idx) in result.top_3" :key="idx" class="space-y-1.5">
                <div class="flex justify-between text-xs font-semibold">
                  <span class="text-slate-200">#{{ idx + 1 }} {{ CLASS_LABELS_VI[item.class_name] || item.class_name }}</span>
                  <span :class="idx === 0 ? 'text-emerald-400 font-bold' : 'text-slate-400'">{{ item.confidence }}%</span>
                </div>
                <div class="w-full h-2.5 bg-slate-950 rounded-full overflow-hidden p-0.5 border border-slate-800">
                  <div
                    class="h-full rounded-full transition-all duration-500"
                    :class="idx === 0 ? 'bg-gradient-to-r from-indigo-500 to-emerald-400' : 'bg-slate-700'"
                    :style="{ width: `${item.confidence}%` }"
                  ></div>
                </div>
              </div>
            </div>
          </div>

          <!-- Grad-CAM Heatmap Visualization -->
          <div class="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div>
                <h3 class="text-sm font-bold text-white flex items-center gap-2">
                  <Eye class="w-4 h-4 text-purple-400" />
                  <span>Giải Thích Trực Quan Grad-CAM</span>
                </h3>
                <p class="text-xs text-slate-400">Bản đồ nhiệt thể hiện vùng ảnh mô hình tập trung chú ý</p>
              </div>

              <!-- View Mode Tabs -->
              <div class="bg-slate-950 p-1 rounded-xl border border-slate-800 flex items-center space-x-1">
                <button
                  v-for="mode in gradCamModes"
                  :key="mode.id"
                  @click="activeGradcamMode = mode.id"
                  :class="[
                    'px-2.5 py-1 rounded-lg text-xs font-semibold transition-all',
                    activeGradcamMode === mode.id
                      ? 'bg-purple-600 text-white'
                      : 'text-slate-400 hover:text-slate-200'
                  ]"
                >
                  {{ mode.label }}
                </button>
              </div>
            </div>

            <!-- Image Comparison Box -->
            <div class="relative h-64 sm:h-80 rounded-xl overflow-hidden bg-slate-950 border border-slate-800 flex items-center justify-center">
              
              <!-- Original Image -->
              <img
                v-if="activeGradcamMode === 'original'"
                :src="selectedImagePreview!"
                class="h-full w-full object-contain"
                alt="Original"
              />

              <!-- Heatmap Only -->
              <img
                v-else-if="activeGradcamMode === 'heatmap'"
                :src="result.gradcam_url"
                class="h-full w-full object-contain filter hue-rotate-15 contrast-125"
                alt="Heatmap"
              />

              <!-- Overlay Mode (Original + Heatmap) -->
              <div v-else class="relative h-full w-full flex items-center justify-center">
                <img :src="selectedImagePreview!" class="h-full w-full object-contain" alt="Original" />
                <img
                  :src="result.gradcam_url"
                  class="absolute inset-0 h-full w-full object-contain opacity-60 mix-blend-screen"
                  alt="Grad-CAM Overlay"
                />
              </div>

            </div>

            <div class="bg-slate-900/60 p-3 rounded-xl border border-slate-800/80 text-[11px] text-slate-400 leading-relaxed flex items-start space-x-2">
              <Info class="w-4 h-4 text-purple-400 shrink-0 mt-0.5" />
              <span>
                <strong>Giải thích Grad-CAM:</strong> Vùng đỏ/vàng trên bản đồ nhiệt biểu thị các đường nét đặc trưng 
                (như chân ghế, tựa lưng, mặt bàn) mà mô hình dựa vào để đưa ra quyết định phân loại.
              </span>
            </div>

          </div>

        </div>

      </div>

    </div>

  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import {
  ScanSearch, Upload, UploadCloud, Trash2, Cpu, Sparkles,
  BarChart3, Eye, Info, Activity, Loader2
} from 'lucide-vue-next';
import {
  predictFurnitureImage, CLASS_LABELS_VI, type PredictionResult
} from '../services/api';

const fileInputRef = ref<HTMLInputElement | null>(null);
const isDragging = ref(false);
const selectedImagePreview = ref<string | null>(null);
const selectedFile = ref<File | string | null>(null);
const selectedSampleId = ref<string | null>(null);

const selectedModel = ref('mobilenet_v2');
const isLoading = ref(false);
const result = ref<PredictionResult | null>(null);

const activeGradcamMode = ref('overlay'); // 'overlay' | 'original' | 'heatmap'

const modelOptions = [
  { id: 'mobilenet_v2', label: 'MobileNetV2' },
  { id: 'resnet18', label: 'ResNet18' },
  { id: 'efficientnet_b0', label: 'EfficientNet-B0' }
];

const gradCamModes = [
  { id: 'overlay', label: 'Chồng Ảnh' },
  { id: 'heatmap', label: 'Bản Đồ Nhiệt' },
  { id: 'original', label: 'Ảnh Gốc' }
];

const sampleImages = [
  { id: 'bar_stool', name: 'Ghế Bar', emoji: '🪑', url: 'https://images.unsplash.com/photo-1503602642458-232111445657?w=400&auto=format&fit=crop&q=80' },
  { id: 'bed', name: 'Giường Ngủ', emoji: '🛏️', url: 'https://images.unsplash.com/photo-1540518614846-7ede433c5173?w=400&auto=format&fit=crop&q=80' },
  { id: 'chair', name: 'Ghế Tựa', emoji: '🛋️', url: 'https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?w=400&auto=format&fit=crop&q=80' },
  { id: 'coffee_table', name: 'Bàn Trà', emoji: '☕', url: 'https://images.unsplash.com/photo-1533090161767-e6ffed986c88?w=400&auto=format&fit=crop&q=80' },
  { id: 'dining_table', name: 'Bàn Ăn', emoji: '🍽️', url: 'https://images.unsplash.com/photo-1615066390971-03e4e1c36ddf?w=400&auto=format&fit=crop&q=80' },
  { id: 'dresser', name: 'Tủ Đồ', emoji: '🗄️', url: 'https://images.unsplash.com/photo-1595428774223-ef52624120d2?w=400&auto=format&fit=crop&q=80' },
];

function triggerFileInput() {
  fileInputRef.value?.click();
}

function handleFileChange(e: Event) {
  const target = e.target as HTMLInputElement;
  if (target.files && target.files[0]) {
    const file = target.files[0];
    selectedFile.value = file;
    selectedImagePreview.value = URL.createObjectURL(file);
    selectedSampleId.value = null;
    result.value = null;
  }
}

function handleDrop(e: DragEvent) {
  isDragging.value = false;
  if (e.dataTransfer?.files && e.dataTransfer.files[0]) {
    const file = e.dataTransfer.files[0];
    selectedFile.value = file;
    selectedImagePreview.value = URL.createObjectURL(file);
    selectedSampleId.value = null;
    result.value = null;
  }
}

function selectSampleImage(sample: typeof sampleImages[0]) {
  selectedSampleId.value = sample.id;
  selectedFile.value = sample.url;
  selectedImagePreview.value = sample.url;
  result.value = null;
}

function clearImage() {
  selectedFile.value = null;
  selectedImagePreview.value = null;
  selectedSampleId.value = null;
  result.value = null;
}

async function runPrediction() {
  if (!selectedFile.value) return;
  isLoading.value = true;
  try {
    const res = await predictFurnitureImage(selectedFile.value, selectedModel.value);
    result.value = res;
  } catch (err) {
    console.error('Prediction failed:', err);
  } finally {
    isLoading.value = false;
  }
}
</script>
