<template>
  <div class="grad_list">
    <div
      v-for="item in props.listData"
      :key="item.id"
      class="grad_item"
      :style="{
        'background-image': item.img ? `url(${item.img})` : `radial-gradient(circle at 50%, ${item.back_color} 60%, transparent 61%),radial-gradient(circle at 70% 35%, ${lightenColor(item.back_color, 20)} 30%, transparent 31%)`
      }"
      @click="handleClick(item)"
    >
      {{ item.name }}
    </div>
  </div>
</template>

<script setup>
import { ref, defineProps, defineEmits } from 'vue'

import tinycolor from 'tinycolor2'

const props = defineProps({
  listData: {
    type: Array,
    default: () => []
  }
})

const emits = defineEmits(['handleClick']);

const lightenColor = (color, amount) => {
  const c = tinycolor(color)
  return c.lighten(amount).toHexString()
}

const handleClick = (item) => {
  emits('handleClick', item)
}
</script>

<style lang="scss" scoped>
.grad_list {
  // 网格布局
  margin-top: 20px;
  .grad_item {
    float: left;
    margin-right: 20px;
    &:last-child {
      margin-right: 0;
    }
    height: 120px;
    width: 120px;
    line-height: 120px;
    border-radius: 10px;
    background-image: radial-gradient(circle at 50%, #d74646 60%, transparent 61%),
                      radial-gradient(circle at 70% 35%, lighten(#d74646, 20%) 30%, transparent 31%);
    // background-size: 50% 100%;
    background-repeat: no-repeat;
    color: white;
    cursor: pointer;
  }
}

/* 在 style 中使用 Sass 预处理器语法 */
/* 定义 lighten() 函数 */
@function lighten($color, $amount) {
  @return mix(white, $color, $amount);
}

@media screen and (max-width: 480px) {
  .grad_list {
    .grad_item {
      height: 100px;
      width: 100px;
      line-height: 100px;
    }
  }
}
</style>