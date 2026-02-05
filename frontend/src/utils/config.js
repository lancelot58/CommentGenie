/**
 * 配置文件
 * 存放 API 地址等配置信息
 */

// API 基础地址
// 从环境变量读取，如果没有则使用默认值
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:5000';

// API 端点
export const API_ENDPOINTS = {
    // 用户相关
    register: '/api/register',
    login: '/api/login',
    userInfo: '/api/user/info',

    // 评语相关
    generateComment: '/api/comment/generate',
    commentHistory: '/api/comment/history',
    deleteComment: (id) => `/api/comment/${id}`,
};

// 本地存储的键名
export const STORAGE_KEYS = {
    token: 'auth_token',
    username: 'username',
    userId: 'user_id',
};

// AI 模型选项
export const AI_MODELS = [
    { value: 'deepseek', label: 'DeepSeek（推荐）' },
    { value: 'zhipu', label: '智谱 AI' },
    { value: 'qwen', label: '通义千问' },
    { value: 'kimi', label: 'Kimi' },
];

export { API_BASE_URL };
