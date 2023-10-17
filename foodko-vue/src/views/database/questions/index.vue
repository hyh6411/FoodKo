<template>
  <div class="question_content">
    <el-row>
      <el-col :span="12">
        <div class="database_item" style="background-color: rgb(11, 181, 125);" @click="dialogTableVisible = true">练习
        </div>
      </el-col>
      <el-col :span="12">
        <RouterLink to="/database/addQuestion">
          <div class="database_item" style="background-color: rgb(203, 107, 29);">新增</div>
        </RouterLink>
      </el-col>
    </el-row>
    <el-dialog v-model="dialogTableVisible" title="选择模式" style="width: 500px;">
      <div @click="goQuestion" class="database_item" style="background-color: rgb(203, 107, 29);">每日一练(10题)</div>
      <div class="database_item" style="background-color: rgb(11, 181, 125);">无尽模式</div>
    </el-dialog>
  </div>
</template>
<script setup>

import { useRouter } from "vue-router";
import { ref } from 'vue'
const router = useRouter();
const dialogTableVisible = ref(false)
const goQuestion = () => {
  router.push({
    path: "/database/questionAnswer",
    query: { type: 1 }
  })
}
</script>
<style lang="scss" scoped>
.question_content {
  a {
    text-decoration: none;
    color: #2c3e50;
  }

  .database_item {
    padding: 50px;
    margin: 20px;
    text-align: center;
    border: 1px solid gray;
    border-radius: 10px;
    color: white;
  }
}
</style>