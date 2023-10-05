import Config from '@/settings'
import Storage from './storage'
var storage = new Storage()
var time = Config.tokenCookieExpires * 60 * 60 * 1000 * 24
// var time = 1 * 60 * 60 * 1000 * 24 // 天
// var time = 0.5 * 60 * 1000 // 分
const TokenKey = Config.TokenKey
const refreshTokenKey = Config.refreshTokenKey

export function getToken() {
  return storage.get(TokenKey)
  // return localStorage.getItem(TokenKey)
}

export function getRefreshToken() {
  return storage.get(refreshTokenKey)
  // return localStorage.getItem(refreshTokenKey)
}

export function setToken(token, rememberMe) {
  // if (rememberMe) {
  return storage.set(TokenKey, token, time)
  // } else {
  //   return storage.set(TokenKey, token)
  // }
}

export function removeToken() {
  return storage.remove(TokenKey)
}

