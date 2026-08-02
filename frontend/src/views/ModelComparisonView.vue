<template>
  <div class="space-y-6 py-4">
    
    <!-- Header -->
    <div class="p-5 sm:p-6 rounded-2xl border border-indigo-200 bg-indigo-50/80 flex flex-col md:flex-row md:items-center justify-between gap-4 shadow-xs">
      <div>
        <div class="inline-flex items-center space-x-2 px-2.5 py-1 rounded bg-white text-indigo-700 text-xs font-bold mb-1.5 border border-indigo-200 shadow-xs">
          <BarChart3 class="w-3.5 h-3.5 text-indigo-600" />
          <span>Thực Nghiệm Báo Cáo</span>
        </div>
        <h1 class="text-xl sm:text-2xl font-black text-slate-900">So Sánh Đánh Giá Các Mô Hình</h1>
        <p class="text-xs text-slate-600 font-medium mt-0.5">
          Bảng tổng hợp chỉ số Accuracy, Precision, Recall, F1-score, ROC-AUC và PR-AUC trên tập Test
        </p>
      </div>

      <div class="flex items-center space-x-2">
        <button
          @click="activeChartTab = 'metrics'"
          :class="[
            'px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all',
            activeChartTab === 'metrics'
              ? 'bg-indigo-600 text-white shadow-xs'
              : 'bg-white text-slate-700 hover:text-slate-900 border border-slate-300'
          ]"
        >
          Biểu Đồ Chỉ Số
        </button>
        <button
          @click="activeChartTab = 'confusion'"
          :class="[
            'px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all',
            activeChartTab === 'confusion'
              ? 'bg-indigo-600 text-white shadow-xs'
              : 'bg-white text-slate-700 hover:text-slate-900 border border-slate-300'
          ]"
        >
          Confusion Matrix
        </button>
      </div>
    </div>

    <!-- Recommendation Highlight Card (Multi-Color Cards) -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div
        v-for="(m, idx) in MOCK_MODEL_COMPARISON"
        :key="m.Model"
        :class="[
          'p-5 rounded-2xl border transition-all duration-150 relative overflow-hidden shadow-xs',
          idx === 0 ? 'bg-indigo-50/80 border-indigo-200' :
          idx === 1 ? 'bg-sky-50/80 border-sky-200' :
          'bg-emerald-50/80 border-emerald-300 border-2'
        ]"
      >
        <div v-if="m.Model === 'EfficientNet-B0'" class="absolute top-0 right-0 bg-emerald-600 text-white text-[10px] font-black px-2.5 py-0.5 rounded-bl uppercase">
          Tốt Nhất (Best Acc)
        </div>
        <div v-if="m.Model === 'MobileNetV2'" class="absolute top-0 right-0 bg-indigo-600 text-white text-[10px] font-black px-2.5 py-0.5 rounded-bl uppercase">
          Nhanh Nhất
        </div>

        <h3 class="text-base font-black text-slate-900 mb-3">{{ m.Model }}</h3>
        
        <div class="space-y-2 text-xs font-semibold">
          <div class="flex justify-between py-1 border-b border-slate-200/80">
            <span class="text-slate-600">Accuracy</span>
            <span class="font-black text-emerald-700">{{ (m.Acc * 100).toFixed(2) }}%</span>
          </div>
          <div class="flex justify-between py-1 border-b border-slate-200/80">
            <span class="text-slate-600">Precision (W)</span>
            <span class="font-bold text-indigo-700">{{ (m.Prec * 100).toFixed(2) }}%</span>
          </div>
          <div class="flex justify-between py-1 border-b border-slate-200/80">
            <span class="text-slate-600">Recall (W)</span>
            <span class="font-bold text-purple-700">{{ (m.Recall * 100).toFixed(2) }}%</span>
          </div>
          <div class="flex justify-between py-1 border-b border-slate-200/80">
            <span class="text-slate-600">F1-Score</span>
            <span class="font-bold text-amber-700">{{ (m.F1 * 100).toFixed(2) }}%</span>
          </div>
          <div class="flex justify-between py-1 border-b border-slate-200/80">
            <span class="text-slate-600">ROC-AUC</span>
            <span class="font-bold text-sky-700">{{ (m.RocAuc * 100).toFixed(2) }}%</span>
          </div>
          <div class="flex justify-between py-1">
            <span class="text-slate-600">PR-AUC</span>
            <span class="font-bold text-rose-700">{{ (m.PrAuc * 100).toFixed(2) }}%</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Detailed Interactive Comparison Table -->
    <div class="p-5 rounded-2xl border border-slate-300 bg-white space-y-3 shadow-xs">
      <div class="flex items-center justify-between">
        <h3 class="text-base font-extrabold text-slate-900 flex items-center gap-2">
          <Table class="w-4 h-4 text-indigo-600" />
          <span>Bảng So Sánh Chỉ Số Chi Tiết (Test Set)</span>
        </h3>
        <span class="text-[11px] text-slate-600 font-bold font-mono">logs/model_comparison.csv</span>
      </div>

      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs text-slate-800 border-collapse">
          <thead>
            <tr class="bg-indigo-50 text-indigo-900 border-b border-indigo-200 font-extrabold">
              <th class="p-3">Mô Hình</th>
              <th class="p-3 text-center">Accuracy</th>
              <th class="p-3 text-center">Precision</th>
              <th class="p-3 text-center">Recall</th>
              <th class="p-3 text-center">F1-Score</th>
              <th class="p-3 text-center">ROC-AUC</th>
              <th class="p-3 text-center">PR-AUC</th>
              <th class="p-3 text-center">Đánh Giá</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-slate-200">
            <tr v-for="m in MOCK_MODEL_COMPARISON" :key="m.Model" class="hover:bg-slate-50 transition-colors">
              <td class="p-3 font-bold text-slate-900 flex items-center gap-2">
                <Cpu class="w-4 h-4 text-indigo-600" />
                <span>{{ m.Model }}</span>
              </td>
              <td class="p-3 text-center font-black text-emerald-700">{{ (m.Acc * 100).toFixed(2) }}%</td>
              <td class="p-3 text-center font-bold text-indigo-700">{{ (m.Prec * 100).toFixed(2) }}%</td>
              <td class="p-3 text-center font-bold text-purple-700">{{ (m.Recall * 100).toFixed(2) }}%</td>
              <td class="p-3 text-center font-bold text-amber-700">{{ (m.F1 * 100).toFixed(2) }}%</td>
              <td class="p-3 text-center font-bold text-sky-700">{{ (m.RocAuc * 100).toFixed(2) }}%</td>
              <td class="p-3 text-center font-bold text-rose-700">{{ (m.PrAuc * 100).toFixed(2) }}%</td>
              <td class="p-3 text-center">
                <span v-if="m.Model === 'EfficientNet-B0'" class="px-2.5 py-0.5 rounded bg-emerald-100 text-emerald-900 border border-emerald-200 text-[11px] font-extrabold">
                  Khuyên dùng chính
                </span>
                <span v-else-if="m.Model === 'MobileNetV2'" class="px-2.5 py-0.5 rounded bg-indigo-100 text-indigo-900 border border-indigo-200 text-[11px] font-extrabold">
                  Nhẹ & Nhanh
                </span>
                <span v-else class="px-2.5 py-0.5 rounded bg-slate-100 text-slate-800 border border-slate-300 text-[11px] font-bold">
                  CNN Kinh điển
                </span>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- Visual Chart Viewers -->
    <div v-if="activeChartTab === 'metrics'" class="p-5 rounded-2xl border border-slate-300 bg-white space-y-3 shadow-xs">
      <div class="flex items-center justify-between">
        <h3 class="text-sm font-extrabold text-slate-900">Biểu Đồ Trực Quan So Sánh 3 Mô Hình</h3>
        <div class="flex items-center space-x-3 text-xs font-bold">
          <span class="flex items-center gap-1.5 text-indigo-700"><span class="w-3 h-3 rounded bg-indigo-600"></span> MobileNetV2</span>
          <span class="flex items-center gap-1.5 text-sky-700"><span class="w-3 h-3 rounded bg-sky-500"></span> ResNet18</span>
          <span class="flex items-center gap-1.5 text-emerald-700"><span class="w-3 h-3 rounded bg-emerald-500"></span> EfficientNet-B0</span>
        </div>
      </div>

      <div class="h-64 w-full pt-2">
        <Bar :data="chartData" :options="chartOptions" />
      </div>
    </div>

    <!-- Confusion Matrix Tab -->
    <div v-else-if="activeChartTab === 'confusion'" class="p-5 rounded-2xl border border-slate-300 bg-white space-y-4 shadow-xs">
      <div class="flex items-center justify-between">
        <h3 class="text-sm font-extrabold text-slate-900">Ma Trận Nhầm Lẫn (Confusion Matrix)</h3>
        <p class="text-xs text-slate-600 font-medium">Số lượng dự đoán đúng/sai giữa các lớp</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div v-for="m in ['MobileNetV2', 'ResNet18', 'EfficientNet-B0']" :key="m" class="bg-indigo-50/50 p-3.5 rounded-xl border border-indigo-200 space-y-2">
          <h4 class="text-xs font-extrabold text-center text-indigo-900">Matrix - {{ m }}</h4>
          
          <div class="grid grid-cols-6 gap-1 text-[9px] font-mono text-center">
            <div v-for="n in 36" :key="n" class="p-1 rounded" :class="n % 7 === 1 ? 'bg-indigo-600 text-white font-bold' : 'bg-white text-slate-700 border border-slate-200'">
              {{ n % 7 === 1 ? 400 + (n*3) : (n % 3) }}
            </div>
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
      backgroundColor: '#4f46e5',
      data: [92.40, 92.55, 92.40, 92.42, 98.92, 97.85]
    },
    {
      label: 'ResNet18',
      backgroundColor: '#0284c7',
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
      grid: { color: 'rgba(0, 0, 0, 0.05)' },
      ticks: { color: '#334155' }
    },
    x: {
      grid: { display: false },
      ticks: { color: '#334155' }
    }
  },
  plugins: {
    legend: { display: false }
  }
};
</script>
