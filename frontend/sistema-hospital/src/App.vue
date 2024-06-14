<script setup>
import { RouterLink, RouterView } from 'vue-router'
import foot from './components/Pie-Pagina.vue'
</script>

<template>

  <RouterView />
  <foot />


</template>

<style>
footer{
  position:fixed;
  bottom: 0;
  width: 100%;
}
</style>

