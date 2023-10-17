import { createApp } from 'vue'
import store from './store/index'
import router from './router/routers.js'
import './router/index' // control
// import VueRouter from 'vue-router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import VXETable from 'vxe-table'
import 'vxe-table/lib/style.css'

import App from './App.vue'
import UTILS from './utils/utils.js'

const app = createApp(App).use(VXETable)
// app.config.globalProperties.$utils = UTILS
// 添加全局属性或方法
app.provide('$utils', UTILS)


app.use(store)
app.use(router)
app.use(ElementPlus)
app.mount('#app')
