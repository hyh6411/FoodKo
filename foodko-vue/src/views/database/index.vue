<template>
  <div class="database_content">
    <el-row>
      <el-col :span="12">
        <RouterLink to="/database/nutrientElements">
          <div class="database_item" style="background-color: rgb(11, 181, 125);">营养元素</div>
        </RouterLink>
      </el-col>
      <el-col :span="12">
        <RouterLink to="/database/questions">
          <div class="database_item" style="background-color: rgb(203, 107, 29);">题库</div>
        </RouterLink>
      </el-col>
    </el-row>
  </div>
</template>
<script setup></script>
<style lang="scss" scoped>
.database_content {
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