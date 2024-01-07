import axios from 'axios';
const baseUrl = ''
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
  del
};