# 互联网部署指南

## 📋 概述

本指南将教你如何将学生评语生成器部署到互联网上，让任何人都可以通过网址访问。

---

## 🎯 部署方案对比

| 平台 | 难度 | 费用 | 推荐度 | 说明 |
|------|------|------|--------|------|
| **Railway** | ⭐ | 免费 | ⭐⭐⭐⭐⭐ | 最推荐，简单快速 |
| **Render** | ⭐⭐ | 免费 | ⭐⭐⭐⭐ | 功能强大，稍复杂 |
| **PythonAnywhere** | ⭐⭐ | 免费/付费 | ⭐⭐⭐ | 专为 Python 设计 |
| **Vercel** | ⭐⭐⭐ | 免费 | ⭐⭐ | 适合前端，后端需改造 |
| **阿里云/腾讯云** | ⭐⭐⭐⭐ | 付费 | ⭐⭐⭐ | 需要备案，适合长期 |

**推荐**：初学者使用 **Railway**，简单快速，5分钟部署完成。

---

## 🚀 方案一：Railway 部署（推荐）

### 为什么选择 Railway？
- ✅ 完全免费（有使用限制）
- ✅ 无需信用卡
- ✅ 支持 GitHub 自动部署
- ✅ 自动配置 HTTPS
- ✅ 5分钟完成部署

### 步骤1：准备工作

#### 1.1 注册 GitHub 账号
1. 访问：https://github.com/
2. 点击 "Sign up" 注册
3. 验证邮箱

#### 1.2 创建 Git 仓库

**方法1：使用 GitHub Desktop（推荐小白）**

1. 下载 GitHub Desktop：https://desktop.github.com/
2. 安装并登录
3. 点击 "File" → "Add local repository"
4. 选择项目目录：`C:\Users\admin\Desktop\EduDemo`
5. 点击 "Publish repository"
6. 取消勾选 "Keep this code private"（或保持私有）
7. 点击 "Publish repository"

**方法2：使用命令行**

```bash
cd C:\Users\admin\Desktop\EduDemo

# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 创建第一次提交
git commit -m "Initial commit"

# 在 GitHub 上创建仓库后，关联远程仓库
git remote add origin https://github.com/你的用户名/EduDemo.git

# 推送到 GitHub
git push -u origin main
```

**重要**：确保 `.gitignore` 文件正确配置，不要上传敏感信息：
```
.env
*.db
__pycache__/
venv/
```

### 步骤2：注册 Railway

1. 访问：https://railway.app/
2. 点击 "Start a New Project"
3. 使用 GitHub 账号登录
4. 授权 Railway 访问你的 GitHub

### 步骤3：部署项目

1. 点击 "New Project"
2. 选择 "Deploy from GitHub repo"
3. 选择你的 `EduDemo` 仓库
4. Railway 会自动检测到 Python 项目

### 步骤4：配置环境变量

1. 在 Railway 项目页面，点击你的服务
2. 点击 "Variables" 标签
3. 添加以下环境变量：

```
DEEPSEEK_API_KEY=sk-你的密钥
ZHIPU_API_KEY=你的密钥
JWT_SECRET_KEY=随机字符串
DATABASE_PATH=database.db
FLASK_ENV=production
PORT=5000
```

### 步骤5：配置部署文件

在项目根目录创建以下文件：

#### `Procfile`（告诉 Railway 如何启动）
```
web: cd backend && python app.py
```

#### `runtime.txt`（指定 Python 版本）
```
python-3.11.0
```

#### `requirements.txt`（确保在根目录也有一份）
```bash
# 复制 backend/requirements.txt 到根目录
copy backend\requirements.txt requirements.txt
```

### 步骤6：修改后端代码

编辑 `backend/app.py`，修改最后的启动部分：

```python
if __name__ == '__main__':
    # 获取端口号（Railway 会自动设置 PORT 环境变量）
    port = int(os.getenv('PORT', 5000))

    print("=" * 50)
    print("学生评语生成器 API 服务器")
    print("=" * 50)
    print(f"服务器地址: http://0.0.0.0:{port}")
    print("=" * 50)

    # 生产环境配置
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False  # 生产环境关闭 debug
    )
```

### 步骤7：推送更新

```bash
git add .
git commit -m "Add Railway deployment config"
git push
```

Railway 会自动检测到更新并重新部署。

### 步骤8：获取访问地址

1. 在 Railway 项目页面，点击 "Settings"
2. 找到 "Domains" 部分
3. 点击 "Generate Domain"
4. 复制生成的域名，例如：`your-app.railway.app`

### 步骤9：配置前端

编辑 `frontend/js/config.js`：

```javascript
// 修改为 Railway 生成的域名
const API_BASE_URL = 'https://your-app.railway.app';
```

### 步骤10：部署前端

**方法1：使用 Vercel（推荐）**

1. 访问：https://vercel.com/
2. 使用 GitHub 登录
3. 点击 "New Project"
4. 选择你的仓库
5. 配置：
   - Framework Preset: Other
   - Root Directory: `frontend`
6. 点击 "Deploy"

**方法2：使用 GitHub Pages**

1. 在 GitHub 仓库页面，点击 "Settings"
2. 找到 "Pages" 部分
3. Source 选择 "main" 分支
4. Folder 选择 `/frontend`
5. 点击 "Save"
6. 等待几分钟，访问：`https://你的用户名.github.io/EduDemo/login.html`

---

## 🔧 方案二：Render 部署

### 步骤1：注册 Render

1. 访问：https://render.com/
2. 使用 GitHub 账号注册

### 步骤2：创建 Web Service

