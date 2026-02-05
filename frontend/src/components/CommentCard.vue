<template>
  <el-card class="comment-card" shadow="hover">
    <div class="card-header">
      <div class="card-title-section">
        <span class="card-title">{{ comment.student_name }}</span>
        <el-tag :type="getModelTagType(comment.ai_model)" size="small">
          {{ getModelLabel(comment.ai_model) }}
        </el-tag>
      </div>
      <span class="card-meta">{{ formatDate(comment.created_at) }}</span>
    </div>

    <div class="card-content">
      {{ comment.generated_comment }}
    </div>

    <div class="card-footer">
      <el-button
        type="primary"
        size="small"
        :icon="CopyDocument"
        @click="handleCopy"
      >
        复制
      </el-button>
      <el-button
        type="danger"
        size="small"
        :icon="Delete"
        @click="handleDelete"
      >
        删除
      </el-button>
    </div>
  </el-card>
</template>

<script setup>
import { CopyDocument, Delete } from '@element-plus/icons-vue';
import { AI_MODELS } from '../utils/config';

const props = defineProps({
  comment: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(['copy', 'delete']);

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

const formatDate = (dateString) => {
  const date = new Date(dateString);
  const now = new Date();
  const diff = now - date;
  const seconds = Math.floor(diff / 1000);
  const minutes = Math.floor(seconds / 60);
  const hours = Math.floor(minutes / 60);
  const days = Math.floor(hours / 24);

  if (days > 0) {
    return `${days} 天前`;
  } else if (hours > 0) {
    return `${hours} 小时前`;
  } else if (minutes > 0) {
    return `${minutes} 分钟前`;
  } else {
    return '刚刚';
  }
};

const handleCopy = () => {
  emit('copy', props.comment);
};

const handleDelete = () => {
  emit('delete', props.comment);
};
</script>

<style scoped>
.comment-card {
  margin-bottom: 15px;
  transition: all 0.3s ease;
}

.comment-card:hover {
  transform: translateY(-2px);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.card-title-section {
  display: flex;
  align-items: center;
  gap: 10px;
}

.card-title {
  font-weight: 600;
  color: #333;
  font-size: 16px;
}

.card-meta {
  font-size: 12px;
  color: #999;
}

.card-content {
  color: #666;
  line-height: 1.8;
  font-size: 14px;
  margin-bottom: 15px;
  padding: 15px;
  background: #f9f9f9;
  border-radius: 8px;
}

.card-footer {
  display: flex;
  gap: 10px;
  padding-top: 15px;
  border-top: 1px solid #f0f0f0;
}
</style>
