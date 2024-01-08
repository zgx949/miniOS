import axios from 'axios';
const baseUrl = ''
// const baseUrl = 'http://win.lefthand.top'
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
  return axios({
    method: 'post',
    url: baseUrl + url,
    data: JSON.stringify(data),
    header: {"token": localStorage.getItem("token")}
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