# Vercel + Railway 部署指南

## 📋 部署架构

```
GitHub 仓库
    ↓
    ├─→ Vercel (自动部署前端)
    └─→ Railway (自动部署后端)
```

**优势**：
- ✅ 推送到 GitHub 后自动部署
- ✅ 前后端独立部署
- ✅ 环境变量安全管理
- ✅ 完全免费（有使用限制）

---

## 🚀 第一步：准备 GitHub 仓库

### 1. 确保 .gitignore 正确配置

检查项目根目录的 `.gitignore` 文件：

```gitignore
# 环境变量（敏感信息）
.env
*.env
!.env.example

# 数据库
*.db
*.sqlite

# Python
__pycache__/
*.py[cod]
venv/
env/

# 前端
node_modules/
.DS_Store
```

### 2. 初始化 Git 仓库（如果还没有）

```bash
cd C:\Users\admin\Desktop\EduDemo

# 初始化 Git
git init

# 添加所有文件
git add .

# 创建第一次提交
git commit -m "Initial commit: Student comment generator"
```

### 3. 创建 GitHub 仓库

1. 访问：https://github.com/new
2. 仓库名称：`EduDemo` 或 `student-comment-generator`
3. 选择 Public 或 Private
4. **不要**勾选 "Initialize with README"（我们已经有了）
5. 点击 "Create repository"

### 4. 推送到 GitHub

```bash
# 关联远程仓库（替换为你的 GitHub 用户名）
git remote add origin https://github.com/你的用户名/EduDemo.git

# 推送代码
git branch -M main
git push -u origin main
```

---

## 🎨 第二步：部署前端到 Vercel

### 1. 注册 Vercel

1. 访问：https://vercel.com/
2. 点击 "Sign Up"
3. 选择 "Continue with GitHub"
4. 授权 Vercel 访问你的 GitHub

### 2. 导入项目

1. 点击 "Add New..." → "Project"
2. 选择你的 `EduDemo` 仓库
3. 点击 "Import"

### 3. 配置项目

**Framework Preset**: Other

**Root Directory**: 点击 "Edit"，选择 `frontend`

**Build Settings**:
- Build Command: (留空)
- Output Directory: (留空)
- Install Command: (留空)

### 4. 部署

点击 "Deploy"，等待部署完成（约 1-2 分钟）

### 5. 获取前端地址

部署成功后，你会得到一个地址，例如：
```
https://edu-demo-xxx.vercel.app
```

**重要**：复制这个地址，后面需要用到。

---

## 🔧 第三步：部署后端到 Railway

### 1. 注册 Railway

1. 访问：https://railway.app/
2. 点击 "Login"
3. 选择 "Login with GitHub"
4. 授权 Railway 访问你的 GitHub

### 2. 创建新项目

1. 点击 "New Project"
2. 选择 "Deploy from GitHub repo"
3. 选择你的 `EduDemo` 仓库
4. Railway 会自动检测到 Python 项目

### 3. 配置环境变量

在 Railway 项目页面：

1. 点击你的服务（service）
2. 点击 "Variables" 标签
3. 点击 "New Variable"
4. 添加以下环境变量：

```
DEEPSEEK_API_KEY=sk-你的DeepSeek密钥
ZHIPU_API_KEY=你的智谱AI密钥
JWT_SECRET_KEY=你的随机密钥（至少32位）
DATABASE_PATH=database.db
FLASK_ENV=production
PORT=5000
```

**生成随机密钥**：
```python
import secrets
print(secrets.token_hex(32))
```

### 4. 配置部署文件

在项目根目录创建 `Procfile`：

```bash
web: cd backend && python app.py
```

在项目根目录创建 `runtime.txt`：

```
python-3.11.0
```

确保根目录有 `requirements.txt`（复制 backend 目录的）：

```bash
# 在项目根目录
copy backend\requirements.txt requirements.txt
```

### 5. 修改后端代码以适应生产环境

编辑 `backend/app.py`，修改最后的启动部分：

```python
if __name__ == '__main__':
    # 获取端口号（Railway 会自动设置）
    port = int(os.getenv('PORT', 5000))

    # 判断是否为生产环境
    is_production = os.getenv('FLASK_ENV') == 'production'

    print("=" * 50)
    print("学生评语生成器 API 服务器")
    print(f"环境: {'生产' if is_production else '开发'}")
    print("=" * 50)

    app.run(
        host='0.0.0.0',
        port=port,
        debug=not is_production  # 生产环境关闭 debug
    )
```

### 6. 修改 CORS 配置

编辑 `backend/app.py`，找到 CORS 配置部分：

```python
# 获取允许的前端域名
FRONTEND_URL = os.getenv('FRONTEND_URL', '*')

# 配置 CORS
CORS(app, resources={
    r"/api/*": {
        "origins": FRONTEND_URL if FRONTEND_URL != '*' else "*",
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})
```

在 Railway 环境变量中添加：
```
FRONTEND_URL=https://你的vercel地址.vercel.app
```

### 7. 推送更新到 GitHub

