<template>
  <div>
    <div class="login_win" v-if="type">
      <div class="login_title">FOODKO</div>
      <el-form ref="form" :model="loginForm" label-width="100px" label-suffix=":">
        <el-form-item prop="name" label="账号" :rules="[{ required: true, message: '请输入账号', trigger: 'blur' }]">
          <el-input v-model="loginForm.name" maxlength="20"></el-input>
        </el-form-item>
        <el-form-item prop="password" label="密码" :rules="[{ required: true, message: '请输入密码', trigger: 'blur' }]">
          <el-input v-model="loginForm.password" maxlength="20" @keydown.enter="handleLogin"></el-input>
        </el-form-item>
      </el-form>
      <div class="register_btn"><a @click="goRegister">注册账户</a></div>
      <el-button style="float: right;" type="primary" @click="handleLogin">登录</el-button>
    </div>
    <div class="login_win" v-else>
      <div class="login_title">注册</div>
      <el-form ref="form" :model="loginForm" label-width="100px" label-suffix=":">
        <el-form-item prop="name" label="账号" :rules="[{ required: true, message: '请输入账号', trigger: 'blur' }]">
          <el-input v-model="loginForm.name" maxlength="20"></el-input>
        </el-form-item>
        <el-form-item prop="password" label="密码" :rules="[{ required: true, message: '请输入密码', trigger: 'blur' }]">
          <el-input v-model="loginForm.password" maxlength="20" @keydown.enter="handleLogin"></el-input>
        </el-form-item>
      </el-form>
      <el-button style="float: right;" type="primary" @click="handleLogin">注册</el-button>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, onMounted } from 'vue';
import { useRouter } from 'vue-router'
import { useStore } from 'vuex';
import { addUser } from '@/views/api.js'
import { ElMessage } from 'element-plus'

const store = useStore();
const router = useRouter()

// import { login } from '@/api/public.js'
// import Storage from '@/utils/storage'
// // import { addOperationLog } from '@/api/common'
// var storage = new Storage()

onMounted(() => {
  getLoginInfo()
})
const type = ref(true)
const goRegister = () => {
  console.log(type)
  type.value = false

}
const form = ref(null)

const loginForm = reactive({
  name: '',
  password: ''
})

function getLoginInfo() {
  // Object.keys(window.localStorage).forEach(item => {
  //   if (!['loginName', 'password', 'rememberMe'].includes(item)) {
  //     window.localStorage.removeItem(item)
  //   }
  // })

  // const rememberMe = storage.get('rememberMe') || ''
  // const loginName = storage.get('loginName') || ''
  // const password = storage.get('password') || ''
  // if (rememberMe) {
  //   this.loginForm = {
  //     loginName: loginName,
  //     password: password,
  //     rememberMe: rememberMe
  //   }
  // }
}

function handleLogin() {
  // 校验
  form.value.validate((valid) => {
    if (valid) {
      const params = {
        name: loginForm.name,
        pass: loginForm.password
      }
      if (type.value === false) {
        addUser(params)
        ElMessage({
          message: '注册成功',
          type: 'success'
        })
        type.value = true

      } else {
        store.dispatch('Login', params).then(res => {
          console.log('login', '===========>')
          router.push({ path: '/' })
        })
      }
    }
  })
}
</script>

<style lang="scss" scoped>
.register_btn {
  text-align: right;
  margin-bottom: 15px;
  font-size: 14px;
  color: rgba(42, 130, 228, 1);
}

.register_btn :hover {
  border-bottom: 1px solid rgba(42, 130, 228, 1);
}

.login_win {
  position: absolute;
  bottom: 30vh;
  left: calc(50vw - 250px);
  width: 400px;
  border: 1px solid rgb(228, 228, 228);
  box-shadow: 1px 5px 20px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  padding: 50px;
  font-weight: bold;

  .login_title {
    height: 20px;
    margin-bottom: 30px;
    font-size: 30px;
    text-align: left;
    color: rgb(160, 160, 160);
  }
}
</style>