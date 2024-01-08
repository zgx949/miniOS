import request from '../utils/request.js'
import axios from "axios";

// 传入的是文件夹id
export const list = (id) => request.get(`/api/file/list/${id}`)

export const createFCB = (data) => request.post(`/api/file/create`, data)

export const delFCB = (id) => request.del(`/api/file/${id}`)

export const upload = (data) => request.postForm(`/api/file/upload`, data)