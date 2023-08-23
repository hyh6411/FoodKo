import { createRouter, createWebHashHistory } from 'vue-router'

export const constantRouterMap = [
  {
    path: '/', redirect: { name: 'Login' }
  },
  {
    path: '/Login',
    name: 'Login',
    meta: { title: '登录', noCache: true },
    component: () => import('@/views/LoginIndex.vue'),
    hidden: true
  },
  {
    path: '/ForgetPwd',
    meta: { title: '忘记密码', noCache: true },
    component: () => import('@/views/forgetPwd/ForgetIndex.vue'),
    hidden: true
  },
  {
    path: '/404',
    component: () => import('@/views/features/404/indexView.vue'),
    hidden: true
  },
  {
    path: '/401',
    component: () => import('@/views/features/401/indexView.vue'),
    hidden: true
  },
]

export default createRouter({
  // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
  history: createWebHashHistory(),
  routes: constantRouterMap, // `routes: routes` 的缩写
})
