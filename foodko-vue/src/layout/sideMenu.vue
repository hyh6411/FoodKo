<template>
  <ul class="menu_content">
    <router-link to="/">
      <li :class="{ 'menu_item': true, 'active': activeIndex === 'index' }" @click="handleSelect('index')">
        总览
      </li>
    </router-link>
    <router-link to="/database">
      <li :class="{ 'menu_item': true, 'active': activeIndex === 'database' }" @click="handleSelect('database')">
        数据库
      </li>
    </router-link>
    <router-link to="/charts">
      <li :class="{ 'menu_item': true, 'active': activeIndex === 'charts' }" @click="handleSelect('charts')">
        图表
      </li>
    </router-link>
    <router-link to="/settings">
      <li :class="{ 'menu_item': true, 'active': activeIndex === 'settings' }" @click="handleSelect('settings')">
        设置
      </li>
    </router-link>
  </ul>
    <!-- <el-menu-item index="index">
      <router-link to="/">总览</router-link>
    </el-menu-item>
    <el-menu-item index="database">
      <router-link to="/database">数据库</router-link>
    </el-menu-item>
    <el-menu-item index="charts">
      <router-link to="/charts">图表</router-link>
    </el-menu-item>
    <el-menu-item index="settings">
      <router-link to="/settings">设置</router-link>
    </el-menu-item> -->
    <!-- <el-sub-menu index="setting">
      <template #title>设置</template>
        <router-link to="/settings/UserInfo">
          <el-menu-item index="userInfo">用户信息</el-menu-item>
        </router-link>
    </el-sub-menu> -->
</template>
<script setup>
import { ref, onMounted } from "vue"
import { useRoute } from 'vue-router'
const route = useRoute()

const activeIndex = ref('index')

onMounted(() => {
  activeIndex.value = route.path.split('/')[1]
})

const handleSelect = (key) => {
  activeIndex.value = key
}
</script>
<style lang="scss" scoped>
.menu_content {
  width: 100%;
  height: 56px;
  margin: 0;
  padding: 0;
  list-style: none;
  border-bottom: 1px solid var(--el-color-primary);
  .menu_item {
    float: left;
    width: 97px;
    line-height: 54px;
    cursor: pointer;
    color: var(--el-color-primary);
    &:hover {
      color: var(--el-color-primary);
    }
  }
  .active {
    color: var(--el-color-primary);
    border-bottom: 2px solid var(--el-color-primary);
    font-weight: bold;
    background-color: var(--el-color-primary-light-9);
  }
}
</style>