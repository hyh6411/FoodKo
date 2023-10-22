<template>
  <div>
    {{ item.name }}
    <div>
      {{ item.content }}
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import { getElementById } from './api.js'

let id = reactive('')
const item = ref({})

onMounted(() => {
  const route = useRoute()
  id = route.query.id
  getInfo()
})

const getInfo = () => {
  if (!id) return
  getElementById(id).then(res => {
    item.value = res.result[0]
  })
}

</script>

<style lang="scss" scoped>
</style>