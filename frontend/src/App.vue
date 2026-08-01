<template>
  <div class="min-h-screen bg-[#090d16] text-slate-100 flex flex-col font-sans">
    
    <!-- Navigation Bar -->
    <Navbar :activeTab="currentTab" @navigate="handleNavigate" />

    <!-- Main Dynamic Content -->
    <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
      <Transition name="fade" mode="out-in">
        <KeepAlive>
          <component :is="currentComponent" @navigate="handleNavigate" />
        </KeepAlive>
      </Transition>
    </main>

    <!-- Footer -->
    <Footer />

  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';
import Navbar from './components/Navbar.vue';
import Footer from './components/Footer.vue';
import HomeView from './views/HomeView.vue';
import PredictionView from './views/PredictionView.vue';
import ModelComparisonView from './views/ModelComparisonView.vue';
import AboutView from './views/AboutView.vue';

const currentTab = ref('home');

const currentComponent = computed(() => {
  switch (currentTab.value) {
    case 'predict':
      return PredictionView;
    case 'comparison':
      return ModelComparisonView;
    case 'about':
      return AboutView;
    case 'home':
    default:
      return HomeView;
  }
});

function handleNavigate(tab: string) {
  currentTab.value = tab;
  window.scrollTo({ top: 0, behavior: 'smooth' });
}
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.fade-enter-from {
  opacity: 0;
  transform: translateY(4px);
}

.fade-leave-to {
  opacity: 0;
  transform: translateY(-4px);
}
</style>
