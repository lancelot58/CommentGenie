/**
 * Axios API 配置
 * 配置请求拦截器和响应拦截器
 */

import axios from 'axios';
import { API_BASE_URL, STORAGE_KEYS } from '../utils/config';
import router from '../router';

// 创建 axios 实例
const api = axios.create({
    baseURL: API_BASE_URL,
    timeout: 30000,
    headers: {
        'Content-Type': 'application/json',
    },
});

// 请求拦截器 - 自动添加 token
api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(STORAGE_KEYS.token);
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

// 响应拦截器 - 处理错误
api.interceptors.response.use(
    (response) => {
        return response;
    },
    (error) => {
        // 处理 401 未授权错误
        if (error.response && error.response.status === 401) {
            // 清除本地存储
            localStorage.removeItem(STORAGE_KEYS.token);
            localStorage.removeItem(STORAGE_KEYS.username);
            localStorage.removeItem(STORAGE_KEYS.userId);
            // 跳转到登录页
            router.push('/login');
        }
        return Promise.reject(error);
    }
);

export default api;
