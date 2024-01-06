import request from '../utils/request.js'

// 传入的是文件夹id
export const list = (id) => request.get(`/api/file/list/${id}`)

export const createFCB = (data) => request.post(`/api/file/create`, data)