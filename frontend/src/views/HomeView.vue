<template>
  <div class="space-y-8 py-4">
    
    <!-- Hero Section with Bright Indigo Tint -->
    <section class="rounded-2xl p-8 sm:p-12 border border-indigo-200 bg-indigo-50/70 shadow-xs">
      <div class="max-w-3xl space-y-5">
        <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-md bg-white border border-indigo-200 text-indigo-700 text-xs font-bold shadow-xs">
          <GraduationCap class="w-4 h-4 text-indigo-600" />
          <span>Báo Cáo Đồ Án Thực Tập Tốt Nghiệp</span>
        </div>

        <h1 class="text-3xl sm:text-4xl font-black text-slate-900 leading-tight tracking-tight">
          Hệ Thống Phân Loại Sản Phẩm Nội Thất <br />
          Sử Dụng Deep Learning
        </h1>

        <p class="text-slate-700 text-sm sm:text-base leading-relaxed font-medium">
          Ứng dụng thị giác máy tính dựa trên kỹ thuật Transfer Learning 
          (<strong class="text-indigo-700 font-bold">MobileNetV2</strong>, <strong class="text-sky-700 font-bold">ResNet18</strong>, <strong class="text-emerald-700 font-bold">EfficientNet-B0</strong>) tự động phân loại 6 dòng sản phẩm nội thất từ hình ảnh 
          kèm giải thích bản đồ vùng chú ý <strong class="text-purple-700 font-bold">Grad-CAM</strong>.
        </p>

        <div class="pt-2 flex flex-wrap gap-3 items-center">
          <button
            @click="$emit('navigate', 'predict')"
            class="px-5 py-2.5 rounded-xl font-extrabold text-xs sm:text-sm bg-indigo-600 text-white hover:bg-indigo-700 shadow-sm transition-all flex items-center space-x-2"
          >
            <ScanSearch class="w-4 h-4" />
            <span>Thử Nhận Diện Ngay</span>
          </button>

          <button
            @click="$emit('navigate', 'comparison')"
            class="px-5 py-2.5 rounded-xl font-extrabold text-xs sm:text-sm bg-white text-slate-800 border border-slate-300 hover:bg-slate-50 transition-all flex items-center space-x-2 shadow-xs"
          >
            <BarChart3 class="w-4 h-4 text-slate-600" />
            <span>Xem Bảng So Sánh Mô Hình</span>
          </button>
        </div>
      </div>
    </section>

    <!-- Key Metrics Highlight (Distinct Bright Pastel Background Cards) -->
    <section class="grid grid-cols-2 lg:grid-cols-4 gap-4">
      
      <div class="p-5 rounded-2xl border border-indigo-200 bg-indigo-50/80 shadow-xs">
        <div class="flex items-center justify-between">
          <Database class="w-6 h-6 text-indigo-600" />
          <span class="text-[11px] font-bold text-indigo-800 bg-white px-2 py-0.5 rounded border border-indigo-200 shadow-xs">
            Chuẩn hoá
          </span>
        </div>
        <div class="mt-3">
          <h4 class="text-xl sm:text-2xl font-black text-slate-900">6 Lớp</h4>
          <p class="text-xs text-indigo-900 mt-0.5 font-bold">Số lớp nội thất</p>
        </div>
      </div>

      <div class="p-5 rounded-2xl border border-sky-200 bg-sky-50/80 shadow-xs">
        <div class="flex items-center justify-between">
          <Image class="w-6 h-6 text-sky-600" />
          <span class="text-[11px] font-bold text-sky-800 bg-white px-2 py-0.5 rounded border border-sky-200 shadow-xs">
            70/15/15
          </span>
        </div>
        <div class="mt-3">
          <h4 class="text-xl sm:text-2xl font-black text-slate-900">10,364</h4>
          <p class="text-xs text-sky-900 mt-0.5 font-bold">Tổng số ảnh</p>
        </div>
      </div>

      <div class="p-5 rounded-2xl border border-emerald-200 bg-emerald-50/80 shadow-xs">
        <div class="flex items-center justify-between">
          <CheckCircle2 class="w-6 h-6 text-emerald-600" />
          <span class="text-[11px] font-bold text-emerald-800 bg-white px-2 py-0.5 rounded border border-emerald-200 shadow-xs">
            EfficientNet-B0
          </span>
        </div>
        <div class="mt-3">
          <h4 class="text-xl sm:text-2xl font-black text-slate-900">>95.8%</h4>
          <p class="text-xs text-emerald-900 mt-0.5 font-bold">Độ chính xác cao nhất</p>
        </div>
      </div>

      <div class="p-5 rounded-2xl border border-amber-200 bg-amber-50/80 shadow-xs">
        <div class="flex items-center justify-between">
          <Zap class="w-6 h-6 text-amber-600" />
          <span class="text-[11px] font-bold text-amber-800 bg-white px-2 py-0.5 rounded border border-amber-200 shadow-xs">
            FastAPI
          </span>
        </div>
        <div class="mt-3">
          <h4 class="text-xl sm:text-2xl font-black text-slate-900">~24 ms</h4>
          <p class="text-xs text-amber-900 mt-0.5 font-bold">Tốc độ phản hồi API</p>
        </div>
      </div>

    </section>

    <!-- Architecture & Pipeline Flow -->
    <section class="space-y-4">
      <div>
        <h2 class="text-xl font-extrabold text-slate-900">Quy Trình Hoạt Động Của Hệ Thống</h2>
        <p class="text-slate-600 text-xs mt-0.5 font-medium">Các bước xử lý từ tải ảnh lên đến phân loại và xuất bản đồ Grad-CAM</p>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
        <div v-for="(step, idx) in pipelineSteps" :key="idx" :class="['p-5 rounded-xl border shadow-xs', step.bgCard]">
          <div :class="['w-8 h-8 rounded-lg flex items-center justify-center mb-3 text-xs font-black text-white shadow-xs', step.badgeBg]">
            0{{ idx + 1 }}
          </div>
          <h3 class="text-sm font-bold text-slate-900 mb-1">{{ step.title }}</h3>
          <p class="text-xs text-slate-700 leading-relaxed font-medium">{{ step.desc }}</p>
        </div>
      </div>
    </section>

    <!-- Target Classes Overview (Multi-Color Cards) -->
    <section class="p-6 rounded-2xl border border-purple-200 bg-purple-50/50 space-y-4 shadow-xs">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-lg font-extrabold text-slate-900">6 Lớp Sản Phẩm Nội Thất</h2>
          <p class="text-xs text-slate-600 mt-0.5 font-medium">Furniture Dataset (Multi-Angle AI Training)</p>
        </div>
        <span class="text-xs px-3 py-1 rounded bg-white text-purple-700 font-extrabold border border-purple-200 shadow-xs">
          10,364 Ảnh
        </span>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
        <div v-for="c in categories" :key="c.id" :class="['p-3.5 rounded-xl border text-center shadow-xs transition-all hover:scale-105', c.bgClass]">
          <div class="text-2xl mb-1">{{ c.emoji }}</div>
          <h4 class="text-xs font-bold text-slate-900">{{ c.name }}</h4>
          <p class="text-[11px] text-slate-700 font-bold mt-0.5">{{ c.count }} ảnh</p>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup lang="ts">
