<template>
  <nav class="sticky top-0 z-50 glass-panel border-b border-slate-800/80 backdrop-blur-xl bg-slate-950/80">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        
        <!-- Logo / Title -->
        <div class="flex items-center space-x-3 cursor-pointer" @click="$emit('navigate', 'home')">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 via-purple-600 to-pink-500 flex items-center justify-center shadow-lg shadow-indigo-500/20">
            <Armchair class="w-6 h-6 text-white" />
          </div>
          <div>
            <h1 class="font-bold text-lg leading-none gradient-text">Furniture AI</h1>
            <p class="text-[11px] text-slate-400 font-medium">Hệ thống phân loại nội thất Deep Learning</p>
          </div>
        </div>

        <!-- Navigation Tabs -->
        <div class="hidden md:flex items-center space-x-1 bg-slate-900/90 p-1.5 rounded-2xl border border-slate-800">
          <button
            v-for="item in navItems"
            :key="item.id"
            @click="$emit('navigate', item.id)"
            :class="[
              'px-4 py-2 rounded-xl text-sm font-semibold transition-all duration-200 flex items-center space-x-2',
              activeTab === item.id
                ? 'bg-gradient-to-r from-indigo-600 to-violet-600 text-white shadow-md shadow-indigo-500/25'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/50'
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
            class="px-4 py-2 rounded-xl text-xs sm:text-sm font-bold bg-indigo-500/10 text-indigo-400 border border-indigo-500/30 hover:bg-indigo-500/20 transition-all flex items-center space-x-2"
          >
            <Sparkles class="w-4 h-4" />
            <span>Thử Thử Nghiệm</span>
          </button>
        </div>

      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { Armchair, Home, ScanSearch, BarChart3, Info, Sparkles } from 'lucide-vue-next';

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
