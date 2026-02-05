/**
 * 认证相关 Composable
 * 处理用户注册、登录、登出等功能
 */

import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import api from '../services/api';
import { API_ENDPOINTS, STORAGE_KEYS } from '../utils/config';

export function useAuth() {
    const router = useRouter();
    const loading = ref(false);
    const error = ref(null);

    // 检查是否已登录
    const isLoggedIn = computed(() => {
        return !!localStorage.getItem(STORAGE_KEYS.token);
    });

    // 获取当前用户信息
    const getCurrentUser = () => {
        return {
            username: localStorage.getItem(STORAGE_KEYS.username),
            userId: localStorage.getItem(STORAGE_KEYS.userId),
        };
    };

    /**
     * 用户注册
     */
    const register = async (username, password, email = '') => {
        loading.value = true;
        error.value = null;

        try {
            const response = await api.post(API_ENDPOINTS.register, {
                username,
                password,
                email,
            });

            loading.value = false;
            return response.data;
        } catch (err) {
            loading.value = false;
            error.value = err.response?.data?.message || '注册失败';
            throw err;
        }
    };

    /**
     * 用户登录
     */
    const login = async (username, password) => {
        loading.value = true;
        error.value = null;

        try {
            const response = await api.post(API_ENDPOINTS.login, {
                username,
                password,
            });

            const data = response.data;

            // 登录成功，保存 token 和用户信息
            if (data.success && data.token) {
                localStorage.setItem(STORAGE_KEYS.token, data.token);
                localStorage.setItem(STORAGE_KEYS.username, data.user.username);
                localStorage.setItem(STORAGE_KEYS.userId, data.user.id);
            }

            loading.value = false;
            return data;
        } catch (err) {
            loading.value = false;
            error.value = err.response?.data?.message || '登录失败';
            throw err;
        }
    };

    /**
     * 用户登出
     */
    const logout = () => {
        // 清除本地存储
        localStorage.removeItem(STORAGE_KEYS.token);
        localStorage.removeItem(STORAGE_KEYS.username);
        localStorage.removeItem(STORAGE_KEYS.userId);

        // 跳转到登录页
        router.push('/login');
    };

    return {
        loading,
        error,
        isLoggedIn,
        getCurrentUser,
        register,
        login,
        logout,
    };
}
