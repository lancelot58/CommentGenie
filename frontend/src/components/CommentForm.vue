<template>
  <el-card class="comment-form-card">
    <template #header>
      <h2>生成评语</h2>
    </template>

    <el-form
      ref="formRef"
      :model="form"
      :rules="rules"
      label-width="100px"
    >
      <el-form-item label="学生姓名" prop="studentName">
        <el-input
          v-model="form.studentName"
          placeholder="请输入学生姓名"
          clearable
        />
      </el-form-item>

      <el-form-item label="学生情况" prop="studentInfo">
        <el-input
          v-model="form.studentInfo"
          type="textarea"
          :rows="5"
          placeholder="请描述学生的学习情况、性格特点、优点缺点等..."
          clearable
        />
      </el-form-item>

      <el-form-item label="AI 模型" prop="aiModel">
        <el-select
          v-model="form.aiModel"
          placeholder="请选择 AI 模型"
          style="width: 100%"
        >
          <el-option
            v-for="model in aiModels"
            :key="model.value"
            :label="model.label"
            :value="model.value"
          />
        </el-select>
      </el-form-item>

      <el-form-item>
        <el-button
          type="primary"
          :loading="loading"
          style="width: 100%"
          @click="handleSubmit"
        >
          {{ loading ? '生成中...' : '生成评语' }}
        </el-button>
      </el-form-item>
    </el-form>
  </el-card>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { AI_MODELS } from '../utils/config';

const props = defineProps({
  loading: {
    type: Boolean,
    default: false,
  },
});

const emit = defineEmits(['submit']);

const formRef = ref(null);
const form = reactive({
  studentName: '',
  studentInfo: '',
  aiModel: 'deepseek',
});

const aiModels = AI_MODELS;

const rules = {
  studentName: [
    { required: true, message: '请输入学生姓名', trigger: 'blur' },
  ],
  studentInfo: [
    { required: true, message: '请描述学生情况', trigger: 'blur' },
    { min: 10, message: '请至少输入 10 个字符', trigger: 'blur' },
  ],
  aiModel: [
    { required: true, message: '请选择 AI 模型', trigger: 'change' },
  ],
};

const handleSubmit = async () => {
  if (!formRef.value) return;

  await formRef.value.validate((valid) => {
    if (valid) {
      emit('submit', {
        student_name: form.studentName,
        student_info: form.studentInfo,
        ai_model: form.aiModel,
      });
    }
  });
};

// 重置表单
const resetForm = () => {
  if (formRef.value) {
    formRef.value.resetFields();
  }
};

// 暴露方法给父组件
defineExpose({
  resetForm,
});
</script>

<style scoped>
.comment-form-card {
  margin-bottom: 30px;
}

h2 {
  margin: 0;
  color: #333;
  font-size: 20px;
}
</style>
