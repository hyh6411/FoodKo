import request from '@/utils/request.js'

// 新增
export function addQuestion(data) {
  return request({
    url: '/question/addQuestion/',
    method: 'post',
    data
  })
}

// 获取随机题目
export function getQuestion(params) {
  return request({
    url: '/question/getQuestion/',
    method: 'get',
    params
  })
}

// 删除
export function deleteQuestionByIds(data) {
  return request({
    url: '/question/deleteQuestion/',
    method: 'post',
    data
  })
}

// 修改
export function updateQuestionById(data) {
  return request({
    url: '/question/updateQuestion/',
    method: 'post',
    data
  })
}

// 查询全部 - 后期优化分页
export function getAllQuestionList() {
  return request({
    url: '/question/queryAllQuestion/',
    method: 'get'
  })
}