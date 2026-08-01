<template>
  <div class="space-y-12 py-6">
    
    <!-- Hero Section -->
    <section class="relative overflow-hidden rounded-3xl glass-panel p-8 sm:p-12 lg:p-16 border border-slate-800/90 shadow-2xl">
      <!-- Glow background blur elements -->
      <div class="absolute -top-24 -left-24 w-96 h-96 bg-indigo-600/20 rounded-full blur-3xl animate-glow"></div>
      <div class="absolute -bottom-24 -right-24 w-96 h-96 bg-purple-600/20 rounded-full blur-3xl animate-glow" style="animation-delay: 2s;"></div>

      <div class="relative z-10 max-w-3xl space-y-6">
        <div class="inline-flex items-center space-x-2 px-3 py-1.5 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 text-xs font-semibold">
          <GraduationCap class="w-4 h-4" />
          <span>Báo Cáo Đồ Án Thực Tập Tốt Nghiệp</span>
        </div>

        <h1 class="text-3xl sm:text-5xl font-black text-white leading-tight tracking-tight">
          Hệ Thống Phân Loại <br />
          <span class="gradient-text">Sản Phẩm Nội Thất</span> <br />
          Sử Dụng Deep Learning
        </h1>

        <p class="text-slate-300 text-base sm:text-lg leading-relaxed">
          Ứng dụng thị giác máy tính với kiến trúc Transfer Learning 
          (<strong class="text-indigo-400">MobileNetV2</strong>, <strong class="text-indigo-400">ResNet18</strong>, <strong class="text-indigo-400">EfficientNet-B0</strong>) 
          giúp tự động phân loại 6 loại nội thất từ ảnh với độ chính xác trên 95% và giải thích trực quan bằng <strong class="text-purple-400">Grad-CAM</strong>.
        </p>

        <div class="pt-4 flex flex-wrap gap-4 items-center">
          <button
            @click="$emit('navigate', 'predict')"
            class="px-6 py-3.5 rounded-2xl font-bold text-sm bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 text-white shadow-lg shadow-indigo-500/30 hover:scale-105 transition-all duration-200 flex items-center space-x-2"
          >
            <ScanSearch class="w-5 h-5" />
            <span>Thử Nhận Diện Ngay</span>
          </button>

          <button
            @click="$emit('navigate', 'comparison')"
            class="px-6 py-3.5 rounded-2xl font-bold text-sm bg-slate-800/80 text-slate-200 border border-slate-700/80 hover:bg-slate-700/80 hover:border-indigo-500/50 transition-all duration-200 flex items-center space-x-2"
          >
            <BarChart3 class="w-5 h-5 text-indigo-400" />
            <span>Xem Bảng So Sánh Mô Hình</span>
          </button>
        </div>
      </div>
    </section>

    <!-- Key Metrics Highlight -->
    <section class="grid grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
      <div v-for="(stat, idx) in stats" :key="idx" class="glass-panel glass-panel-hover p-6 rounded-2xl border border-slate-800/80">
        <div class="flex items-center justify-between">
          <component :is="stat.icon" class="w-8 h-8 text-indigo-400" />
          <span class="text-xs font-semibold text-emerald-400 bg-emerald-500/10 px-2 py-1 rounded-lg border border-emerald-500/20">
            {{ stat.badge }}
          </span>
        </div>
        <div class="mt-4">
          <h4 class="text-2xl sm:text-3xl font-extrabold text-white">{{ stat.value }}</h4>
          <p class="text-xs sm:text-sm text-slate-400 mt-1 font-medium">{{ stat.label }}</p>
        </div>
      </div>
    </section>

    <!-- Architecture & Pipeline Flow -->
    <section class="space-y-6">
      <div class="text-center max-w-2xl mx-auto space-y-2">
        <h2 class="text-2xl sm:text-3xl font-bold text-white">Quy Trình Hoạt Động Của Hệ Thống</h2>
        <p class="text-slate-400 text-sm">Từ hình ảnh tải lên đến kết quả phân loại Top-3 và bản đồ kích hoạt Grad-CAM</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div v-for="(step, idx) in pipelineSteps" :key="idx" class="glass-panel p-6 rounded-2xl border border-slate-800/80 relative overflow-hidden group">
          <div class="absolute -right-4 -bottom-4 text-slate-800/40 text-7xl font-black select-none">
            {{ idx + 1 }}
          </div>
          <div class="w-10 h-10 rounded-xl bg-indigo-500/10 border border-indigo-500/30 flex items-center justify-center text-indigo-400 mb-4 group-hover:scale-110 transition-transform">
            <component :is="step.icon" class="w-5 h-5" />
          </div>
          <h3 class="text-base font-bold text-white mb-2">{{ step.title }}</h3>
          <p class="text-xs text-slate-400 leading-relaxed">{{ step.desc }}</p>
        </div>
      </div>
    </section>

    <!-- Target Classes Overview -->
    <section class="glass-panel p-8 rounded-3xl border border-slate-800 space-y-6">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-xl sm:text-2xl font-bold text-white">6 Lớp Sản Phẩm Nội Thất</h2>
          <p class="text-xs sm:text-sm text-slate-400 mt-1">Được làm sạch & phân chia chuẩn từ Furniture Dataset (Multi-Angle)</p>
        </div>
        <span class="text-xs px-3 py-1.5 rounded-xl bg-indigo-500/10 text-indigo-400 font-semibold border border-indigo-500/20">
          10,364 Ảnh
        </span>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
        <div v-for="c in categories" :key="c.id" class="bg-slate-900/60 p-4 rounded-xl border border-slate-800 text-center hover:border-indigo-500/50 transition-all">
          <div class="text-2xl mb-2">{{ c.emoji }}</div>
          <h4 class="text-xs font-bold text-slate-200">{{ c.name }}</h4>
          <p class="text-[11px] text-indigo-400 font-medium mt-1">{{ c.count }} ảnh</p>
        </div>
      </div>
    </section>

  </div>
