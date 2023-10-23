<template>
  <div v-loading="tloading" class="element_list">
    <el-input
      v-model="search"
      placeholder="请输入名称"
      clearable
      @change="getElementList"
    ></el-input>
    <GradList :list-data="tableData" @handleClick="handleRowClick"></GradList>
  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'

import { useRouter } from "vue-router"
const router = useRouter()

import { queryAllElementList } from './api.js'

import GradList from '@/views/database/components/gradList.vue'

const search = ref('')
const tloading = ref(false)
const tableData = ref([])

onMounted(() => {
  getElementList()
})

const getElementList = () => {
  tloading.value = true
  queryAllElementList().then(res => {
    tloading.value = false
    const data = res.result
    tableData.value = data.filter(row => row.name.includes(search.value))
  })
}

const handleRowClick = (row) => {
  console.log('==id=========>', row.id)
  router.push({
    path: '/database/elementInfomation',
    query: {
      id: row.id
    }
  })
}

</script>
<style scoped lang="scss">
.element_list {
  padding: 20px;
  ::v-deep .el-input__wrapper {
    border-radius: 20px;
  }
}
</style>
