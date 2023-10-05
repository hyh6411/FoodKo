import router from './routers'
import { getToken } from '@/utils/auth.js'
import store from '@/store'

const whiteList = ['/Login', '/ForgetPwd', '/License'] // no redirect whitelist

router.beforeEach((to, from, next) => {
  if (getToken()) {
    // 已登录且要跳转的页面是登录页
    if (to.path === '/Login') {
      // 不需要设置默认页面
      next({ path: '/home' })
    } else {
      // if (!store.getters.user.user_name) {
      //   // 判断当前用户是否已拉取完user_info信息
      //   store.dispatch('GetInfo')
      //     .then(res => {
      //       next()
      //     })
      //     .catch(err => {
      //       console.log(err)
      //     })
      // } else {
        next()
      // }
    }
  } else {
    /* has no token*/
    if (whiteList.indexOf(to.path) !== -1) {
      // 在免登录白名单，直接进入
      next()
    } else {
      next({ path: '/Login' }) // 否则全部重定向到登录页
    }
  }
})