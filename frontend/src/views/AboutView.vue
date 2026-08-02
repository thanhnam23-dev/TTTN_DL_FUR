<template>
  <div class="space-y-6 py-4">
    
    <!-- Header -->
    <div class="glass-panel p-5 sm:p-6 rounded-xl border border-slate-200 bg-white space-y-1 shadow-xs">
      <div class="inline-flex items-center space-x-2 px-2.5 py-1 rounded bg-indigo-50 text-indigo-700 text-xs font-semibold border border-indigo-200">
        <Info class="w-3.5 h-3.5 text-indigo-600" />
        <span>Thông Tin Đồ Án</span>
      </div>
      <h1 class="text-xl sm:text-2xl font-bold text-slate-900">Về Đề Tài Thực Tập Tốt Nghiệp</h1>
      <p class="text-xs text-slate-500">
        Giới thiệu bộ dữ liệu, quy trình huấn luyện Fine-tuning và công nghệ sử dụng trong hệ thống
      </p>
    </div>

    <!-- Tech Stack Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      
      <!-- Left: Dataset Info -->
      <div class="glass-panel p-5 rounded-xl border border-slate-200 bg-white space-y-3 shadow-xs">
        <h3 class="text-base font-bold text-slate-900 flex items-center gap-2">
          <Database class="w-4 h-4 text-indigo-600" />
          <span>Bộ Dữ Liệu (Furniture Dataset)</span>
        </h3>
        <p class="text-xs text-slate-600 leading-relaxed">
          Bộ dữ liệu huấn luyện được thu thập từ Kaggle (Multi-Angle AI Training), gồm 10,364 ảnh nội thất 
          thuộc 6 lớp sản phẩm phổ biến, được làm sạch và phân chia theo tỷ lệ chuẩn 70% Train, 15% Validation, 15% Test.
        </p>

        <div class="space-y-2 pt-1">
          <div v-for="cls in classDetails" :key="cls.name" class="flex items-center justify-between text-xs p-2.5 rounded-lg bg-slate-50 border border-slate-200">
            <span class="font-bold text-slate-900 flex items-center gap-2">
              <span>{{ cls.emoji }}</span>
              <span>{{ cls.name }}</span>
            </span>
            <div class="flex items-center space-x-3 text-slate-600 font-mono">
              <span>Tổng: <strong class="text-slate-900">{{ cls.total }}</strong></span>
              <span class="text-indigo-600 font-semibold">Train: {{ cls.train }}</span>
              <span class="text-purple-600 font-semibold">Val: {{ cls.val }}</span>
              <span class="text-emerald-600 font-semibold">Test: {{ cls.test }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Right: Preprocessing & Training Methodology -->
      <div class="space-y-4">
        
        <!-- Preprocessing Card -->
        <div class="glass-panel p-5 rounded-xl border border-slate-200 bg-white space-y-2.5 shadow-xs">
          <h3 class="text-base font-bold text-slate-900 flex items-center gap-2">
            <Sliders class="w-4 h-4 text-purple-600" />
            <span>Tiền Xử Lý & Data Augmentation</span>
          </h3>
          <ul class="space-y-2 text-xs text-slate-700">
            <li class="flex items-center gap-2">
              <CheckCircle2 class="w-4 h-4 text-emerald-600 shrink-0" />
              <span><strong>Resize & Crop:</strong> Đưa ảnh về kích thước chuẩn 224 × 224 pixel.</span>
            </li>
            <li class="flex items-center gap-2">
              <CheckCircle2 class="w-4 h-4 text-emerald-600 shrink-0" />
              <span><strong>Normalize ImageNet:</strong> Mean=[0.485, 0.456, 0.406], Std=[0.229, 0.224, 0.225].</span>
            </li>
            <li class="flex items-center gap-2">
              <CheckCircle2 class="w-4 h-4 text-emerald-600 shrink-0" />
              <span><strong>Data Augmentation:</strong> Random Horizontal Flip, Rotation (15°), Color Jitter.</span>
            </li>
          </ul>
        </div>

        <!-- 2-Stage Training Strategy Card -->
        <div class="glass-panel p-5 rounded-xl border border-slate-200 bg-white space-y-2.5 shadow-xs">
          <h3 class="text-base font-bold text-slate-900 flex items-center gap-2">
            <Cpu class="w-4 h-4 text-emerald-600" />
            <span>Quy Trình Fine-Tuning 2 Giai Đoạn</span>
          </h3>
          
          <div class="space-y-2 text-xs">
            <div class="p-3 rounded-lg bg-indigo-50/70 border border-indigo-200">
              <h4 class="font-bold text-indigo-900">Giai đoạn 1 (10 Epochs - Freeze Backbone):</h4>
              <p class="text-indigo-800 mt-0.5">Đóng băng các lớp backbone, chỉ huấn luyện lớp phân loại Fully Connected (FC Head) với LR = 1e-3.</p>
            </div>

            <div class="p-3 rounded-lg bg-purple-50/70 border border-purple-200">
              <h4 class="font-bold text-purple-900">Giai đoạn 2 (20 Epochs - Unfreeze Full Model):</h4>
              <p class="text-purple-800 mt-0.5">Mở đóng băng toàn bộ mô hình, fine-tune sâu tất cả các layer với LR = 1e-5 để tối ưu hóa đặc trưng.</p>
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- Technologies Used Badge Section -->
    <div class="glass-panel p-5 rounded-xl border border-slate-200 bg-white space-y-3 shadow-xs">
      <h3 class="text-base font-bold text-slate-900">Công Nghệ & Thư Viện Sử Dụng</h3>
      
      <div class="flex flex-wrap gap-2.5">
        <span v-for="t in techStack" :key="t.name" class="px-3 py-1.5 rounded-lg bg-slate-50 border border-slate-200 flex items-center space-x-2 text-xs font-bold text-slate-800">
          <span>{{ t.icon }}</span>
          <span>{{ t.name }}</span>
          <span class="text-[10px] text-indigo-600 font-mono">({{ t.role }})</span>
        </span>
      </div>
    </div>

  </div>
</template>

<script setup lang="ts">
import { Info, Database, Sliders, CheckCircle2, Cpu } from 'lucide-vue-next';

const classDetails = [
  { name: 'Ghế Quầy Bar (Bar Stool)', total: 1665, train: 1165, val: 249, test: 251, emoji: '🪑' },
  { name: 'Giường Ngủ (Bed)', total: 2862, train: 2003, val: 429, test: 430, emoji: '🛏️' },
  { name: 'Ghế Tựa (Chair)', total: 980, train: 686, val: 147, test: 147, emoji: '🛋️' },
  { name: 'Bàn Trà (Coffee Table)', total: 528, train: 369, val: 79, test: 80, emoji: '☕' },
  { name: 'Bàn Ăn (Dining Table)', total: 2355, train: 1648, val: 353, test: 354, emoji: '🍽️' },
  { name: 'Tủ Trang Điểm (Dresser)', total: 1974, train: 1381, val: 296, test: 297, emoji: '🗄️' },
];

const techStack = [
  { name: 'PyTorch 2.13', role: 'Deep Learning Core', icon: '🔥' },
  { name: 'FastAPI', role: 'Backend REST API', icon: '⚡' },
  { name: 'Vue 3 + TypeScript', role: 'Frontend UI', icon: '💚' },
  { name: 'Tailwind CSS', role: 'Styling & Design System', icon: '🎨' },
  { name: 'Torchvision', role: 'Pretrained CNN Models', icon: '👁️' },
  { name: 'Grad-CAM', role: 'Model Interpretability', icon: '🎯' },
  { name: 'Chart.js', role: 'Interactive Visualizations', icon: '📊' },
  { name: 'Vite', role: 'Build Tool & Dev Server', icon: '⚡' },
];
</script>
