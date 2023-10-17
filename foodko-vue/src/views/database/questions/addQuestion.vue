<template>
  <div class="add_question">
    <!-- <div class="question_title">新的知识点</div> -->
    <el-form ref="addQuestionFormRef" :model="form" :disabled="!isEdit" :rules="rules" label-width="100px">
      <el-form-item label="问题内容" prop="content">
        <el-input
          v-model="form.content"
          type="textarea"
          :rows="4"
          maxlength="255"
          show-word-limit
        ></el-input>
      </el-form-item>
      <el-form-item label="问题选项" prop="option">
        <el-input
          v-model="form.option"
          type="textarea"
          :rows="4"
          maxlength="255"
          show-word-limit
        ></el-input>
      </el-form-item>
      <el-form-item label="问题答案" prop="answer">
        <el-input
          v-model="form.answer"
          maxlength="2"
        ></el-input>
      </el-form-item>
      <el-form-item label="答案解释" prop="explain">
        <el-input
          v-model="form.explain"
          type="textarea"
          :rows="4"
          maxlength="255"
          show-word-limit
        ></el-input>
      </el-form-item>
    </el-form>
  </div>
</template>
<script setup>
import { ref, reactive, defineProps } from 'vue'

const props = defineProps({
  isEdit: {
    // 是否编辑状态 true新增/false预览
    type: Boolean,
    default: false
  }
})

const initForm = reactive({
  content: '',
  option: '',
  answer: '',
  explain: '暂无',
  remark: ''
})
const form = ref({ ...initForm })

const addQuestionFormRef = ref(null)

const rules = reactive({
  content: [
    {
      required: true,
      message: '请输入问题内容',
      trigger: 'blur'
    }
  ],
  option: [
    {
      required: true,
      message: '请输入问题选项',
      trigger: 'blur'
    }
  ],
  answer: [
    {
      required: true,
      message: '请输入问题答案',
      trigger: 'blur'
    }
  ]
})

const resetFields = (formData) => {
  const data = formData || initForm
  form.value = { ...data }
  addQuestionFormRef.value.clearValidate()
}

const submit = () => {
  return new Promise((resolve, reject) => {
    addQuestionFormRef.value.validate((valid) => {
      if (valid) {
        const optionArr = form.value.option.replaceAll('\n', '').split(',')
        const obj = {}
        optionArr.forEach((item) => {
          const arr = item.split(':')
          obj[arr[0]] = arr[1]
        })
        const params = {
          ...form.value,
          option: JSON.stringify(obj)
        }
        resolve(params)
      } else {
        reject(new Error('表单验证不通过'))
      }
    })
  })
}

defineExpose({
  resetFields,
  submit
})

</script>
<style lang="scss" scoped>
.add_question {
  padding: 20px;

  .question_title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 50px;
    border-left: 5px solid var(--el-color-primary);
    text-align: left;
    padding-left: 10px;
  }

  ::v-deep .el-form-item__label {
    font-weight: bold;
  }
}
</style>