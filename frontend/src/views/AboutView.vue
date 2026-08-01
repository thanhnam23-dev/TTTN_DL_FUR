<template>
  <div class="space-y-8 py-4">
    
    <!-- Header -->
    <div class="glass-panel p-6 sm:p-8 rounded-2xl border border-slate-800 space-y-2">
      <div class="inline-flex items-center space-x-2 px-2.5 py-1 rounded-md bg-indigo-500/10 text-indigo-400 text-xs font-semibold">
        <Info class="w-3.5 h-3.5" />
        <span>Thông Tin Đồ Án</span>
      </div>
      <h1 class="text-2xl sm:text-3xl font-extrabold text-white">Về Đề Tài Thực Tập Tốt Nghiệp</h1>
      <p class="text-xs sm:text-sm text-slate-400">
        Giới thiệu bộ dữ liệu, quy trình huấn luyện Fine-tuning và công nghệ sử dụng trong hệ thống
      </p>
    </div>

    <!-- Tech Stack Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      
      <!-- Left: Dataset Info -->
      <div class="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <Database class="w-5 h-5 text-indigo-400" />
          <span>Bộ Dữ Liệu (Furniture Dataset)</span>
        </h3>
        <p class="text-xs text-slate-400 leading-relaxed">
          Bộ dữ liệu huấn luyện được thu thập từ Kaggle (Multi-Angle AI Training), gồm 10,364 ảnh nội thất 
          thuộc 6 lớp sản phẩm phổ biến, được làm sạch và phân chia theo tỷ lệ chuẩn 70% Train, 15% Validation, 15% Test.
        </p>

        <div class="space-y-2 pt-2">
          <div v-for="cls in classDetails" :key="cls.name" class="flex items-center justify-between text-xs p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
            <span class="font-bold text-white flex items-center gap-2">
              <span>{{ cls.emoji }}</span>
              <span>{{ cls.name }}</span>
            </span>
            <div class="flex items-center space-x-3 text-slate-400 font-mono">
              <span>Tổng: <strong class="text-white">{{ cls.total }}</strong></span>
              <span class="text-indigo-400">Train: {{ cls.train }}</span>
              <span class="text-purple-400">Val: {{ cls.val }}</span>
              <span class="text-emerald-400">Test: {{ cls.test }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Right: Preprocessing & Training Methodology -->
      <div class="space-y-6">
        
        <!-- Preprocessing Card -->
        <div class="glass-panel p-6 rounded-2xl border border-slate-800 space-y-3">
          <h3 class="text-lg font-bold text-white flex items-center gap-2">
            <Sliders class="w-5 h-5 text-purple-400" />
            <span>Tiền Xử Lý & Data Augmentation</span>
          </h3>
          <ul class="space-y-2 text-xs text-slate-300">
            <li class="flex items-center gap-2">
              <CheckCircle2 class="w-4 h-4 text-emerald-400 shrink-0" />
              <span><strong>Resize & Crop:</strong> Đưa ảnh về kích thước chuẩn 224 × 224 pixel.</span>
            </li>
            <li class="flex items-center gap-2">
              <CheckCircle2 class="w-4 h-4 text-emerald-400 shrink-0" />
              <span><strong>Normalize ImageNet:</strong> Mean=[0.485, 0.456, 0.406], Std=[0.229, 0.224, 0.225].</span>
            </li>
            <li class="flex items-center gap-2">
              <CheckCircle2 class="w-4 h-4 text-emerald-400 shrink-0" />
              <span><strong>Data Augmentation:</strong> Random Horizontal Flip, Rotation (15°), Color Jitter (Brightness/Contrast).</span>
            </li>
          </ul>
        </div>

        <!-- 2-Stage Training Strategy Card -->
        <div class="glass-panel p-6 rounded-2xl border border-slate-800 space-y-3">
          <h3 class="text-lg font-bold text-white flex items-center gap-2">
            <Cpu class="w-5 h-5 text-emerald-400" />
            <span>Quy Trình Fine-Tuning 2 Giai Đoạn</span>
          </h3>
          
          <div class="space-y-3 text-xs">
            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800">
              <h4 class="font-bold text-indigo-300">Giai đoạn 1 (10 Epochs - Freeze Backbone):</h4>
              <p class="text-slate-400 mt-1">Đóng băng toàn bộ các lớp backbone, chỉ huấn luyện lớp phân loại Fully Connected (FC Head) với Learning Rate = 1e-3 (Adam).</p>
            </div>

            <div class="p-3 rounded-xl bg-slate-900/80 border border-slate-800">
              <h4 class="font-bold text-purple-300">Giai đoạn 2 (20 Epochs - Unfreeze Full Model):</h4>
              <p class="text-slate-400 mt-1">Mở đóng băng toàn bộ mô hình, tiến hành fine-tune sâu tất cả các layer với Learning Rate nhỏ = 1e-5 để tối ưu hóa đặc trưng.</p>
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- Technologies Used Badge Section -->
    <div class="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
      <h3 class="text-lg font-bold text-white">Công Nghệ & Thư Viện Sử Dụng</h3>
      
      <div class="flex flex-wrap gap-3">
        <span v-for="t in techStack" :key="t.name" class="px-3.5 py-2 rounded-xl bg-slate-900 border border-slate-800 flex items-center space-x-2 text-xs font-semibold text-slate-200">
          <span class="text-base">{{ t.icon }}</span>
          <span>{{ t.name }}</span>
          <span class="text-[10px] text-indigo-400 font-mono">({{ t.role }})</span>
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
