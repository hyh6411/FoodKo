import { createRouter, createWebHashHistory } from 'vue-router'

export const constantRouterMap = [
  {
    path: '/', redirect: { name: 'Overview' }
  },
  {
    path: '/Login',
    name: 'Login',
    meta: { title: '登录', noCache: true },
    component: () => import('@/views/LoginIndex.vue'),
    hidden: true
  },
  {
    path: '/home',
    name: 'Home',
    meta: { title: '首页', noCache: true },
    component: () => import('@/layout/home.vue'),
    hidden: false,
    children: [
      {
        path: 'overview',
        name: 'Overview',
        meta: { title: '总览', noCache: true },
        component: () => import('@/views/home/overView/index.vue'),
        hidden: false
      },
      {
        path: 'historyRecord',
        name: 'HistoryRecord',
        meta: { title: '历史记录', noCache: true },
        component: () => import('@/views/home/historyRecord/index.vue'),
        hidden: false
      }
    ]
  },
  {
    path: '/settings',
    name: 'Settings',
    meta: { title: '设置', noCache: true },
    component: () => import('@/layout/home.vue'),
    hidden: false,
    children: [
      {
        path: 'UserInfo',
        name: 'UserInfo',
        meta: { title: '个人信息', noCache: true },
        component: () => import('@/views/settings/UserInfo.vue'),
        hidden: false
      },
    ]
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
