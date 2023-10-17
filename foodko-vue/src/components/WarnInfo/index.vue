<template>
  <span class="messageInfo">
    <el-tag type="warning" class="document-tip" style="white-space: normal;">
      <i class="iconfont iconicon_message"></i>
      <slot></slot>
    </el-tag>
  </span>
</template>

<script setup>
</script>

<style lang="scss" scoped>
.messageInfo {
  margin-top: 5px;
  display: inline-block;
  .document-tip {
    font-weight: normal !important;
    color: #ff852b !important;
  }
}
</style>
