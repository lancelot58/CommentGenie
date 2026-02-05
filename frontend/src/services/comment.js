/**
 * 评语相关 API 服务
 */

import api from './api';
import { API_ENDPOINTS } from '../utils/config';

/**
 * 生成评语
 * @param {Object} data - 评语生成数据
 * @param {string} data.student_name - 学生姓名
 * @param {string} data.student_info - 学生情况
 * @param {string} data.ai_model - AI 模型
 * @returns {Promise}
 */
export const generateComment = (data) => {
    return api.post(API_ENDPOINTS.generateComment, data);
};

/**
 * 获取评语历史记录
 * @param {number} limit - 获取数量限制
 * @returns {Promise}
 */
export const getCommentHistory = (limit = 50) => {
    return api.get(API_ENDPOINTS.commentHistory, {
        params: { limit },
    });
};

/**
 * 删除评语
 * @param {number} id - 评语 ID
 * @returns {Promise}
 */
export const deleteComment = (id) => {
    return api.delete(API_ENDPOINTS.deleteComment(id));
};
