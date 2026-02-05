/**
 * 消息提示 Composable
 * 封装 Element Plus 的 ElMessage
 */

import { ElMessage } from 'element-plus';

export function useMessage() {
    const showSuccess = (message) => {
        ElMessage.success(message);
    };

    const showError = (message) => {
        ElMessage.error(message);
    };

    const showWarning = (message) => {
        ElMessage.warning(message);
    };

    const showInfo = (message) => {
        ElMessage.info(message);
    };

    return {
        showSuccess,
        showError,
        showWarning,
        showInfo,
    };
}
