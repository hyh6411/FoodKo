<template>
  <div class="home_content">
    <Card :dx="10" :dy="80">
      <span class="jrink_title">Jrink</span>
      <el-progress :text-inside="true" :stroke-width="26" :percentage="processNum" />
      <el-button circle size="large" class="jrink_icon" :icon="MilkTea" @click="addProcessNum()"></el-button>
    </Card>
  </div>
</template>
<script setup>
import Card from '@/components/card/index.vue'
import { ref } from 'vue'
import { MilkTea } from '@element-plus/icons-vue'

const processNum = ref(10)

function addProcessNum(num = 10) {
  processNum.value = processNum.value + num
}

</script>
<style lang="scss" scoped>
.home_content {
  .jrink_title {
    font-size: 24px;
    
  }
  .jrink_icon {
    font-size: large;
    position: absolute;
    top: 60px;
    right: -6px;
    border-right-color: gray;
  }
}
</style>