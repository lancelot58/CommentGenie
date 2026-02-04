/**
 * 配置文件
 * 存放 API 地址等配置信息
 */

// API 基础地址
// 开发环境：本地服务器
// 生产环境：改为实际的服务器地址
const API_BASE_URL = 'http://localhost:5000';

// API 端点
const API_ENDPOINTS = {
    // 用户相关
    register: `${API_BASE_URL}/api/register`,
    login: `${API_BASE_URL}/api/login`,
    userInfo: `${API_BASE_URL}/api/user/info`,

    // 评语相关
    generateComment: `${API_BASE_URL}/api/comment/generate`,
    commentHistory: `${API_BASE_URL}/api/comment/history`,
    deleteComment: (id) => `${API_BASE_URL}/api/comment/${id}`,
};

// 本地存储的键名
const STORAGE_KEYS = {
    token: 'auth_token',
    username: 'username',
    userId: 'user_id',
};

// AI 模型选项
const AI_MODELS = [
    { value: 'deepseek', label: 'DeepSeek（推荐）' },
    { value: 'zhipu', label: '智谱 AI' },
    { value: 'qwen', label: '通义千问' },
    { value: 'kimi', label: 'Kimi' },
];