```bash
git add .
git commit -m "Add deployment configuration for Railway"
git push
```

Railway 会自动检测到更新并重新部署。

### 8. 获取后端地址

1. 在 Railway 项目页面，点击 "Settings"
2. 找到 "Domains" 部分
3. 点击 "Generate Domain"
4. 复制生成的域名，例如：`your-app.railway.app`

---

## 🔗 第四步：连接前后端

### 1. 更新前端配置

编辑 `frontend/js/config.js`：

```javascript
// 生产环境使用 Railway 的后端地址
const API_BASE_URL = 'https://your-app.railway.app';

// 如果需要区分开发和生产环境
// const API_BASE_URL = window.location.hostname === 'localhost'
//     ? 'http://localhost:5000'
//     : 'https://your-app.railway.app';
```

### 2. 推送更新

```bash
git add frontend/js/config.js
git commit -m "Update API URL for production"
git push
```

Vercel 会自动重新部署前端。

---

## ✅ 第五步：验证部署

### 1. 测试后端

访问：`https://your-app.railway.app/`

应该看到：
```json
{
  "message": "学生评语生成器 API",
  "version": "1.0.0",
  "status": "running"
}
```

### 2. 测试前端

访问：`https://your-vercel-app.vercel.app/login.html`

- 尝试注册新账号
- 尝试登录
- 尝试生成评语

---

## 🔄 日常开发流程

### 本地开发

1. 修改代码
2. 本地测试（使用本地 .env 配置）
3. 确认功能正常

### 推送到生产环境

```bash
# 添加修改
git add .

# 提交
git commit -m "描述你的修改"

# 推送到 GitHub
git push
```

**自动部署**：
- Vercel 自动部署前端（约 1 分钟）
- Railway 自动部署后端（约 2-3 分钟）

### 查看部署状态

**Vercel**：
- 访问：https://vercel.com/dashboard
- 查看部署历史和日志

**Railway**：
- 访问：https://railway.app/dashboard
- 查看部署日志和状态

---

## 🔐 环境变量管理最佳实践

### 本地开发

```bash
# .env (不提交到 Git)
DEEPSEEK_API_KEY=sk-本地测试密钥
JWT_SECRET_KEY=本地开发密钥
```

### 生产环境

在 Railway 平台配置：
```
DEEPSEEK_API_KEY=sk-生产环境密钥
JWT_SECRET_KEY=生产环境随机密钥（更安全）
```

### 安全建议

1. **不同环境使用不同的密钥**
   - 开发环境：测试密钥
   - 生产环境：正式密钥

2. **定期轮换密钥**
   - JWT_SECRET_KEY 定期更换
   - AI API Key 定期检查使用情况

3. **最小权限原则**
   - 只给必要的权限
   - 不要在前端暴露 API Key

---

## 📊 部署架构图

```
开发者本地
    ↓ (git push)
GitHub 仓库
    ↓ (webhook)
    ├─→ Vercel
    │   └─→ 前端静态文件
    │       └─→ 用户浏览器
    │
    └─→ Railway
        └─→ Flask 后端
            ├─→ AI API (DeepSeek等)
            └─→ SQLite 数据库
```

---

## 🐛 常见问题

### 1. 推送后没有自动部署

**检查**：
- GitHub webhook 是否正确配置
- 查看 Vercel/Railway 的部署日志
- 确认推送到了正确的分支（main）

### 2. 前端无法连接后端

**检查**：
- `config.js` 中的 API 地址是否正确
- Railway 后端是否正常运行
- CORS 配置是否正确

### 3. 环境变量不生效

**解决**：
- 在 Railway 中重新配置环境变量
- 点击 "Redeploy" 重新部署
- 检查变量名是否正确（区分大小写）

### 4. 数据库数据丢失

**原因**：Railway 免费版重启会清空数据

**解决方案**：
- 升级到付费版（持久化存储）
- 或使用外部数据库（如 PlanetScale）
- 或定期备份数据

---

## 💰 成本估算

### 免费额度

**Vercel**：
- 100 GB 带宽/月
- 无限部署次数
- 适合个人项目

**Railway**：
- $5 免费额度/月
- 约 500 小时运行时间
- 适合小型项目

### 超出免费额度

- Vercel Pro: $20/月
- Railway: 按使用量计费

---

## 🎉 完成！

现在你有了一个完整的自动化部署流程：

1. ✅ 本地开发和测试
2. ✅ 推送到 GitHub
3. ✅ 自动部署到 Vercel（前端）
4. ✅ 自动部署到 Railway（后端）
5. ✅ 环境变量安全管理
6. ✅ 生产环境正常运行

**访问地址**：
- 前端：`https://your-app.vercel.app`
- 后端：`https://your-app.railway.app`

**分享给朋友**：
- 直接发送前端地址
- 他们可以注册并使用

---

## 📚 相关文档

- Vercel 文档：https://vercel.com/docs
- Railway 文档：https://docs.railway.app/
- GitHub Actions：https://docs.github.com/actions
