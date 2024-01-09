// router/index.js 或者相关路由配置文件

import { createRouter, createWebHistory } from 'vue-router';
import desk from '@/view/desk.vue'
import login from '@/view/login.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            redirect: '/login'
        },
        {
            path: '/login',
            name: 'Login',
            component: login
        },
        {
            path: '/desk',
            name: 'Desk',
            component: desk,
            meta: { requiresAuth: true },
        },
    ], // 你的路由配置数组
});

// 全局前置守卫
// router.beforeEach((to, from, next) => {
//     const token = localStorage.getItem('token')
//     // 判断是否已登录
//     const isLoggedIn = token !== null && token !== ''
//     // 如果存在用户登录状态
//     if (isLoggedIn) {
//         next();
//     } else {
//         // 未登录且目标不是登录页，则重定向到登录页
//         if (to.path !== '/login') {
//             next({ path: '/login', query: { redirect: to.fullPath } });
//         } else {
//             // 如果已经在访问登录页，则直接进入
//             next();
//         }
//     }
// });

export default router;