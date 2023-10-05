import { createApp } from 'vue'
import store from './store/index'
import router from './router/routers.js'
import './router/index' // control
// import VueRouter from 'vue-router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'

const app = createApp(App)

app.use(store)
app.use(router)
app.use(ElementPlus)
app.mount('#app')
