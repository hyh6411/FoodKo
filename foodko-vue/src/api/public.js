import request from '@/utils/request.js'

export function login(data) {
  return request({
    url: '/account/login/',
    method: 'post',
    data
  })
}

export function getInfo({ name, id }) {
  return request({
    url: '/account/queryUserInfo/?name=' + name + '&id=' + id,
    method: 'get'
  })
}

export function updateUserInfo(data) {
  return request({
    url: '/account/update/',
    method: 'post',
    data
  })
}

export function addUser(data) {
  return request({
    url: '/account/add/',
    method: 'post',
    data
  })
}

export function deleteUser(data) {
  return request({
    url: '/account/delete/',
    method: 'post',
    data
  })
}

export function logout() {
  return request({
    url: '/account/logout/',
    method: 'post'
  })
}

export function refreshToken() {
  return request({
    url: '/account/refresh/',
    method: 'get'
  })
}

