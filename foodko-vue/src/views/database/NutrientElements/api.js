import request from '@/utils/request.js'

export function queryAllElementList() {
  return request({
    url: '/element/queryAllElement/',
    method: 'get'
  })
}

export function getElementById(id) {
  return request({
    url: '/element/queryElement/?id=' + id,
    method: 'get'
  })
}

export function addElement(data) {
  return request({
    url: '/element/addElement/',
    method: 'post',
    data
  })
}

export function updateElementById(data) {
  return request({
    url: '/element/updateElement/',
    method: 'post',
    data
  })
}

export function deleteElementByIds(data) {
  return request({
    url: '/element/deleteElement/',
    method: 'post',
    data
  })
}
