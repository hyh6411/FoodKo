import { login, getInfo, logout } from '@/api/public'
import { getToken, getRefreshToken, setToken, removeToken } from '@/utils/auth.js'
import Storage from '@/utils/storage'
var storage = new Storage()
/* 获取本地存储 用户名 */
const getLoginName = _ => storage.get('loginName') || ''
const user = {
  state: {
    token: getToken(),
    refreshToken: getRefreshToken(),
    user: {},
    loginName: getLoginName()
  },

  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token
    },
    SET_REFRESH_TOKEN: (state, token) => {
      state.refreshToken = token
    },
    SET_LOGIN_NAME: (state, name) => {
      storage.set('loginName', name)
      state.loginName = name
    },
    SET_USER: (state, user) => {
      state.user = user
    }
  },

  actions: {
    // 登录
    Login({ commit }, userInfo) {
      return new Promise((resolve, reject) => {
        login(userInfo).then(res => {
          setToken(res.result.access_token)
          commit('SET_TOKEN', res.result.access_token)
          commit('SET_REFRESH_TOKEN', res.result.refresh_token)
          commit('SET_LOGIN_NAME', res.result.user_name)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },
    // 获取用户信息
    GetInfo({ commit }) {
      return new Promise((resolve, reject) => {
        getInfo({ name: getLoginName() }).then(res => {
          const result = res.result || {}
          setUserInfo(result, commit)
          resolve(result)
          window.UserInfo = result
        }).catch(error => {
          reject(error)
        })
      })
    },
    // 登出
    LogOut({ commit }) {
      return new Promise((resolve, reject) => {
        logout().then(res => {
          logOut(commit)

          resolve()
        }).catch(error => {
          logOut(commit)
          reject(error)
        })
      })
    }
  }
}

export const logOut = (commit) => {
  commit('SET_TOKEN', '')
  removeToken()
}

export const setUserInfo = (res, commit) => {
  commit('SET_USER', res)
}

export default user
