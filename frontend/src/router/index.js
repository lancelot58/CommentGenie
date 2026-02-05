/**
 * Vue Router 配置
 */

import { createRouter, createWebHistory } from 'vue-router';
import { STORAGE_KEYS } from '../utils/config';

// 路由配置
const routes = [
    {
        path: '/login',
        name: 'Login',
        component: () => import('../views/LoginView.vue'),
        meta: { requiresAuth: false },
    },
    {
        path: '/register',
        name: 'Register',
        component: () => import('../views/RegisterView.vue'),
        meta: { requiresAuth: false },
    },
    {
        path: '/',
        name: 'Home',
        component: () => import('../views/HomeView.vue'),
        meta: { requiresAuth: true },
    },
];

// 创建路由实例
const router = createRouter({
    history: createWebHistory(),
    routes,
});

// 路由守卫 - 检查认证状态
router.beforeEach((to, from, next) => {
    const token = localStorage.getItem(STORAGE_KEYS.token);
    const isLoggedIn = !!token;

    // 需要认证的页面
    if (to.meta.requiresAuth && !isLoggedIn) {
        next('/login');
    }
    // 已登录用户访问登录/注册页面，跳转到首页
    else if ((to.path === '/login' || to.path === '/register') && isLoggedIn) {
        next('/');
    }
    else {
        next();
    }
});

export default router;
