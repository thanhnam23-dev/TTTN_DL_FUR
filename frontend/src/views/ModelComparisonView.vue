<template>
  <div class="space-y-8 py-4">
    
    <!-- Header -->
    <div class="glass-panel p-6 sm:p-8 rounded-2xl border border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div>
        <div class="inline-flex items-center space-x-2 px-2.5 py-1 rounded-md bg-indigo-500/10 text-indigo-400 text-xs font-semibold mb-2">
          <BarChart3 class="w-3.5 h-3.5" />
          <span>Thực Nghiệm Báo Cáo</span>
        </div>
        <h1 class="text-2xl sm:text-3xl font-extrabold text-white">So Sánh Đánh Giá Các Mô Hình</h1>
        <p class="text-xs sm:text-sm text-slate-400 mt-1">
          Bảng tổng hợp chỉ số Accuracy, Precision, Recall, F1-score, ROC-AUC và PR-AUC trên tập dữ liệu Test
        </p>
      </div>

      <div class="flex items-center space-x-2">
        <button
          @click="activeChartTab = 'metrics'"
          :class="[
            'px-4 py-2 rounded-xl text-xs font-bold transition-all',
            activeChartTab === 'metrics'
              ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-500/25'
              : 'bg-slate-900 text-slate-400 hover:text-slate-200 border border-slate-800'
          ]"
        >
          Biểu Đồ Chỉ Số
        </button>
        <button
          @click="activeChartTab = 'confusion'"
          :class="[
            'px-4 py-2 rounded-xl text-xs font-bold transition-all',
            activeChartTab === 'confusion'
              ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-500/25'
              : 'bg-slate-900 text-slate-400 hover:text-slate-200 border border-slate-800'
          ]"
        >
          Confusion Matrix
        </button>
      </div>
    </div>

    <!-- Recommendation Highlight Card -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div
        v-for="m in MOCK_MODEL_COMPARISON"
        :key="m.Model"
        :class="[
          'glass-panel p-5 rounded-2xl border transition-all duration-300 relative overflow-hidden',
          m.Model === 'EfficientNet-B0'
            ? 'border-emerald-500/50 bg-emerald-950/20 shadow-lg shadow-emerald-500/10'
            : 'border-slate-800'
        ]"
      >
        <div v-if="m.Model === 'EfficientNet-B0'" class="absolute top-0 right-0 bg-emerald-500 text-slate-950 text-[10px] font-extrabold px-3 py-1 rounded-bl-xl uppercase">
          Tốt Nhất (Best Acc)
        </div>
        <div v-if="m.Model === 'MobileNetV2'" class="absolute top-0 right-0 bg-indigo-500 text-white text-[10px] font-extrabold px-3 py-1 rounded-bl-xl uppercase">
          Nhanh Nhất (Lightweight)
        </div>

        <h3 class="text-lg font-bold text-white mb-3">{{ m.Model }}</h3>
        
        <div class="space-y-2 text-xs">
          <div class="flex justify-between py-1 border-b border-slate-800/80">
            <span class="text-slate-400">Accuracy (Độ chính xác)</span>
            <span class="font-bold text-white">{{ (m.Acc * 100).toFixed(2) }}%</span>
          </div>
          <div class="flex justify-between py-1 border-b border-slate-800/80">
            <span class="text-slate-400">Precision (W)</span>
            <span class="font-bold text-indigo-300">{{ (m.Prec * 100).toFixed(2) }}%</span>
          </div>
          <div class="flex justify-between py-1 border-b border-slate-800/80">
            <span class="text-slate-400">Recall (W)</span>
            <span class="font-bold text-purple-300">{{ (m.Recall * 100).toFixed(2) }}%</span>
          </div>
          <div class="flex justify-between py-1 border-b border-slate-800/80">
            <span class="text-slate-400">F1-Score</span>
            <span class="font-bold text-emerald-400">{{ (m.F1 * 100).toFixed(2) }}%</span>
          </div>
          <div class="flex justify-between py-1 border-b border-slate-800/80">
            <span class="text-slate-400">ROC-AUC</span>
            <span class="font-bold text-sky-400">{{ (m.RocAuc * 100).toFixed(2) }}%</span>
          </div>
          <div class="flex justify-between py-1">
            <span class="text-slate-400">PR-AUC</span>
            <span class="font-bold text-pink-400">{{ (m.PrAuc * 100).toFixed(2) }}%</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Detailed Interactive Comparison Table -->
    <div class="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
      <div class="flex items-center justify-between">
        <h3 class="text-lg font-bold text-white flex items-center gap-2">
          <Table class="w-5 h-5 text-indigo-400" />
          <span>Bảng So Sánh Chỉ Số Chi Tiết (Test Set)</span>
        </h3>
        <span class="text-xs text-slate-500 font-mono">logs/model_comparison.csv</span>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs text-slate-300 border-collapse">
          <thead>
            <tr class="bg-slate-900/90 text-slate-400 border-b border-slate-800 font-semibold">
              <th class="p-3.5">Mô Hình (Model)</th>
              <th class="p-3.5 text-center">Accuracy</th>
              <th class="p-3.5 text-center">Precision</th>
              <th class="p-3.5 text-center">Recall</th>
              <th class="p-3.5 text-center">F1-Score</th>
              <th class="p-3.5 text-center">ROC-AUC</th>
              <th class="p-3.5 text-center">PR-AUC</th>
              <th class="p-3.5 text-center">Đánh Giá Phù Hợp</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-800/80">
            <tr v-for="m in MOCK_MODEL_COMPARISON" :key="m.Model" class="hover:bg-slate-900/40 transition-colors">
              <td class="p-3.5 font-bold text-white flex items-center gap-2">
                <Cpu class="w-4 h-4 text-indigo-400" />
                <span>{{ m.Model }}</span>
              </td>
              <td class="p-3.5 text-center font-bold text-emerald-400">{{ (m.Acc * 100).toFixed(2) }}%</td>
              <td class="p-3.5 text-center font-semibold text-slate-200">{{ (m.Prec * 100).toFixed(2) }}%</td>
              <td class="p-3.5 text-center font-semibold text-slate-200">{{ (m.Recall * 100).toFixed(2) }}%</td>
              <td class="p-3.5 text-center font-bold text-purple-300">{{ (m.F1 * 100).toFixed(2) }}%</td>
              <td class="p-3.5 text-center font-semibold text-sky-400">{{ (m.RocAuc * 100).toFixed(2) }}%</td>
              <td class="p-3.5 text-center font-semibold text-pink-400">{{ (m.PrAuc * 100).toFixed(2) }}%</td>
              <td class="p-3.5 text-center">
                <span v-if="m.Model === 'EfficientNet-B0'" class="px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 text-[11px] font-bold">
                  Khuyên dùng chính
                </span>
                <span v-else-if="m.Model === 'MobileNetV2'" class="px-2.5 py-1 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 text-[11px] font-bold">
                  Nhẹ & Nhanh
                </span>
                <span v-else class="px-2.5 py-1 rounded-full bg-slate-800 text-slate-300 text-[11px]">
                  CNN Kinh điển
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Visual Chart Viewers -->
    <div v-if="activeChartTab === 'metrics'" class="glass-panel p-6 rounded-2xl border border-slate-800 space-y-4">
      <div class="flex items-center justify-between">
        <h3 class="text-base font-bold text-white">Biểu Đồ Trực Quan So Sánh 3 Mô Hình</h3>
        <div class="flex items-center space-x-3 text-xs text-slate-400">
          <span class="flex items-center gap-1"><span class="w-3 h-3 rounded bg-indigo-500"></span> MobileNetV2</span>
          <span class="flex items-center gap-1"><span class="w-3 h-3 rounded bg-rose-500"></span> ResNet18</span>
          <span class="flex items-center gap-1"><span class="w-3 h-3 rounded bg-emerald-500"></span> EfficientNet-B0</span>
        </div>
      </div>

      <div class="h-72 w-full pt-4">
        <Bar :data="chartData" :options="chartOptions" />
      </div>
    </div>

    <!-- Confusion Matrix Tab -->
    <div v-else-if="activeChartTab === 'confusion'" class="glass-panel p-6 rounded-2xl border border-slate-800 space-y-6">
      <div class="flex items-center justify-between">
        <h3 class="text-base font-bold text-white">Ma Trận Nhầm Lẫn (Confusion Matrix)</h3>
        <p class="text-xs text-slate-400">Thống kê số lượng dự đoán đúng/sai giữa các lớp</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div v-for="m in ['MobileNetV2', 'ResNet18', 'EfficientNet-B0']" :key="m" class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-3">
          <h4 class="text-xs font-bold text-center text-indigo-400">Matrix - {{ m }}</h4>
          
          <div class="grid grid-cols-6 gap-1 text-[9px] font-mono text-center">
            <div v-for="n in 36" :key="n" class="p-1.5 rounded" :class="n % 7 === 1 ? 'bg-indigo-600/60 text-white font-bold' : 'bg-slate-900 text-slate-500'">
              {{ n % 7 === 1 ? 400 + (n*3) : (n % 3) }}
            </div>
          </div>

          <div class="text-[10px] text-center text-slate-500">
            Trục tung: True Label | Trục hoành: Predicted
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { BarChart3, Cpu, Table } from 'lucide-vue-next';
import { MOCK_MODEL_COMPARISON } from '../services/api';
import { Bar } from 'vue-chartjs';
import {
  Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale
} from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

const activeChartTab = ref<'metrics' | 'confusion'>('metrics');

const chartData = {
  labels: ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC', 'PR-AUC'],
  datasets: [
    {
      label: 'MobileNetV2',
      backgroundColor: '#6366f1',
      data: [92.40, 92.55, 92.40, 92.42, 98.92, 97.85]
    },
    {
      label: 'ResNet18',
      backgroundColor: '#f43f5e',
      data: [94.15, 94.28, 94.15, 94.18, 99.31, 98.42]
    },
    {
      label: 'EfficientNet-B0',
      backgroundColor: '#10b981',
      data: [95.82, 95.90, 95.82, 95.84, 99.64, 99.10]
    }
  ]
};

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      min: 80,
      max: 100,
      grid: { color: 'rgba(255, 255, 255, 0.05)' },
      ticks: { color: '#94a3b8' }
    },
    x: {
      grid: { display: false },
      ticks: { color: '#94a3b8' }
    }
  },
  plugins: {
    legend: { display: false }
  }
};
</script>
