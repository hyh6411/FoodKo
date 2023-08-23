import router from './routers'

const whiteList = ['/Login', '/ForgetPwd', '/License'] // no redirect whitelist

router.beforeEach((to, from, next) => {
  if (storage.get('token')) {
    // 已登录且要跳转的页面是登录页
    // if (to.path === '/Login') {
    //   // 不需要设置默认页面
    //   if (store.getters.homePagePath) {
    //     next({ path: store.getters.homePagePath })
    //   } else {
    //     store.dispatch('GetHomePath').then(res => {
    //       next({ path: res })
    //     })
    //   }
    // } else {
    //   if (!store.getters.user.loginName) {
    //     // 判断当前用户是否已拉取完user_info信息
    //     store
    //       .dispatch('GetInfo')
    //       .then(res => {
    //         // webSocket 启动长链接
    //         // connectSocket()
    //         // 拉取user_info
    //         store
    //           .dispatch('setLocale')
    //           .then(res => {
    //             // 获取国际化
    //             store.dispatch('setBtnPermission').then(res => {
    //               // 按钮权限集合
    //               // 动态路由，拉取菜单
    //               loadMenus(next, to)
    //               queryBaseSettingDynamicParam('documentService').then(res=> {
    //                 const script = document.createElement('script');
    //                 script.src = `${res.result.value}/web-apps/apps/api/documents/api.js`;
    //                 document.body.appendChild(script);
    //               })
    //             })
    //           })
    //           .catch(err => {
    //             console.log('获取国际化失败', err)
    //           })
    //       })
    //       .catch(err => {
    //         console.log(err)
    //       })
    //     // 登录时未拉取 菜单，在此处拉取
    //   } else if (store.getters.loadMenus) {
    //     // 修改成false，防止死循环
    //     store.dispatch('updateLoadMenus').then(res => {})
    //     loadMenus(next, to)
    //   } else {
    //     next()
    //     console.log("非微前端环境")
    //   }
    // }
  } else {
    /* has no token*/
    // if (whiteList.indexOf(to.path) !== -1) {
    //   // 在免登录白名单，直接进入
    //   next()
    // } else {
    //   next({ path: '/Login' }) // 否则全部重定向到登录页
    // }
  }
})