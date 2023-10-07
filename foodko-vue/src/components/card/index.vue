<template>
  <div ref="card_content" class="card_content">
    <slot></slot>
  </div>
</template>
<script setup>
import { ref, defineProps, watch, onMounted } from 'vue'

const card_content = ref(null)
const props = defineProps({
  dx: {
    type: Number,
    default: 10
  },
  dy: {
    type: Number,
    default: 80
  },
  dwidth: {
    type: Number,
    default: 250
  },
  dheight: {
    type: Number,
    default: 80
  }
})

onMounted(() => {
  if (card_content.value) {
    card_content.value.style.left = props['dx'] + 'px'
    card_content.value.style.top = props['dy'] + 'px'
    card_content.value.style.width = props['dwidth'] + 'px'
    card_content.value.style.height = props['dheight'] + 'px'
  }
})

watch(() => props['dx'], (val) => {
  if (card_content.value) {
    card_content.value.style.left = val + 'px'
  }
}, { deep: true })
watch(() => props['dy'], (val) => {
  if (card_content.value) {
    card_content.value.style.top = val + 'px'
  }
}, { deep: true })
watch(() => props['dwidth'], (val) => {
  if (card_content.value) {
    card_content.value.style.width = val + 'px'
  }
}, { deep: true })
watch(() => props['dheight'], (val) => {
  if (card_content.value) {
    card_content.value.style.height = val + 'px'
  }
}, { deep: true })
</script>
<style scoped>
.card_content {
  position: absolute;
  border: 1px solid gray;
  box-shadow: 1px 5px 20px rgba(0, 0, 0, 0.1);
  border-radius: 20px;
  padding: 50px;
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  background-color: rgba(255, 255, 255, 0.5);
}
</style>