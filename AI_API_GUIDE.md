# AI API 申请和配置指南

## 📝 概述

本项目支持多个国内主流 AI API，你可以选择其中一个或多个进行配置。

---

## 🤖 支持的 AI 模型

### 1. DeepSeek（推荐）

**优点**：
- 性价比极高
- API 简单易用
- 响应速度快
- 中文能力强

**申请步骤**：
1. 访问：https://platform.deepseek.com/
2. 注册账号（支持手机号/邮箱）
3. 进入控制台
4. 点击"API Keys"
5. 创建新的 API Key
6. 复制 API Key（格式：sk-xxxxxxxx）

**价格**：
- 输入：¥1/百万 tokens
- 输出：¥2/百万 tokens
- 新用户有免费额度

---

### 2. 智谱 AI（GLM-4）

**优点**：
- 清华大学出品
- 中文理解能力优秀
- 有免费额度
- 稳定可靠

**申请步骤**：
1. 访问：https://open.bigmodel.cn/
2. 注册账号
3. 实名认证（需要）
4. 进入控制台
5. 创建 API Key
6. 复制 API Key

**价格**：
- GLM-4：¥100/百万 tokens
- 新用户赠送 1800 万 tokens（约 18 元）

---

### 3. 通义千问（Qwen）

**优点**：
- 阿里云出品
- 稳定性好
- 有免费额度
- 支持多种模型

**申请步骤**：
1. 访问：https://dashscope.aliyun.com/
2. 使用阿里云账号登录（没有则注册）
3. 开通 DashScope 服务
4. 进入控制台
5. 创建 API Key
6. 复制 API Key

**价格**：
- qwen-turbo：¥2/百万 tokens
- 新用户有免费额度

---

### 4. Kimi（月之暗面）

**优点**：
- 长文本处理能力强
- 上下文窗口大
- 响应质量高

**申请步骤**：
1. 访问：https://platform.moonshot.cn/
2. 注册账号
3. 进入控制台
4. 创建 API Key
5. 复制 API Key

**价格**：
- moonshot-v1-8k：¥12/百万 tokens
- 新用户有免费额度

---

## ⚙️ 配置步骤

### 1. 创建 .env 文件

在 `backend` 目录下，复制 `.env.example` 为 `.env`：

```bash
cd backend
copy .env.example .env    # Windows
# 或
cp .env.example .env      # Mac/Linux
```

### 2. 填入 API Key

打开 `.env` 文件，填入你申请到的 API Key：

```env
# 至少配置一个 AI API
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
ZHIPU_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxx
QWEN_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
KIMI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx

# JWT 密钥（随机字符串，用于加密）
JWT_SECRET_KEY=your-random-secret-key-here

# 数据库配置
DATABASE_PATH=database.db

# 服务器配置
FLASK_ENV=development
PORT=5000
```

**重要提示**：
- ⚠️ `.env` 文件包含敏感信息，不要上传到 Git
- ⚠️ 至少配置一个 AI API Key
- ⚠️ JWT_SECRET_KEY 要改成随机字符串

### 3. 生成随机密钥

JWT_SECRET_KEY 可以用以下方式生成：

**Python**：
```python
import secrets
print(secrets.token_hex(32))
```

**在线生成**：
- https://randomkeygen.com/

---

## 🧪 测试 AI API

### 方法1：使用测试脚本

```bash
cd backend
python utils/ai_client.py
```

这会测试你配置的 AI API 是否正常工作。

### 方法2：使用 API 接口

启动服务器后，调用评语生成接口：

```bash
# 使用 DeepSeek
curl -X POST http://localhost:5000/api/comment/generate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <你的token>" \
  -d '{
    "student_name": "张三",
    "student_info": "性格开朗，成绩优秀",
    "ai_model": "deepseek"
  }'

# 使用智谱 AI
curl -X POST http://localhost:5000/api/comment/generate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <你的token>" \
  -d '{
    "student_name": "张三",
    "student_info": "性格开朗，成绩优秀",
    "ai_model": "zhipu"
  }'
```

---

## 💡 使用建议

### 选择哪个 AI？

**学习和测试**：
- 推荐 **DeepSeek**（性价比最高，免费额度多）
- 或 **智谱 AI**（免费额度大）

**生产环境**：
- 如果预算有限：**DeepSeek**
- 如果追求稳定：**通义千问**（阿里云）
- 如果需要长文本：**Kimi**

### 成本估算

以生成 1000 条评语为例（每条约 200 字）：

| AI 模型 | 预计成本 |
|---------|----------|
| DeepSeek | ¥0.05 |
| 智谱 GLM-4 | ¥0.50 |
| 通义千问 | ¥0.10 |
| Kimi | ¥0.60 |

**结论**：DeepSeek 最便宜，适合学习和小规模使用。

---

## 🔧 常见问题

### 1. API Key 无效

**错误信息**：`401 Unauthorized` 或 `Invalid API Key`

**解决方法**：
- 检查 API Key 是否正确复制（没有多余空格）
- 确认 API Key 是否已激活
- 检查账户余额是否充足

### 2. 请求超时

**错误信息**：`Timeout` 或 `Connection Error`

**解决方法**：
- 检查网络连接
- 增加超时时间（在 `ai_client.py` 中修改 `timeout` 参数）
- 尝试切换其他 AI 模型

### 3. 未配置 API Key

**错误信息**：`未配置 xxx 的 API Key`

**解决方法**：
- 确认 `.env` 文件存在
- 检查 `.env` 文件中是否填入了 API Key
- 重启服务器（修改 `.env` 后需要重启）

### 4. 生成的评语质量不好

**解决方法**：
- 提供更详细的学生信息
- 尝试不同的 AI 模型
- 修改提示词（在 `ai_client.py` 中的 `prompt` 变量）

---

## 📚 API 文档

### DeepSeek
- 官方文档：https://platform.deepseek.com/docs

### 智谱 AI
- 官方文档：https://open.bigmodel.cn/dev/api

### 通义千问
- 官方文档：https://help.aliyun.com/zh/dashscope/

### Kimi
- 官方文档：https://platform.moonshot.cn/docs

---

## 🎯 下一步

配置完成后，你可以：
1. 测试 AI API 是否正常工作
2. 开始开发前端页面
3. 进行完整的前后端联调

有问题随时问我！
