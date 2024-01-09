import request from '../utils/request.js'
export const userLogin = (data) => request.post('/api/users/login', data)
export const userRegister= (data) => request.post('/api/users/register', data)
export const userLogout= () => request.post('/api/users/logout')
