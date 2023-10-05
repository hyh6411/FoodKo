<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <side-menu></side-menu>
      </el-header>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>
<script setup>
import sideMenu from '@/layout/sideMenu.vue'

</script>
<style lang="scss" scoped>
</style>