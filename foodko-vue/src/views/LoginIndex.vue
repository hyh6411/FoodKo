<template>
  <div>
    账号：<el-input v-model="name"></el-input>
    密码：<el-input v-model="password"></el-input>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  props: {
  },
  data() {
    return {
      name: '',
      password: ''
    }
  },
  methods: {
  }
}
</script>

<style lang="scss" scoped>
</style>