</template>

<script setup lang="ts">
import { GraduationCap, ScanSearch, BarChart3, Image, Cpu, Activity, Eye, Database, CheckCircle2, Zap } from 'lucide-vue-next';

defineEmits(['navigate']);

const stats = [
  { label: 'Số lớp nội thất', value: '6 Lớp', badge: 'Chuẩn hoá', icon: Database },
  { label: 'Tổng số ảnh', value: '10,364', badge: '70/15/15', icon: Image },
  { label: 'Độ chính xác tối đa', value: '>95.8%', badge: 'EfficientNet-B0', icon: CheckCircle2 },
  { label: 'Tốc độ phản hồi API', value: '~24 ms', badge: 'FastAPI', icon: Zap },
];

const pipelineSteps = [
  { icon: Image, title: '1. Tải Ảnh Lên', desc: 'Người dùng chọn ảnh nội thất (JPG, PNG) cần phân loại từ thiết bị.' },
  { icon: Cpu, title: '2. Tiền Xử Lý', desc: 'Ảnh được Resize 224x224, Chuẩn hoá ImageNet & trích xuất đặc trưng.' },
  { icon: Activity, title: '3. Mô Hình Suy Luận', desc: 'Chạy suy luận qua MobileNetV2, ResNet18 hoặc EfficientNet-B0.' },
  { icon: Eye, title: '4. Kết Quả & Grad-CAM', desc: 'Hiển thị Top-3 dự đoán, Confidence %, thời gian suy luận và vùng chú ý Grad-CAM.' },
];

const categories = [
  { id: 'bar_stool', name: 'Ghế Quầy Bar', count: '1,665', emoji: '🪑' },
  { id: 'bed', name: 'Giường Ngủ', count: '2,862', emoji: '🛏️' },
  { id: 'chair', name: 'Ghế Tựa', count: '980', emoji: '🛋️' },
  { id: 'coffee_table', name: 'Bàn Trà', count: '528', emoji: '☕' },
  { id: 'dining_table', name: 'Bàn Ăn', count: '2,355', emoji: '🍽️' },
  { id: 'dresser', name: 'Tủ Trang Điểm', count: '1,974', emoji: '🗄️' },
];
</script>
