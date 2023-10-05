import axios from 'axios'
import router from '@/router/routers'
import { MessageBox } from 'element-plus';
import debounce from 'lodash/debounce'
// import store from '../store/index'
import { getToken, removeToken } from '@/utils/auth'
import Config from '@/settings'
// import Storage from '@/utils/storage'
// const storage = new Storage()
// 请求出错
const onRequestError = debounce(({ message, ...rest }) => {
  MessageBox.alert(message, '系统错误', {
    confirmButtonText: '确定',
    type: 'error',
    callback: action => {}
  })
  console.warn(`http请求出错: [${message}], code: ${rest.code}`)
  return rest
}, 400)

const TokenExprie = debounce(() => {
  MessageBox.alert(
    '登录状态已过期或者您的账号在别处登录，您可以继续留在该页面，或者重新登录',
    '系统提示',
    {
      confirmButtonText: '重新登录',
      type: 'warning',
      showClose: false
    }
  ).then(() => {
    removeToken()
    /* store.dispatch('LogOut').then(() => {
      location.reload() // 为了重新实例化vue-router对象 避免bug
    })*/
    router.push({ path: '/Login' })
  })
}, 1000)

// 创建axios实例F
const service = axios.create({
  // 直接拿配置即可，dev环境通过webpack 中代理直接访问后台8000 端口，所以要指定8000， prod环境是通过ngnix做的转发，所以没写端口（默认80），然后通过ngnix 配置做的8000端口转发
  // baseURL: process.env.NODE_ENV === 'production' ? process.env.VUE_APP_BASE_API : '', // api 的 base_url , 这里/ 是因为用了直接部署到比如80 端口上所有直接 /
  // baseURL: process.env.VUE_APP_BASE_API,
  timeout: Config.timeout // 请求超时时间
})

// request拦截器
service.interceptors.request.use(
  config => {
    /* console.log(getToken()) */
    if (getToken()) {
      config.headers['Authorization'] = getToken() // 让每个请求携带自定义token 请根据实际情况自行修改
      // config.headers['X-Access-Lang'] = storage.get('locale')
    }
    config.headers['Accept'] = 'application/json'
    config.headers['Content-Type'] = 'application/json'
    // config.headers["Content-Type"] = "application/x-www-form-urlencoded";
    return config
  },
  error => Promise.reject(error)
)

// response 拦截器
service.interceptors.response.use(
  response => {
    const code = response.data.code
    if (code < 200 || code > 300) {
      if (code === 401) {
        TokenExprie()
      } else if (code === 403) {
        window.location.href = window.location.origin + '/License'
      } else {
        onRequestError({ message: response.data.message })
        return Promise.reject('error')
      }
    } else {
      if (response.config.responseType === 'blob' && response.config.method === 'post') {
        return new Promise((resolve, reject) => {
          if (response.headers['content-type'].includes('json')) {
            const reader = new FileReader()
            reader.onload = () => {
              try {
                const { result } = reader
                const errorInfo = JSON.parse(result)
                if (errorInfo.code !== 200) {
                  onRequestError(errorInfo)
                  reject(errorInfo)
                } else {
                  resolve(errorInfo)
                }
              } catch (err) {
                resolve(response)
              }
            }
            reader.onerror = err => {
              reject(err)
            }
            reader.readAsText(response.data)
          } else {
            resolve(response)
          }
        })
      }
      return response.data
    }
  },
  error => {
    let code = 0
    try {
      code = error.response.data.code
    } catch (e) {
      if (error.toString().indexOf('Error: timeout') !== -1) {
        return Promise.reject(onRequestError({ message: '网络请求超时' }))
      }
    }
    if (code) {
      if (code === 401) {
        TokenExprie()
      } else if (code === 403) {
        router.push({ path: '/401' })
      } else {
        const errorMsg = error.response.data.message
        if (errorMsg !== undefined) {
          onRequestError({ message: errorMsg })
        }
      }
    }
    // return Promise.reject(onRequestError({ message: '系统升级维护中，请稍后！' }))
  }

)
export default service