1. 点击 "New +" → "Web Service"
2. 连接你的 GitHub 仓库
3. 配置：
   - Name: `edudemo`
   - Environment: `Python 3`
   - Build Command: `cd backend && pip install -r requirements.txt`
   - Start Command: `cd backend && python app.py`

### 步骤3：添加环境变量

在 "Environment" 标签添加：
- `DEEPSEEK_API_KEY`
- `ZHIPU_API_KEY`
- `JWT_SECRET_KEY`
- `PORT=10000`

### 步骤4：部署

点击 "Create Web Service"，等待部署完成。

---

## 🐍 方案三：PythonAnywhere 部署

### 步骤1：注册账号

1. 访问：https://www.pythonanywhere.com/
2. 注册免费账号（Beginner）

### 步骤2：上传代码

1. 在 Dashboard 点击 "Files"
2. 上传项目文件，或使用 Git clone

### 步骤3：创建虚拟环境

在 "Consoles" 中打开 Bash：

```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
cd EduDemo/backend
pip install -r requirements.txt
```

### 步骤4：配置 Web App

1. 点击 "Web" 标签
2. 点击 "Add a new web app"
3. 选择 "Manual configuration"
4. 选择 Python 3.10
5. 配置 WSGI 文件（需要修改为 Flask 应用）

### 步骤5：设置环境变量

在 Web 标签的 "Environment variables" 部分添加配置。

---

## ☁️ 方案四：阿里云/腾讯云部署

### 适用场景
- 需要长期稳定运行
- 需要自定义域名
- 有一定预算（约 ¥100/年）

### 步骤概述

1. **购买服务器**
   - 阿里云：https://www.aliyun.com/
   - 腾讯云：https://cloud.tencent.com/
   - 选择：1核2G，Ubuntu 20.04

2. **连接服务器**
   ```bash
   ssh root@你的服务器IP
   ```

3. **安装环境**
   ```bash
   # 更新系统
   apt update && apt upgrade -y

   # 安装 Python
   apt install python3 python3-pip python3-venv -y

   # 安装 Nginx
   apt install nginx -y
   ```

4. **上传代码**
   ```bash
   # 使用 Git
   git clone https://github.com/你的用户名/EduDemo.git
   cd EduDemo/backend

   # 创建虚拟环境
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. **配置 Nginx**
   ```nginx
   server {
       listen 80;
       server_name 你的域名或IP;

       location / {
           root /root/EduDemo/frontend;
           index login.html;
       }

       location /api {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

6. **使用 Supervisor 管理进程**
   ```bash
   apt install supervisor -y
   ```

   创建配置文件 `/etc/supervisor/conf.d/edudemo.conf`：
   ```ini
   [program:edudemo]
   command=/root/EduDemo/backend/venv/bin/python app.py
   directory=/root/EduDemo/backend
   autostart=true
   autorestart=true
   stderr_logfile=/var/log/edudemo.err.log
   stdout_logfile=/var/log/edudemo.out.log
   ```

7. **启动服务**
   ```bash
   supervisorctl reread
   supervisorctl update
   supervisorctl start edudemo
   ```

8. **配置域名（可选）**
   - 购买域名
   - 添加 A 记录指向服务器 IP
   - 配置 SSL 证书（Let's Encrypt）

---

## 🔒 安全配置

### 1. 修改 CORS 配置

编辑 `backend/app.py`：

```python
# 生产环境只允许特定域名
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://your-frontend-domain.com"],  # 改为实际域名
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})
```

### 2. 使用强密钥

```python
# 生成随机密钥
import secrets
print(secrets.token_hex(32))
```

### 3. 关闭 Debug 模式

```python
app.run(debug=False)  # 生产环境必须关闭
```

### 4. 配置 HTTPS

使用 Let's Encrypt 免费 SSL 证书：

```bash
apt install certbot python3-certbot-nginx -y
certbot --nginx -d your-domain.com
```

---

## 📊 部署检查清单

部署前请确认：

- [ ] `.env` 文件不在 Git 仓库中
- [ ] 所有 API Key 已配置为环境变量
- [ ] JWT_SECRET_KEY 使用随机字符串
- [ ] Debug 模式已关闭
- [ ] CORS 配置正确
- [ ] 前端 API 地址已更新
- [ ] 数据库文件路径正确
- [ ] 所有依赖都在 requirements.txt 中

---

## 🐛 常见问题

### 1. 部署后无法访问

**检查**：
- 服务器是否正常运行
- 端口是否正确
- 防火墙是否开放
- 域名解析是否正确

### 2. AI API 调用失败

**检查**：
- 环境变量是否正确配置
- API Key 是否有效
- 服务器是否能访问外网

### 3. 数据库错误

**检查**：
- 数据库文件是否有写入权限
- 路径是否正确
- 是否需要初始化数据库

### 4. 跨域问题

**解决**：
- 检查 CORS 配置
- 确认前端域名在允许列表中

---

## 💡 优化建议

### 性能优化
- 使用 Gunicorn 替代 Flask 内置服务器
- 配置 Redis 缓存
- 使用 CDN 加速静态资源

### 监控和日志
- 配置日志收集
- 设置错误告警
- 监控服务器资源使用

### 备份
- 定期备份数据库
- 备份配置文件
- 使用版本控制

---

## 🎉 完成！

现在你的应用已经部署到互联网上了！

**访问地址**：
- 后端 API：`https://your-app.railway.app`
- 前端页面：`https://your-frontend.vercel.app`

**分享给朋友**：
- 发送前端地址给其他人
- 他们可以注册账号并使用

**下一步**：
- 监控应用运行状态
- 收集用户反馈
- 持续优化功能
