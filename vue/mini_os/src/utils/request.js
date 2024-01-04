import axios from 'axios';
const baseUrl = 'http://baidu.com'
// 封装get请求
function get(url, params) {
  return axios({
    method: 'get',
    url: baseUrl + url,
    params: params
  });
}

// 封装post请求
function post(url, data) {
  return axios({
    method: 'post',
    url: url,
    data: baseUrl + url,
  });
}

export default {
  get,
  post
};