<template>
  <div class="home-container">
    <el-card class="main-card">
      <!-- 头部导航 -->
      <div class="header">
        <div class="header-left">
          <h1>CommentGenie</h1>
          <span class="user-info">欢迎，{{ currentUser.username }}</span>
        </div>
        <el-button type="danger" @click="handleLogout">退出登录</el-button>
      </div>

      <!-- 评语生成表单 -->
      <CommentForm
        ref="commentFormRef"
        :loading="generating"
        @submit="handleGenerateComment"
      />

      <!-- 生成结果显示 -->
      <el-card v-if="generatedComment" class="result-card" shadow="never">
        <template #header>
          <div class="result-header">
            <h3>生成结果</h3>
            <el-tag :type="getModelTagType(generatedComment.ai_model)" size="small">
              {{ getModelLabel(generatedComment.ai_model) }}
            </el-tag>
          </div>
        </template>
        <div class="result-content">
          {{ generatedComment.generated_comment || generatedComment.comment }}
        </div>
        <template #footer>
          <div class="result-footer">
            <el-button
              type="primary"
              :icon="CopyDocument"
              @click="copyToClipboard(generatedComment.generated_comment || generatedComment.comment)"
            >
              复制评语
            </el-button>
          </div>
        </template>
      </el-card>

      <!-- 历史记录 -->
      <div class="history-section">
        <div class="section-header">
          <h2>历史记录</h2>
          <el-button
            type="primary"
            size="small"
            :icon="Refresh"
            :loading="loadingHistory"
            @click="loadHistory"
          >
            刷新
          </el-button>
        </div>

        <div v-if="loadingHistory && comments.length === 0" class="loading-state">
          <el-skeleton :rows="3" animated />
        </div>

        <div v-else-if="comments.length === 0" class="empty-state">
          <el-empty description="暂无历史记录" />
        </div>

        <div v-else class="comments-list">
          <CommentCard
            v-for="comment in comments"
            :key="comment.id"
            :comment="comment"
            @copy="handleCopyComment"
            @delete="handleDeleteComment"
          />
        </div>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { CopyDocument, Refresh } from '@element-plus/icons-vue';
import { ElMessageBox } from 'element-plus';
import CommentForm from '../components/CommentForm.vue';
import CommentCard from '../components/CommentCard.vue';
import { useAuth } from '../composables/useAuth';
import { useMessage } from '../composables/useMessage';
import { generateComment, getCommentHistory, deleteComment } from '../services/comment';
import { AI_MODELS } from '../utils/config';

const { getCurrentUser, logout } = useAuth();
const { showSuccess, showError } = useMessage();

const currentUser = getCurrentUser();
const commentFormRef = ref(null);
const generating = ref(false);
const loadingHistory = ref(false);
const generatedComment = ref(null);
const comments = ref([]);

// 获取模型标签
const getModelLabel = (modelValue) => {
  const model = AI_MODELS.find((m) => m.value === modelValue);
  return model ? model.label : modelValue;
};

const getModelTagType = (modelValue) => {
  const types = {
    deepseek: 'success',
    zhipu: 'primary',
    qwen: 'warning',
    kimi: 'info',
  };
  return types[modelValue] || 'info';
};

// 生成评语
const handleGenerateComment = async (formData) => {
  generating.value = true;
  generatedComment.value = null;

  try {
    const response = await generateComment(formData);
    const data = response.data;

    if (data.success) {
      // 构造完整的评语对象，与历史记录格式一致
      generatedComment.value = {
        id: data.comment_id,
        generated_comment: data.comment,
        ai_model: formData.ai_model,
        student_name: formData.student_name,
        created_at: new Date().toISOString()
      };
      showSuccess('评语生成成功！');
      // 刷新历史记录
      await loadHistory();
      // 重置表单
      if (commentFormRef.value) {
        commentFormRef.value.resetForm();
      }
    } else {
      showError(data.message || '评语生成失败');
    }
  } catch (error) {
    console.error('生成评语错误:', error);
    showError(error.response?.data?.message || '评语生成失败，请检查网络连接');
  } finally {
    generating.value = false;
  }
};

// 加载历史记录
const loadHistory = async () => {
  loadingHistory.value = true;

  try {
    const response = await getCommentHistory(50);
    const data = response.data;

    if (data.success) {
      comments.value = data.comments || [];
    } else {
      showError(data.message || '加载历史记录失败');
    }
  } catch (error) {
    console.error('加载历史记录错误:', error);
    showError('加载历史记录失败，请检查网络连接');
  } finally {
    loadingHistory.value = false;
  }
};

// 复制到剪贴板
const copyToClipboard = async (text) => {
  try {
    await navigator.clipboard.writeText(text);
    showSuccess('已复制到剪贴板');
  } catch (error) {
    console.error('复制失败:', error);
    showError('复制失败，请手动复制');
  }
};

// 处理复制评语
const handleCopyComment = (comment) => {
  copyToClipboard(comment.generated_comment);
};

// 处理删除评语
const handleDeleteComment = async (comment) => {
  try {
    await ElMessageBox.confirm(
      '确定要删除这条评语吗？',
      '确认删除',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
    );

    const response = await deleteComment(comment.id);
    const data = response.data;

    if (data.success) {
      showSuccess('删除成功');
      // 从列表中移除
      comments.value = comments.value.filter((c) => c.id !== comment.id);
      // 如果删除的是当前显示的生成结果，清除它
      if (generatedComment.value && generatedComment.value.id === comment.id) {
        generatedComment.value = null;
      }
    } else {
      showError(data.message || '删除失败');
    }
  } catch (error) {
    if (error !== 'cancel') {
      console.error('删除评语错误:', error);
      showError(error.response?.data?.message || '删除失败，请检查网络连接');
    }
  }
};

// 退出登录
const handleLogout = () => {
  logout();
};

// 页面加载时获取历史记录
onMounted(() => {
  loadHistory();
});
</script>

<style scoped>
.home-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
}

.main-card {
  max-width: 900px;
  margin: 0 auto;
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding-bottom: 20px;
  border-bottom: 2px solid #f0f0f0;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 20px;
}

.header h1 {
  margin: 0;
  color: #333;
  font-size: 28px;
}

.user-info {
  color: #666;
  font-size: 14px;
}

.result-card {
  margin-bottom: 30px;
  background: #f0f7ff;
  border: 2px solid #409eff;
}

.result-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.result-header h3 {
  margin: 0;
  color: #333;
  font-size: 18px;
}

.result-content {
  color: #333;
  line-height: 1.8;
  font-size: 15px;
  padding: 20px;
  background: white;
  border-radius: 8px;
  white-space: pre-wrap;
}

.result-footer {
  display: flex;
  justify-content: flex-end;
}

.history-section {
  margin-top: 30px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.section-header h2 {
  margin: 0;
  color: #333;
  font-size: 20px;
}

.loading-state {
  padding: 20px;
}

.empty-state {
  padding: 40px 20px;
  text-align: center;
}

.comments-list {
  max-height: 600px;
  overflow-y: auto;
}

/* 滚动条样式 */
.comments-list::-webkit-scrollbar {
  width: 8px;
}

.comments-list::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

.comments-list::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 4px;
}

.comments-list::-webkit-scrollbar-thumb:hover {
  background: #555;
}

@media (max-width: 768px) {
  .header {
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
  }

  .header-left {
    flex-direction: column;
    align-items: flex-start;
    gap: 10px;
  }
}
</style>
