<template>
  <div class="add_question">
    <div class="question_title">新的知识点</div>
    <el-form ref="addQuestionFormRef" :model="form" :rules="rules" label-width="100px">
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
    <el-button type="primary" @click="submit">提交</el-button>
  </div>
</template>
<script setup>
import { ref, reactive } from 'vue'
import { addQuestion } from './api.js'

const form = reactive({
  content: '',
  option: '',
  answer: '',
  explain: '暂无',
  remark: ''
})

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

const submit = () => {
  addQuestionFormRef.value.validate((valid) => {
    console.log(valid, '==========vv=>')
    if (valid) {
      const optionArr = form.option.replaceAll('\n', '').split(',')
      const obj = {}
      optionArr.forEach((item) => {
        const arr = item.split(':')
        obj[arr[0]] = arr[1]
      })
      const params = {
        ...form,
        option: JSON.stringify(obj)
      }
      addQuestion(params).then(res => {
        console.log(res, '===========>')
      })
    } else {
      console.log('error submit', '===========>')
    }
  })
}

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