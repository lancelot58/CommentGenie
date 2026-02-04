# 本地部署指南

## 📋 前置要求

在开始之前，请确保你的电脑已安装：
- ✅ Python 3.8 或更高版本
- ✅ 现代浏览器（Chrome、Firefox、Edge 等）
- ✅ 文本编辑器（VS Code 推荐）

---

## 🚀 完整部署步骤

### 步骤1：检查 Python 环境

打开命令行（Windows 按 `Win + R`，输入 `cmd`），运行：

```bash
python --version
```

应该显示类似：`Python 3.14.2`

---

### 步骤2：进入项目目录

```bash
cd C:\Users\admin\Desktop\EduDemo
```

或者在文件管理器中右键项目文件夹，选择"在终端中打开"。

---

### 步骤3：安装后端依赖

```bash
# 进入后端目录
cd backend

# 创建虚拟环境（如果还没有）
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# 安装依赖包
pip install -r requirements.txt
```

**说明**：
- 虚拟环境是一个独立的 Python 环境，避免不同项目的依赖冲突
- 激活后，命令行前面会显示 `(venv)`

---

### 步骤4：配置环境变量

1. 复制环境变量模板：
   ```bash
   copy .env.example .env
   ```

2. 编辑 `.env` 文件，填入你的配置：
   ```env
   # AI API 配置（至少配置一个）
   DEEPSEEK_API_KEY=sk-你的DeepSeek密钥
   ZHIPU_API_KEY=你的智谱AI密钥

   # JWT 密钥（随机字符串）
   JWT_SECRET_KEY=your-random-secret-key-12345678

   # 数据库配置
   DATABASE_PATH=database.db

   # 服务器配置
   FLASK_ENV=development
   PORT=5000
   ```

**重要**：
- 至少配置一个 AI API Key（推荐 DeepSeek）
- JWT_SECRET_KEY 要改成随机字符串
- 如何申请 AI API Key，请查看 `AI_API_GUIDE.md`

---

### 步骤5：启动后端服务器

#### 方法1：使用命令提示符（CMD）- 推荐

**打开命令提示符**：
1. 按 `Win + R` 键
2. 输入 `cmd`
3. 按回车

**进入项目目录并启动**：
```bash
# 进入后端目录
cd C:\Users\admin\Desktop\EduDemo\backend

# 激活虚拟环境
venv\Scripts\activate

# 启动服务器
python app.py
```

**成功标志**：
```
==================================================
学生评语生成器 API 服务器
==================================================
服务器地址: http://localhost:5000
API 文档: http://localhost:5000/
==================================================
 * Running on http://127.0.0.1:5000
```

**注意**：
- 激活虚拟环境后，命令行前面会显示 `(venv)`
- 保持这个命令行窗口打开，不要关闭
- 服务器会在 `http://localhost:5000` 运行
- 按 `Ctrl + C` 可以停止服务器

#### 方法2：使用 PowerShell

**打开 PowerShell**：
- 在项目文件夹上右键
- 选择"在终端中打开"

**启动服务器**：
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python app.py
```

如果遇到权限错误，先运行：
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 方法3：使用 VS Code 终端

1. 用 VS Code 打开项目文件夹
2. 按 `Ctrl + ~` 打开终端
3. 运行：
   ```bash
   cd backend
   venv\Scripts\activate
   python app.py
   ```

---

### 步骤6：打开前端页面

**方法1：直接打开（推荐）**

1. 打开文件管理器
2. 进入 `frontend` 目录
3. 双击 `login.html` 文件
4. 浏览器会自动打开登录页面

**方法2：使用浏览器地址栏**

在浏览器地址栏输入：
```
file:///C:/Users/admin/Desktop/EduDemo/frontend/login.html
```

**方法3：使用 HTTP 服务器（可选）**

如果遇到跨域问题，可以启动一个简单的 HTTP 服务器：

```bash
# 新开一个命令行窗口
cd C:\Users\admin\Desktop\EduDemo\frontend
python -m http.server 8000
```

然后在浏览器访问：`http://localhost:8000/login.html`

---

### 步骤7：注册和使用

1. **注册账号**
   - 在登录页面点击"立即注册"
   - 填写用户名（3-20个字符）
   - 填写密码（至少6个字符）
   - 点击"注册"按钮

