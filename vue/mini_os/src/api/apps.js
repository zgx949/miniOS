import request from '@/utils/request.js'

// 传入的是文件夹id
export const listApp = () => request.get(`/api/app/list`)

export const createApp = (data) => request.post(`/app/create`, data)