import { GraduationCap, ScanSearch, BarChart3, Image, CheckCircle2, Zap, Database } from 'lucide-vue-next';

defineEmits(['navigate']);

const pipelineSteps = [
  { title: 'Tải Ảnh Lên', desc: 'Chọn ảnh nội thất (JPG, PNG) cần phân loại từ thiết bị.', bgCard: 'bg-indigo-50 border-indigo-200', badgeBg: 'bg-indigo-600' },
  { title: 'Tiền Xử Lý', desc: 'Resize 224x224, Chuẩn hoá ImageNet & trích xuất đặc trưng.', bgCard: 'bg-sky-50 border-sky-200', badgeBg: 'bg-sky-600' },
  { title: 'Suy Luận Mô Hình', desc: 'Chạy suy luận qua MobileNetV2, ResNet18 hoặc EfficientNet-B0.', bgCard: 'bg-purple-50 border-purple-200', badgeBg: 'bg-purple-600' },
  { title: 'Kết Quả & Grad-CAM', desc: 'Hiển thị Top-3 dự đoán, Confidence %, thời gian suy luận và vùng chú ý Grad-CAM.', bgCard: 'bg-emerald-50 border-emerald-200', badgeBg: 'bg-emerald-600' },
];

const categories = [
  { id: 'bar_stool', name: 'Ghế Quầy Bar', count: '1,665', emoji: '🪑', bgClass: 'bg-indigo-50 border-indigo-200' },
  { id: 'bed', name: 'Giường Ngủ', count: '2,862', emoji: '🛏️', bgClass: 'bg-sky-50 border-sky-200' },
  { id: 'chair', name: 'Ghế Tựa', count: '980', emoji: '🛋️', bgClass: 'bg-purple-50 border-purple-200' },
  { id: 'coffee_table', name: 'Bàn Trà', count: '528', emoji: '☕', bgClass: 'bg-amber-50 border-amber-200' },
  { id: 'dining_table', name: 'Bàn Ăn', count: '2,355', emoji: '🍽️', bgClass: 'bg-emerald-50 border-emerald-200' },
  { id: 'dresser', name: 'Tủ Trang Điểm', count: '1,974', emoji: '🗄️', bgClass: 'bg-rose-50 border-rose-200' },
];
</script>
