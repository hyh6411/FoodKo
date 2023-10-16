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
        component: () => import('@/views/home/index.vue'),
        hidden: false
      },
      {
        path: 'jrink',
        name: 'Jrink',
        meta: { title: '喝水', noCache: true },
        component: () => import('@/views/home/jrink/index.vue'),
        hidden: false
      }
    ]
  },
  {
    path: '/database',
    name: 'Database',
    meta: { title: '数据库', noCache: true },
    component: () => import('@/layout/home.vue'),
    redirect: { name: 'DatabaseView' },
    hidden: false,
    children: [
      {
        path: 'databaseView',
        name: 'DatabaseView',
        meta: { title: '数据库', noCache: true },
        component: () => import('@/views/database/index.vue'),
        hidden: false
      },
      {
        path: 'food',
        name: 'Food',
        meta: { title: '成品', noCache: true },
        component: () => import('@/views/database/food'),
        hidden: false
      },
      {
        path: 'ingredients',
        name: 'Ingredients',
        meta: { title: '原材料', noCache: true },
        component: () => import('@/views/database/ingredients'),
        hidden: false
      },
      {
        path: 'nutrientElements',
        name: 'NutrientElements',
        meta: { title: '营养元素', noCache: true },
        component: () => import('@/views/database/NutrientElements'),
        hidden: false
      },
      {
        path: 'questions',
        name: 'Questions',
        meta: { title: '题库', noCache: true },
        component: () => import('@/views/database/questions'),
        hidden: false
      },
      {
        path: 'questionAnswer',
        name: 'QuestionAnswer',
        meta: { title: '题库', noCache: true },
        component: () => import('@/views/database/questions/questionAnswer.vue'),
        hidden: false
      },
      {
        path: 'addQuestion',
        name: 'AddQuestion',
        meta: { title: '添加题目', noCache: true },
        component: () => import('@/views/database/questions/addQuestion.vue'),
        hidden: false
      }
    ]
  },
  {
    path: '/charts',
    name: 'Charts',
    meta: { title: '图表', noCache: true },
    component: () => import('@/layout/home.vue'),
    redirect: { name: 'ChartsView' },
    hidden: false,
    children: [
      {
        path: 'chartsView',
        name: 'ChartsView',
        meta: { title: '图表', noCache: true },
        component: () => import('@/views/charts/index.vue'),
        hidden: false
      },
      {
        path: 'eatFoodHistory',
        name: 'EatFoodHistory',
        meta: { title: '吃了什么', noCache: true },
        component: () => import('@/views/charts/eatFoodHistory'),
        hidden: false
      },
      {
        path: 'jrinkHistory',
        name: 'JrinkHistory',
        meta: { title: '吃了什么', noCache: true },
        component: () => import('@/views/charts/jrinkHistory'),
        hidden: false
      }
    ]
  },
  {
    path: '/settings',
    name: 'Settings',
    meta: { title: '设置', noCache: true },
    component: () => import('@/layout/home.vue'),
    redirect: { name: 'SettingView' },
    hidden: false,
    children: [
      {
        path: 'settingView',
        name: 'SettingView',
        meta: { title: '设置菜单', noCache: true },
        component: () => import('@/views/settings/index.vue'),
        hidden: false
      },
      {
        path: 'userInfo',
        name: 'UserInfo',
        meta: { title: '个人信息', noCache: true },
        component: () => import('@/views/settings/userInfo/index.vue'),
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
