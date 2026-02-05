# Vercel 部署指南

## 部署前准备

### 1. 后端部署（必须先完成）

前端需要连接到后端 API，所以必须先部署后端。推荐使用以下平台：

#### 选项 A: Railway（推荐）
1. 访问 https://railway.app/
2. 使用 GitHub 登录
3. 创建新项目，选择 "Deploy from GitHub repo"
4. 选择你的 CommentGenie 仓库
5. 配置环境变量（在 Railway 项目设置中）：
   ```
   DEEPSEEK_API_KEY=你的密钥
   ZHIPU_API_KEY=你的密钥
   QWEN_API_KEY=你的密钥
   KIMI_API_KEY=你的密钥
   JWT_SECRET_KEY=随机生成的密钥
   PORT=5000
   ```
6. 部署完成后，获取后端 URL（例如：https://your-app.railway.app）

#### 选项 B: Render
1. 访问 https://render.com/
2. 创建新的 Web Service
3. 连接 GitHub 仓库
4. 配置：
   - Build Command: `cd backend && pip install -r requirements.txt`
   - Start Command: `cd backend && python app.py`
5. 添加环境变量（同上）
6. 获取后端 URL

### 2. 更新前端配置

获得后端 URL 后，更新前端生产环境配置：

```bash
# 编辑 frontend/.env.production
VITE_API_BASE_URL=https://your-backend-url.railway.app
```

**重要**: 将 `https://your-backend-url.railway.app` 替换为你的实际后端 URL。

### 3. 更新后端 CORS 配置

编辑 `backend/app.py`，更新 CORS 配置以允许 Vercel 域名：

```python
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:3000",  # 开发环境
            "https://your-app.vercel.app",  # 生产环境
            "https://*.vercel.app"  # 允许所有 Vercel 预览部署
        ],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})
```

## 推送到 GitHub

### 1. 添加所有文件

```bash
cd /d/Projects/CommentGenie

# 添加新的 Vue 前端文件
git add frontend/

# 添加文档
git add MIGRATION_SUMMARY.md QUICK_START.md DEPLOYMENT_GUIDE_VERCEL.md

# 添加更新的配置
git add vercel.json .gitignore

# 删除旧的静态文件（已备份到 frontend_backup）
git rm -r frontend/css frontend/js
git rm frontend/login.html frontend/register.html frontend/test.html frontend/hello.html frontend/vercel.json
```

### 2. 提交更改

```bash
git commit -m "Migrate to Vue 3 + Vite + Element Plus

- Convert from static HTML to Vue 3 SPA
- Add Element Plus UI components
- Implement Vue Router for navigation
- Add Axios for API calls
- Create composables for auth and messages
- Update Vercel deployment configuration
- All features migrated and tested"
```

### 3. 推送到 GitHub

```bash
git push origin master
```

## Vercel 部署

### 方式 1: 自动部署（推荐）

如果你的 Vercel 项目已经连接到 GitHub：

1. 推送代码后，Vercel 会自动检测到更改
2. 自动开始构建和部署
3. 等待几分钟，部署完成

### 方式 2: 手动连接

如果还没有连接 Vercel：

1. 访问 https://vercel.com/
2. 使用 GitHub 登录
3. 点击 "Add New Project"
4. 选择 CommentGenie 仓库
5. Vercel 会自动检测到 `vercel.json` 配置
6. 点击 "Deploy"

### 配置环境变量（可选）

如果需要在 Vercel 上配置环境变量：

1. 进入项目设置 (Settings)
2. 选择 "Environment Variables"
3. 添加：
   ```
   VITE_API_BASE_URL = https://your-backend-url.railway.app
   ```

**注意**: 如果你已经在 `frontend/.env.production` 中配置了，就不需要在 Vercel 上再配置。

## 验证部署

### 1. 检查构建日志

在 Vercel 部署页面查看构建日志，确保：
- ✅ 依赖安装成功
- ✅ 构建完成（`npm run build`）
- ✅ 没有错误

### 2. 测试应用

访问 Vercel 提供的 URL（例如：https://your-app.vercel.app）：

1. **测试注册**: 创建新账号
2. **测试登录**: 使用新账号登录
3. **测试生成**: 生成学生评语
4. **测试历史**: 查看历史记录
5. **测试功能**: 复制、删除、刷新

### 3. 检查 API 连接

打开浏览器开发者工具 (F12)：
- 查看 Network 标签
- 确认 API 请求发送到正确的后端 URL
- 检查是否有 CORS 错误

## 常见问题

### 问题 1: 前端无法连接后端

**症状**: 页面加载但无法登录或生成评语

**解决方案**:
1. 检查 `frontend/.env.production` 中的 API URL 是否正确
2. 检查后端 CORS 配置是否包含 Vercel 域名
3. 确认后端服务正在运行

### 问题 2: 构建失败

**症状**: Vercel 构建过程中出错

**解决方案**:
1. 检查 `package.json` 是否正确
2. 确认所有依赖都已安装
3. 查看构建日志中的具体错误信息

### 问题 3: 404 错误

**症状**: 刷新页面或直接访问路由时出现 404

**解决方案**:
- 确认 `vercel.json` 中有 rewrites 配置（已配置）
- 这会将所有请求重定向到 index.html（SPA 模式）

### 问题 4: 环境变量未生效

**症状**: 前端使用了错误的 API URL

**解决方案**:
1. 确认 `.env.production` 文件已提交到 Git
2. 重新部署项目
3. 清除浏览器缓存

## 更新部署

每次代码更新后：

```bash
# 1. 提交更改
git add .
git commit -m "描述你的更改"

# 2. 推送到 GitHub
git push origin master

# 3. Vercel 会自动重新部署
```

## 回滚

如果新部署有问题：

1. 在 Vercel 项目页面
2. 找到之前的成功部署
3. 点击 "Promote to Production"

## 监控

### Vercel Analytics（可选）

1. 在项目设置中启用 Analytics
2. 查看访问量、性能指标等

### 后端监控

- Railway/Render 提供日志查看
- 可以看到 API 请求和错误

## 成本

- **Vercel**: 免费套餐足够个人项目使用
- **Railway**: 免费 $5/月额度，通常够用
- **Render**: 免费套餐（但会休眠，需要时间唤醒）

## 安全建议

1. ✅ 不要提交 `backend/.env` 文件（包含 API 密钥）
2. ✅ 使用强密码作为 JWT_SECRET_KEY
3. ✅ 定期更新依赖包
4. ✅ 在生产环境关闭 Flask debug 模式
5. ✅ 使用 HTTPS（Vercel 和 Railway 自动提供）

## 下一步

部署成功后，你可以：

1. 配置自定义域名
2. 添加 Google Analytics
3. 优化性能（代码分割、懒加载）
4. 添加更多功能

祝部署顺利！
