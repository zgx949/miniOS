import axios from 'axios';
import {ElNotification} from "element-plus";
const baseUrl = ''
// const baseUrl = 'http://win.lefthand.top'
// 响应拦截器
axios.interceptors.response.use(
    function (response) {
      // 对响应数据进行操作
      if (response.data.code === -1) {
        ElNotification({
          title: '系统提示',
          message: `登录已经过期，请重新登录`,
          type: 'error',
        })
        localStorage.clear()
        window.location.href = '/login'
      }
      return response;
    },
    function (error) {
      // 对响应错误进行操作
      return Promise.reject(error);
    }
)

// 封装get请求
function get(url, params) {
  return axios({
    method: 'get',
    url: baseUrl + url,
    params: params,
    header: {"token": localStorage.getItem("token")}
  })
}

// 封装post请求
function post(url, data) {
  return axios.post(baseUrl + url, JSON.stringify(data),{
    headers: {
      'Content-Type': 'application/json'
    }
  })
}

// 封装postForm请求
function postForm(url, data) {
  return axios({
    method: 'post',
    url: baseUrl + url,
    data: data,
    header: {"token": localStorage.getItem("token")}
  })
}

function del(url, data) {
  return axios({
    method: 'delete',
    url: baseUrl + url,
    data: JSON.stringify(data),
    header: {"token": localStorage.getItem("token")}
  })
}




export default {
  get,
  post,
  del,
  postForm
};