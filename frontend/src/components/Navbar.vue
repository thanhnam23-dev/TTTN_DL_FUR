<template>
  <nav class="sticky top-0 z-50 bg-white border-b border-slate-300 shadow-xs">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        
        <!-- Logo / Title -->
        <div class="flex items-center space-x-3 cursor-pointer" @click="$emit('navigate', 'home')">
          <div class="w-10 h-10 rounded-xl bg-indigo-600 flex items-center justify-center text-white shadow-sm">
            <Armchair class="w-5 h-5" />
          </div>
          <div>
            <h1 class="font-extrabold text-base text-slate-900 leading-none">Furniture AI</h1>
            <p class="text-[11px] text-slate-600 font-semibold mt-0.5">Phân loại nội thất Deep Learning</p>
          </div>
        </div>

        <!-- Navigation Tabs -->
        <div class="hidden md:flex items-center space-x-1 bg-slate-100 p-1.5 rounded-xl border border-slate-300">
          <button
            v-for="item in navItems"
            :key="item.id"
            @click="$emit('navigate', item.id)"
            :class="[
              'px-4 py-1.5 rounded-lg text-xs font-extrabold transition-all duration-150 flex items-center space-x-2',
              activeTab === item.id
                ? 'bg-white text-indigo-700 shadow-xs border border-slate-300'
                : 'text-slate-700 hover:text-slate-900 hover:bg-slate-200/80'
            ]"
          >
            <component :is="item.icon" class="w-4 h-4" />
            <span>{{ item.label }}</span>
          </button>
        </div>

        <!-- Right Quick Action -->
        <div class="flex items-center space-x-3">
          <button
            @click="$emit('navigate', 'predict')"
            class="px-4 py-2 rounded-xl text-xs font-bold bg-indigo-600 text-white shadow-sm hover:bg-indigo-700 transition-all flex items-center space-x-1.5"
          >
            <ScanSearch class="w-4 h-4" />
            <span>Thử Nhận Diện</span>
          </button>
        </div>

      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { Armchair, Home, ScanSearch, BarChart3, Info } from 'lucide-vue-next';

defineProps<{
  activeTab: string;
}>();

defineEmits(['navigate']);

const navItems = [
  { id: 'home', label: 'Trang Chủ', icon: Home },
  { id: 'predict', label: 'Dự Đoán & Grad-CAM', icon: ScanSearch },
  { id: 'comparison', label: 'So Sánh Mô Hình', icon: BarChart3 },
  { id: 'about', label: 'Về Dự Án', icon: Info },
];
</script>
