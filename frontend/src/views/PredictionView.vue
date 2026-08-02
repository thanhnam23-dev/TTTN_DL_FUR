<template>
  <div class="space-y-6 py-4">
    
    <!-- Header -->
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 p-5 rounded-xl border border-indigo-200 bg-indigo-50/80 shadow-xs">
      <div>
        <h1 class="text-xl sm:text-2xl font-extrabold text-slate-900 flex items-center gap-2">
          <ScanSearch class="w-6 h-6 text-indigo-600" />
          <span>Dự Đoán Phân Loại & Grad-CAM</span>
        </h1>
        <p class="text-xs text-slate-600 mt-0.5 font-medium">
          Upload ảnh sản phẩm nội thất để nhận diện và xem bản đồ nhiệt vùng chú ý Grad-CAM
        </p>
      </div>

      <!-- Model Selector -->
      <div class="bg-white p-1 rounded-xl border border-indigo-200 flex items-center space-x-1 shadow-xs">
        <button
          v-for="m in modelOptions"
          :key="m.id"
          @click="selectedModel = m.id"
          :class="[
            'px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center space-x-1.5',
            selectedModel === m.id
              ? 'bg-indigo-600 text-white shadow-xs'
              : 'text-slate-700 hover:bg-slate-100'
          ]"
        >
          <Cpu class="w-3.5 h-3.5" />
          <span>{{ m.label }}</span>
        </button>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
      
      <!-- Left Column: Upload & Control Panel -->
      <div class="lg:col-span-5 space-y-4">
        
        <!-- Drag and Drop Dropzone -->
        <div
          @dragover.prevent="isDragging = true"
          @dragleave.prevent="isDragging = false"
          @drop.prevent="handleDrop"
          :class="[
            'relative rounded-2xl border-2 border-dashed p-6 text-center transition-all duration-150 flex flex-col items-center justify-center min-h-[280px]',
            isDragging
              ? 'border-indigo-500 bg-indigo-100'
              : selectedImagePreview
              ? 'border-slate-300 bg-white'
              : 'border-indigo-300 bg-sky-50/60 hover:border-indigo-400'
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
          <div v-if="selectedImagePreview" class="relative w-full h-60 rounded-xl overflow-hidden group shadow-xs">
            <img :src="selectedImagePreview" class="w-full h-full object-cover rounded-xl" alt="Preview" />
            <div class="absolute inset-0 bg-slate-900/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center space-x-2">
              <button
                @click="triggerFileInput"
                class="px-3 py-1.5 rounded bg-indigo-600 text-white text-xs font-bold flex items-center gap-1 hover:bg-indigo-700 shadow-sm"
              >
                <Upload class="w-3.5 h-3.5" /> Đổi Ảnh
              </button>
              <button
                @click="clearImage"
                class="px-3 py-1.5 rounded bg-rose-600 text-white text-xs font-bold flex items-center gap-1 hover:bg-rose-700 shadow-sm"
              >
                <Trash2 class="w-3.5 h-3.5" /> Xoá
              </button>
            </div>
          </div>

          <!-- Empty Upload Prompt -->
          <div v-else class="space-y-3 cursor-pointer" @click="triggerFileInput">
            <div class="w-12 h-12 rounded-xl bg-indigo-600 text-white flex items-center justify-center mx-auto shadow-sm">
              <UploadCloud class="w-6 h-6" />
            </div>
            <div>
              <p class="text-xs font-extrabold text-slate-900">Kéo thả ảnh vào đây hoặc bấm để chọn</p>
              <p class="text-[11px] text-slate-600 mt-0.5 font-semibold">Hỗ trợ JPG, PNG, WEBP</p>
            </div>
          </div>
        </div>

        <!-- Sample Presets for 6 Furniture Classes -->
        <div class="p-4 rounded-2xl border border-sky-200 bg-sky-50/70 space-y-3 shadow-xs">
          <p class="text-xs font-extrabold text-sky-900 flex items-center gap-1.5">
            <Sparkles class="w-3.5 h-3.5 text-sky-600" />
            <span>Ảnh mẫu 6 lớp sản phẩm nội thất chuẩn:</span>
          </p>

          <div class="grid grid-cols-3 gap-2">
            <button
              v-for="sample in furnitureSamples"
              :key="sample.id"
              @click="selectSampleImage(sample)"
              :class="[
                'p-2 rounded-xl border text-left text-xs transition-all flex items-center space-x-1.5 shadow-xs',
                selectedSampleId === sample.id
                  ? 'border-indigo-600 bg-indigo-600 text-white font-extrabold'
                  : 'border-slate-200 bg-white text-slate-800 hover:border-slate-300 font-semibold'
              ]"
            >
              <span class="text-sm">{{ sample.emoji }}</span>
              <span class="truncate font-bold">{{ sample.name }}</span>
            </button>
          </div>

          <!-- OOD Exception Test Presets -->
          <div class="pt-2 border-t border-sky-200/80 space-y-2">
            <p class="text-[11px] font-extrabold text-amber-900 flex items-center gap-1.5">
              <AlertTriangle class="w-3.5 h-3.5 text-amber-600" />
              <span>Ảnh kiểm thử ngoại lệ (Không phải nội thất):</span>
            </p>

            <div class="grid grid-cols-2 gap-2">
              <button
                v-for="sample in exceptionSamples"
                :key="sample.id"
                @click="selectSampleImage(sample)"
                :class="[
                  'p-2 rounded-xl border text-left text-xs transition-all flex items-center space-x-1.5 shadow-xs',
                  selectedSampleId === sample.id
                    ? 'border-amber-600 bg-amber-600 text-white font-extrabold'
                    : 'border-amber-200 bg-white text-amber-900 hover:border-amber-300 font-semibold'
                ]"
              >
                <span class="text-sm">{{ sample.emoji }}</span>
                <span class="truncate font-bold">{{ sample.name }}</span>
              </button>
            </div>
          </div>
        </div>

        <!-- Predict Button -->
        <button
          @click="runPrediction"
          :disabled="!selectedImagePreview || isLoading"
          class="w-full py-3.5 rounded-xl font-extrabold text-xs sm:text-sm bg-indigo-600 text-white shadow-sm hover:bg-indigo-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all flex items-center justify-center space-x-2"
        >
          <Loader2 v-if="isLoading" class="w-4 h-4 animate-spin" />
          <ScanSearch v-else class="w-4 h-4" />
          <span>{{ isLoading ? 'Đang Chạy Mô Hình...' : 'Phân Loại & Xuất Grad-CAM' }}</span>
        </button>

      </div>

      <!-- Right Column: Results & Grad-CAM Panel -->
      <div class="lg:col-span-7 space-y-4">
        
        <!-- Placeholder when no result -->
        <div v-if="!result && !isLoading" class="p-12 rounded-2xl border border-slate-300 bg-white text-center space-y-3 shadow-xs">
          <div class="w-12 h-12 rounded-full bg-indigo-50 border border-indigo-200 flex items-center justify-center text-indigo-600 mx-auto">
            <Activity class="w-6 h-6" />
          </div>
          <h3 class="text-sm font-extrabold text-slate-900">Chưa Có Kết Quả Nhận Diện</h3>
          <p class="text-xs text-slate-600 max-w-xs mx-auto font-medium">
            Chọn hoặc tải ảnh lên ở bên trái và bấm nút <strong class="text-indigo-600 font-bold">"Phân Loại & Xuất Grad-CAM"</strong>
          </p>
        </div>

        <!-- Loading Skeleton -->
        <div v-else-if="isLoading" class="p-6 rounded-2xl border border-indigo-200 bg-indigo-50/50 space-y-4 animate-pulse">
          <div class="h-6 bg-indigo-200 rounded w-1/3"></div>
          <div class="h-20 bg-indigo-100 rounded"></div>
          <div class="space-y-2">
            <div class="h-4 bg-indigo-200 rounded w-1/2"></div>
            <div class="h-4 bg-indigo-100 rounded"></div>
          </div>
        </div>

        <!-- Active Prediction Result -->
        <div v-else-if="result" class="space-y-4">
          
          <!-- Out-of-Distribution (OOD) Warning Banner -->
          <div v-if="!result.is_valid_furniture" class="p-4 rounded-xl border border-amber-300 bg-amber-50 text-amber-950 space-y-1.5 shadow-xs">
            <div class="flex items-center gap-2 font-extrabold text-xs sm:text-sm text-amber-900">
              <AlertTriangle class="w-5 h-5 text-amber-600 shrink-0" />
              <span>⚠️ CẢNH BÁO NGOẠI LỆ: ẢNH KHÔNG PHẢI ĐỒ NỘI THẤT HỢP LỆ</span>
            </div>
            <p class="text-xs text-amber-800 font-semibold leading-relaxed pl-7">
              {{ result.warning_message || 'Hình ảnh tải lên có độ tin cậy thấp (< 80.0%) hoặc chênh lệch lớp nhỏ, không thuộc 6 danh mục sản phẩm nội thất của hệ thống.' }}
            </p>
          </div>

          <!-- Primary Class Result Header -->
          <div :class="[
            'p-5 rounded-2xl border relative overflow-hidden shadow-xs',
            result.is_valid_furniture
              ? 'border-emerald-300 bg-emerald-50/90'
              : 'border-amber-300 bg-amber-50/60'
          ]">
            <div class="flex items-start justify-between">
              <div>
                <span :class="[
                  'text-[11px] font-extrabold px-2.5 py-0.5 rounded border shadow-xs',
                  result.is_valid_furniture
                    ? 'text-emerald-800 bg-white border-emerald-200'
                    : 'text-amber-800 bg-white border-amber-200'
                ]">
                  {{ result.is_valid_furniture ? 'Top-1 Dự Đoán Hàng Đầu' : 'Lớp Gần Nhất (Không Khả Thi)' }}
                </span>
                <h2 class="text-2xl font-black text-slate-900 mt-1.5">
                  {{ CLASS_LABELS_VI[result.top_class] || result.top_class }}
                </h2>
                <p class="text-xs font-semibold mt-0.5" :class="result.is_valid_furniture ? 'text-emerald-900' : 'text-amber-900'">
                  Mã Lớp: <code class="font-bold font-mono">{{ result.top_class }}</code>
                </p>
              </div>

              <div class="text-right">
                <div :class="['text-3xl font-black', result.is_valid_furniture ? 'text-emerald-700' : 'text-amber-700']">
                  {{ result.top_confidence }}%
                </div>
                <div class="text-[11px] font-bold" :class="result.is_valid_furniture ? 'text-emerald-800' : 'text-amber-800'">
                  Confidence Score
                </div>
              </div>
            </div>
          </div>

          <!-- Performance Quick Badge -->
          <div class="grid grid-cols-3 gap-3">
            <div class="p-3 rounded-xl border border-indigo-200 bg-indigo-50/80 text-center shadow-xs">
              <div class="text-[11px] text-indigo-900 font-bold">Inference Time</div>
              <div class="text-base font-black text-indigo-700 mt-0.5 font-mono">{{ result.inference_time_ms }} ms</div>
            </div>
            <div class="p-3 rounded-xl border border-purple-200 bg-purple-50/80 text-center shadow-xs">
              <div class="text-[11px] text-purple-900 font-bold">Mô Hình</div>
              <div class="text-base font-black text-purple-700 mt-0.5 uppercase font-mono">{{ result.model_used }}</div>
            </div>
            <div class="p-3 rounded-xl border border-sky-200 bg-sky-50/80 text-center shadow-xs">
              <div class="text-[11px] text-sky-900 font-bold">Input Size</div>
              <div class="text-base font-black text-sky-700 mt-0.5 font-mono">224 × 224</div>
            </div>
          </div>

          <!-- Top-3 Confidence Breakdown -->
          <div class="p-5 rounded-2xl border border-slate-200 bg-white space-y-3 shadow-xs">
            <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-2">
              <BarChart3 class="w-4 h-4 text-indigo-600" />
              <span>Top-3 Dự Đoán Hàng Đầu</span>
            </h3>

            <div class="space-y-2.5">
              <div v-for="(item, idx) in result.top_3" :key="idx" class="space-y-1">
                <div class="flex justify-between text-xs font-bold">
                  <span class="text-slate-800">#{{ idx + 1 }} {{ CLASS_LABELS_VI[item.class_name] || item.class_name }}</span>
                  <span :class="idx === 0 ? (result.is_valid_furniture ? 'text-emerald-700 font-black' : 'text-amber-700 font-black') : 'text-slate-600'">
                    {{ item.confidence }}%
                  </span>
                </div>
                <div class="w-full h-2.5 bg-slate-100 rounded-full overflow-hidden border border-slate-200">
                  <div
                    class="h-full rounded-full transition-all duration-300"
                    :class="idx === 0 ? (result.is_valid_furniture ? 'bg-emerald-500' : 'bg-amber-500') : 'bg-slate-300'"
                    :style="{ width: `${item.confidence}%` }"
                  ></div>
                </div>
              </div>
            </div>
          </div>

          <!-- Grad-CAM Heatmap Visualization -->
          <div class="p-5 rounded-2xl border border-purple-200 bg-purple-50/50 space-y-3 shadow-xs">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <div>
                <h3 class="text-xs font-extrabold text-slate-900 flex items-center gap-2">
                  <Eye class="w-4 h-4 text-purple-600" />
                  <span>Giải Thích Trực Quan Grad-CAM</span>
                </h3>
                <p class="text-[11px] text-slate-600 font-medium">Bản đồ nhiệt thể hiện vùng ảnh mô hình tập trung chú ý</p>
              </div>

              <!-- View Mode Tabs -->
              <div class="bg-white p-1 rounded-xl border border-purple-200 flex items-center space-x-1 shadow-xs">
                <button
                  v-for="mode in gradCamModes"
                  :key="mode.id"
                  @click="activeGradcamMode = mode.id"
                  :class="[
                    'px-2.5 py-1 rounded-lg text-xs font-bold transition-all',
                    activeGradcamMode === mode.id
                      ? 'bg-purple-600 text-white shadow-xs'
                      : 'text-slate-700 hover:bg-slate-100'
                  ]"
                >
                  {{ mode.label }}
                </button>
              </div>
            </div>

            <!-- Image Comparison Box -->
            <div class="relative h-60 sm:h-72 rounded-xl overflow-hidden bg-slate-900 border border-slate-300 flex items-center justify-center shadow-xs">
              
              <img
                v-if="activeGradcamMode === 'original'"
                :src="selectedImagePreview!"
                class="h-full w-full object-contain"
                alt="Original"
              />

              <img
                v-else-if="activeGradcamMode === 'heatmap'"
                :src="result.gradcam_url"
                class="h-full w-full object-contain filter hue-rotate-15 contrast-125"
                alt="Heatmap"
              />

              <div v-else class="relative h-full w-full flex items-center justify-center">
                <img :src="selectedImagePreview!" class="h-full w-full object-contain" alt="Original" />
                <img
                  :src="result.gradcam_url"
                  class="absolute inset-0 h-full w-full object-contain opacity-60 mix-blend-screen"
                  alt="Grad-CAM Overlay"
                />
              </div>

            </div>

            <div class="bg-white p-3 rounded-xl border border-purple-200 text-[11px] text-purple-950 font-semibold leading-relaxed flex items-start space-x-2 shadow-xs">
              <Info class="w-4 h-4 text-purple-600 shrink-0 mt-0.5" />
              <span>
                <strong>Giải thích Grad-CAM:</strong> Vùng sáng đỏ/vàng trên bản đồ nhiệt biểu thị các đường nét đặc trưng 
                (như chân ghế, mặt bàn) mà mô hình dựa vào để đưa ra quyết định phân loại.
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
  BarChart3, Eye, Info, Activity, Loader2, AlertTriangle
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