2. **登录**
   - 输入刚才注册的用户名和密码
   - 点击"登录"按钮
   - 登录成功后自动跳转到主页

3. **生成评语**
   - 输入学生姓名
   - 输入学生情况（越详细越好）
   - 选择 AI 模型
   - 点击"生成评语"按钮
   - 等待几秒，评语生成完成

4. **查看历史**
   - 页面下方会显示历史记录
   - 可以复制或删除评语

---

## 🔧 常见问题

### 1. 命令找不到（command not found）

**问题**：运行 `python` 命令时提示找不到

**解决**：
- 检查 Python 是否正确安装
- 尝试使用 `python3` 或 `py` 命令
- 将 Python 添加到系统环境变量

### 2. 端口被占用

**错误信息**：`Address already in use`

**解决**：
- 方法1：关闭占用 5000 端口的程序
- 方法2：修改 `.env` 文件中的 `PORT=5001`

### 3. 虚拟环境激活失败

**Windows 错误**：`无法加载文件，因为在此系统上禁止运行脚本`

**解决**：
```bash
# 以管理员身份运行 PowerShell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 4. 依赖安装失败

**错误信息**：`pip install` 失败

**解决**：
```bash
# 升级 pip
python -m pip install --upgrade pip

# 使用国内镜像源
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 5. 无法连接到服务器

**前端错误**：网络错误，请检查服务器是否启动

**解决**：
- 确认后端服务器正在运行
- 检查浏览器控制台的错误信息（按 F12）
- 确认 API 地址正确（`frontend/js/config.js`）

### 6. AI 生成失败

**错误信息**：未配置 xxx 的 API Key

**解决**：
- 检查 `.env` 文件中是否填入了 API Key
- 确认 API Key 是否有效
- 重启后端服务器（修改 `.env` 后需要重启）

---

## 📝 日常使用流程

### 启动项目

1. 打开命令行
2. 进入后端目录：`cd C:\Users\admin\Desktop\EduDemo\backend`
3. 激活虚拟环境：`venv\Scripts\activate`
4. 启动服务器：`python app.py`
5. 打开浏览器，访问前端页面

### 停止项目

1. 在后端命令行窗口按 `Ctrl + C`
2. 关闭浏览器标签页

---

## 🎯 快速启动脚本（可选）

为了方便启动，可以创建一个批处理脚本：

**Windows（start.bat）**：
```batch
@echo off
cd /d C:\Users\admin\Desktop\EduDemo\backend
call venv\Scripts\activate
python app.py
pause
```

**使用方法**：
1. 将上面的内容保存为 `start.bat`
2. 双击运行即可启动服务器

---

## 📊 系统架构

```
┌─────────────┐         HTTP 请求          ┌─────────────┐
│   浏览器    │ ─────────────────────────> │ Flask 服务器 │
│  (前端)     │ <───────────────────────── │   (后端)     │
└─────────────┘         JSON 响应          └─────────────┘
                                                   │
                                                   │ 调用
                                                   ↓
                                            ┌─────────────┐
                                            │  AI API     │
                                            │ (DeepSeek等)│
                                            └─────────────┘
                                                   │
                                                   │ 存储
                                                   ↓
                                            ┌─────────────┐
                                            │  SQLite     │
                                            │  数据库     │
                                            └─────────────┘
```

---

## ✅ 验证部署成功

### 1. 后端验证

访问：`http://localhost:5000/`

应该看到：
```json
{
  "message": "学生评语生成器 API",
  "version": "1.0.0",
  "status": "running"
}
```

### 2. 前端验证

- 能够打开登录页面
- 能够注册新用户
- 能够登录
- 能够生成评语

### 3. AI 功能验证

运行测试脚本：
```bash
cd backend
python test_ai.py
```

应该看到评语成功生成。

---

## 🎉 完成！

现在你已经成功在本地部署了学生评语生成器！

**下一步**：
- 查看 `FRONTEND_GUIDE.md` 了解前端使用方法
- 查看 `AI_API_GUIDE.md` 了解如何申请更多 AI API
- 查看 `DEPLOYMENT_GUIDE.md` 了解如何部署到互联网
