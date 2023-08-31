<template>
  <div>
    <div class="login_win">
      <div class="login_title">登录</div>
      <el-form v-model="loginForm" label-width="100px" label-suffix=":">
        <el-form-item prop="name" label="账号">
          <el-input v-model="loginForm.name" maxlength="20"></el-input>
        </el-form-item>
        <el-form-item prop="password" label="密码">
          <el-input v-model="loginForm.password" maxlength="20"></el-input>
        </el-form-item>
      </el-form>
      <el-button style="float: right;" type="primary" @click="login">登录</el-button>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue';
const loginForm = reactive({
  name: '',
  password: ''
})

function login() {
  
}
</script>

<style lang="scss" scoped>
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