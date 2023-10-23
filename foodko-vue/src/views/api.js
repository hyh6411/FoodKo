import request from '@/utils/request.js'

// 注册
export function addUser(data) {
  return request({
    url: '/account/add/',
    method: 'post',
    data
  })
}
