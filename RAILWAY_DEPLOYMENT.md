# Railway 后端部署指南

## 步骤 1: 访问 Railway

1. 打开浏览器，访问 https://railway.app/
2. 点击 "Start a New Project"
3. 使用 GitHub 账号登录

## 步骤 2: 创建新项目

1. 点击 "Deploy from GitHub repo"
2. 如果是第一次使用，需要授权 Railway 访问你的 GitHub
3. 选择 **CommentGenie** 仓库
4. Railway 会自动检测到这是一个 Python 项目

## 步骤 3: 配置项目

### 3.1 设置根目录

1. 在项目设置中，找到 "Root Directory"
2. 设置为: `backend`
3. 这样 Railway 就知道从 backend 目录部署

### 3.2 配置环境变量

点击项目 → Settings → Variables，添加以下环境变量：

**必需的环境变量**:

```
DEEPSEEK_API_KEY=你的DeepSeek密钥
ZHIPU_API_KEY=你的智谱AI密钥
QWEN_API_KEY=你的通义千问密钥
KIMI_API_KEY=你的Kimi密钥
JWT_SECRET_KEY=随机生成的强密码（至少32位）
FLASK_ENV=production
PORT=5000
```

**如何获取 API 密钥**:

- **DeepSeek**: https://platform.deepseek.com/
- **智谱 AI**: https://open.bigmodel.cn/
- **通义千问**: https://dashscope.aliyun.com/
- **Kimi**: https://platform.moonshot.cn/

**生成 JWT_SECRET_KEY**:
```bash
# 在本地运行这个命令生成随机密钥
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 3.3 配置数据库（可选）

Railway 提供 PostgreSQL 数据库，但我们当前使用 SQLite。
如果需要持久化数据，建议：

1. 添加 Railway PostgreSQL 插件
2. 或使用 Railway Volumes 持久化 SQLite 文件

**当前配置**: SQLite 数据库会在每次重新部署时重置。

## 步骤 4: 部署

1. 配置完成后，Railway 会自动开始部署
2. 等待 3-5 分钟
3. 查看部署日志，确保没有错误

## 步骤 5: 获取后端 URL

1. 部署成功后，在项目页面找到 "Settings"
2. 找到 "Domains" 部分
3. 点击 "Generate Domain"
4. 复制生成的 URL（例如：`https://commentgenie-production.up.railway.app`）

## 步骤 6: 测试后端

在浏览器中访问你的后端 URL：

```
https://your-app.railway.app/
```

应该看到：
```json
{
  "message": "学生评语生成器 API",
  "status": "running",
  "version": "1.0.0"
}
```

## 步骤 7: 更新前端配置

获得后端 URL 后，更新前端配置：

```bash
# 编辑 frontend/.env.production
VITE_API_BASE_URL=https://your-app.railway.app
```

然后提交并推送：
```bash
git add frontend/.env.production
git commit -m "Update production API URL"
git push origin master
```

## 步骤 8: 更新 CORS 配置

编辑 `backend/app.py`，更新 CORS 配置：

```python
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:3000",  # 开发环境
            "https://your-app.vercel.app",  # 你的 Vercel 域名
            "https://*.vercel.app"  # 所有 Vercel 预览部署
        ],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})
```

提交并推送：
```bash
git add backend/app.py
git commit -m "Update CORS configuration for production"
git push origin master
```

Railway 会自动重新部署。

## 监控和日志

### 查看日志

1. 在 Railway 项目页面
2. 点击 "Deployments"
3. 选择最新的部署
4. 查看实时日志

### 常见日志信息

- ✅ `学生评语生成器 API 服务器` - 服务器启动成功
- ✅ `环境: 生产环境` - 确认在生产模式
- ✅ `Running on http://0.0.0.0:5000` - 服务器运行中

## 常见问题

### 问题 1: 部署失败

**症状**: 部署过程中出错

**解决方案**:
1. 查看部署日志中的错误信息
2. 确认 `requirements.txt` 中的依赖都能安装
3. 确认 Python 版本兼容（使用 3.11）

### 问题 2: 环境变量未生效

**症状**: API 调用失败，提示未配置 API Key

**解决方案**:
1. 检查 Railway 项目设置中的环境变量
2. 确认变量名拼写正确
3. 重新部署项目

### 问题 3: 数据库重置

**症状**: 每次部署后用户数据丢失

**原因**: SQLite 文件存储在临时文件系统中

**解决方案**:
1. 使用 Railway PostgreSQL 插件
2. 或使用 Railway Volumes 持久化数据

### 问题 4: CORS 错误

**症状**: 前端无法连接后端

**解决方案**:
1. 确认 CORS 配置包含前端域名
2. 检查浏览器控制台的具体错误
3. 确认后端服务正在运行

## 成本

- **免费额度**: $5/月
- **通常使用**: 小型项目通常在免费额度内
- **超出后**: 按使用量计费

## 更新部署

每次推送代码到 GitHub 后：

1. Railway 会自动检测到更改
2. 自动重新部署
3. 等待几分钟即可

## 回滚

如果新部署有问题：

1. 在 Railway 项目页面
2. 找到 "Deployments"
3. 选择之前的成功部署
4. 点击 "Redeploy"

## 下一步

后端部署成功后：

1. ✅ 获取后端 URL
2. ✅ 更新前端 `.env.production`
3. ✅ 更新后端 CORS 配置
4. ✅ 部署前端到 Vercel

祝部署顺利！🚀
