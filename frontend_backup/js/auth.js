/**
 * 认证相关函数
 * 处理用户注册、登录、登出等功能
 */

/**
 * 用户注册
 * @param {string} username - 用户名
 * @param {string} password - 密码
 * @param {string} email - 邮箱（可选）
 * @returns {Promise<Object>} 注册结果
 */
async function register(username, password, email = '') {
    try {
        const response = await fetch(API_ENDPOINTS.register, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password, email }),
        });

        const data = await response.json();
        return data;
    } catch (error) {
        console.error('注册错误:', error);
        throw error;
    }
}

/**
 * 用户登录
 * @param {string} username - 用户名
 * @param {string} password - 密码
 * @returns {Promise<Object>} 登录结果
 */
async function login(username, password) {
    try {
        const response = await fetch(API_ENDPOINTS.login, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });

        const data = await response.json();

        // 登录成功，保存 token 和用户信息
        if (data.success && data.token) {
            localStorage.setItem(STORAGE_KEYS.token, data.token);
            localStorage.setItem(STORAGE_KEYS.username, data.user.username);
            localStorage.setItem(STORAGE_KEYS.userId, data.user.id);
        }

        return data;
    } catch (error) {
        console.error('登录错误:', error);
        throw error;
    }
}

/**
 * 用户登出
 */
function logout() {
    // 清除本地存储
    localStorage.removeItem(STORAGE_KEYS.token);
    localStorage.removeItem(STORAGE_KEYS.username);
    localStorage.removeItem(STORAGE_KEYS.userId);

    // 跳转到登录页
    window.location.href = 'login.html';
}

/**
 * 检查是否已登录
 * @returns {boolean} 是否已登录
 */
function isLoggedIn() {
    const token = localStorage.getItem(STORAGE_KEYS.token);
    return !!token;
}

/**
 * 获取当前用户信息
 * @returns {Object} 用户信息
 */
function getCurrentUser() {
    return {
        username: localStorage.getItem(STORAGE_KEYS.username),
        userId: localStorage.getItem(STORAGE_KEYS.userId),
    };
}

/**
 * 获取认证头
 * @returns {Object} 包含 Authorization 的请求头
 */
function getAuthHeaders() {
    const token = localStorage.getItem(STORAGE_KEYS.token);
    return {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
    };
}

/**
 * 检查登录状态（用于页面加载时）
 * 如果未登录，跳转到登录页
 */
function requireAuth() {
    if (!isLoggedIn()) {
        window.location.href = 'login.html';
    }
}