const activeGradcamMode = ref('overlay');

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

// 6 lớp sản phẩm nội thất chuẩn
const furnitureSamples = [
  { id: 'bar_stool', name: 'Ghế Bar', emoji: '🪑', url: 'https://images.unsplash.com/photo-1503602642458-232111445657?w=400&auto=format&fit=crop&q=80' },
  { id: 'bed', name: 'Giường Ngủ', emoji: '🛏️', url: 'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=400&auto=format&fit=crop&q=80' },
  { id: 'chair', name: 'Ghế Tựa', emoji: '🛋️', url: 'https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?w=400&auto=format&fit=crop&q=80' },
  { id: 'coffee_table', name: 'Bàn Trà', emoji: '☕', url: 'https://images.unsplash.com/photo-1533090161767-e6ffed986c88?w=400&auto=format&fit=crop&q=80' },
  { id: 'dining_table', name: 'Bàn Ăn', emoji: '🍽️', url: 'https://images.unsplash.com/photo-1615066390971-03e4e1c36ddf?w=400&auto=format&fit=crop&q=80' },
  { id: 'dresser', name: 'Tủ Đồ', emoji: '🗄️', url: 'https://images.unsplash.com/photo-1595428774223-ef52624120d2?w=400&auto=format&fit=crop&q=80' },
];

// Nút kiểm thử ngoại lệ
const exceptionSamples = [
  { id: 'other_car', name: 'Xe Ô Tô (Ngoại Lệ)', emoji: '🚗', url: 'https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=400&auto=format&fit=crop&q=80' },
  { id: 'other_person', name: 'Ảnh Người (Ngoại Lệ)', emoji: '👤', url: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400&auto=format&fit=crop&q=80' },
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

function selectSampleImage(sample: { id: string; name: string; emoji: string; url: string }) {
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
