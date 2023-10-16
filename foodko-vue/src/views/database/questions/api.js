import request from '@/utils/request.js'

export function addQuestion(data) {
  return request({
    url: '/question/addQuestion/',
    method: 'post',
    data
  })
}