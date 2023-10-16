<template>
  <div class="home_body">
    <div class="home_header">
      <side-menu></side-menu>
    </div>
    <div class="user_info">
      <span class="user_name">{{ store.getters.user.user_name }}</span>
      <el-avatar
        src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
      ></el-avatar>
    </div>
    <div class="home_content">
      <router-view></router-view>
    </div>
  </div>
</template>
<script setup>
import sideMenu from '@/layout/sideMenu.vue'
import { useStore } from 'vuex'
import { onMounted } from 'vue'

onMounted(() => {
  // console.log('home', store.getters.user, store.getters.user)
})

const store = useStore()
</script>
<style scoped>
.home_body {
  min-width: 480px;
}
.home_body .home_header {
  min-width: 480px;
}
.home_body .user_info {
  position: absolute;
  top: 0;
  right: 0;
  width: 80px;
}

.user_info .el-avatar {
  position: relative;
  top: 10px;
  right: 0;
}

.user_info .user_name {
  display: inline-block;
  transform: translateY(-5px) translateX(-10px);
}

@media (max-width: 480px) {
  .home_header {
    position: absolute;
    bottom: 0;
  }
  .home_body {
    min-width: 100%;
  }
  .home_body .user_info {
    display: none;
  }
}
</style>