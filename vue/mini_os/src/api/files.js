import request from '../utils/request.js'
import axios from "axios";

// 传入的是文件夹id
export const list = (id) => request.get(`/api/file/list/${id}`)

export const createFCB = (data) => request.post(`/api/file/create`, data)

// export const delFCB = (id) => request.del(`/api/file/${id}`)
export const delFCB = (id) => request.post(`/api/file/delete`, {'id': id})

export const upload = (data) => request.postForm(`/api/file/upload`, data)

export const getDownloadUrl = (id, filename) => {return `/api/file/download/${id}/${filename}`}

export const getOpenUrl = (id) => {return `/api/file/open/${id}`}

export const getPreviewUrl = (url) => {return `/viewer/?file=${url}`}