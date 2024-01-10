import request from '@/utils/request.js'

// 传入的是文件夹id
export const listApp = () => request.get(`/api/app/list`)

export const createApp = (data) => request.post(`/api/app/create`, data)

export const MarketApp = () => request.post(`/api/app/market`)

export const InstallApp = (id) => request.post(`/api/app/install`, {id: id})

export const UninstallApp = (id) => request.post(`/api/app/uninstall`, {id: id})