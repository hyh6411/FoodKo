<template>
  <div class="question_content">
    <el-row>
      <el-col :span="12">
        <div class="database_item" style="background-color: rgb(11, 181, 125);" @click="goQuestion">
          每日一练(10题)
        </div>
      </el-col>
      <el-col :span="12">
        <div class="database_item" style="background-color: rgb(203, 107, 29); " @click="goQuestionAll">
          无尽挑战
        </div>
      </el-col>
    </el-row>
    <div class="question_table">
      <div class="q_operation">
        <el-button type="primary" @click="handleAddQuestion">新增</el-button>
        <el-button type="primary" :disabled="!selectRow.length" @click="deleteQuestion">删除</el-button>
      </div>
      <vxe-table border resizable highlight-hover-row highlight-current-row auto-resize row-id="id" show-overflow
        :data="tableData" @cell-click="handleRowClick" @checkbox-all="handleSelectionChange"
        @checkbox-change="handleSelectionChange">
        <vxe-column type="checkbox" width="60"></vxe-column>
        <vxe-column v-for="(item, index) in tableColumns" :key="index" :field="item.field" :title="item.title"
          :min-width="item.field === 'content' ? '150' : ''"></vxe-column>
      </vxe-table>
    </div>
    <el-dialog v-model="showAddDialog" title="新增知识点" width="90vw" top="10vh">
      <div v-if="isEditDialog" class="q_operation">
        <el-button v-show="!isEdit" type="primary" @click="isEdit = true">编辑</el-button>
        <el-button v-show="isEdit" @click="submitUpdateQuestion">保存</el-button>
        <el-button v-show="isEdit" @click="cancelUpdateQuestion">取消</el-button>
      </div>
      <addQuestionForm ref="addQuestionFormRef" :is-edit="isEdit"></addQuestionForm>
      <template #footer>
        <span class="dialog-footer">
          <el-button @click="cancelAddQuestion">取消</el-button>
          <el-button v-if="!isEditDialog" type="primary" @click="addQuestionSubmit">提交</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>
<script setup>
import { ref, reactive, onMounted, nextTick, inject } from 'vue'
import { addQuestion, deleteQuestionByIds, updateQuestionById, getAllQuestionList } from './api'
const utils = inject('$utils')

import addQuestionForm from './addQuestion.vue';

import { useRouter } from "vue-router";
const router = useRouter();
const tableData = ref([])
const tableColumns = ref([
  { field: 'content', title: '问题内容', type: 'input' },
  { field: 'remark', title: '备注', type: 'input' }
])
const selectRow = ref([])
const isEdit = ref(false)
const isEditDialog = ref(false)
const showAddDialog = ref(false)
let copyRowData = {}
const addQuestionFormRef = ref(null)


onMounted(() => {
  getTableData()
})

const goQuestion = () => {
  router.push({
    path: "/database/questionAnswer",
    query: { type: 1 }
  })
}
const goQuestionAll = () => {
  router.push({
    path: "/database/questionAnswer",
    query: { type: 2 }
  })

}

const handleSelectionChange = ({ records }) => {
  // 选中行
  selectRow.value = records
}

const getTableData = () => {
  // 查询表格数据
  getAllQuestionList().then(res => {
    tableData.value = res.result
  })
}

// ========= 新增知识点 =========================
const handleAddQuestion = () => {
  showAddDialog.value = true
  isEdit.value = true
}

const cancelAddQuestion = () => {
  showAddDialog.value = false
  isEdit.value = false
  isEditDialog.value = false
  addQuestionFormRef.value.resetFields()
}

const addQuestionSubmit = () => {
  addQuestionFormRef.value.submit().then((params) => {
    addQuestion(params).then(res => {
      utils.showMessageBox('success', '添加成功!')
      showAddDialog.value = false
      isEdit.value = false
    })
  }).catch(err => {
    console.log('err')
  })
}
// ============================================

// ======== 删除知识点 =========================
const deleteQuestion = () => {
  const ids = selectRow.value.map(item => item.id)
  deleteQuestionByIds(ids).then(res => {
    getTableData()
  })
}

// ======== 修改知识点 =========================
const handleRowClick = ({ row }) => {
  isEditDialog.value = true
  showAddDialog.value = true
  nextTick(() => {
    // 将json对象转换为字符串
    let str = ''
    const objOption = JSON.parse(row.option)
    for (const key in objOption) {
      str += `${key}:${objOption[key]},`
    }
    str = str.substring(0, str.length - 1)
    row.option = str
    copyRowData = { ...row }
    addQuestionFormRef.value.resetFields(row)
  })
}

const cancelUpdateQuestion = () => {
  isEdit.value = false
  addQuestionFormRef.value.resetFields(copyRowData)
}

const submitUpdateQuestion = () => {
  addQuestionFormRef.value.submit().then((params) => {
    updateQuestionById(params).then(res => {
      getTableData()
    })
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
    cursor: pointer;
    padding: 50px;
    margin: 20px;
    text-align: center;
    border: 1px solid gray;
    border-radius: 10px;
    color: white;
  }
}

.question_table {
  padding: 20px;

  ::v-deep .vxe-table--body-wrapper {
    overflow-y: auto;
    height: calc(100vh - 400px);
  }
}

::v-deep .q_operation {
  margin-bottom: 20px;
  display: flex;
  justify-content: flex-end;
}
</style>