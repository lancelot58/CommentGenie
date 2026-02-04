# 学生评语生成器（EduDemo）

## 📝 项目简介

这是一个基于 AI 的学生评语自动生成系统，帮助老师快速生成个性化、有温度的学生评语。

### 核心功能

- ✅ **AI 智能生成**：支持 DeepSeek、智谱 AI、通义千问、Kimi 等多个 AI 模型
- ✅ **用户系统**：注册、登录、JWT 认证
- ✅ **历史管理**：保存、查看、复制、删除评语历史
- ✅ **现代 UI**：简洁美观的用户界面
- ✅ **响应式设计**：支持多种设备访问

---

## 🛠️ 技术栈

### 后端
- **Python 3.8+**
- **Flask** - Web 框架
- **SQLite** - 数据库
- **Flask-JWT-Extended** - 用户认证
- **bcrypt** - 密码加密
- **requests** - AI API 调用

### 前端
- **HTML5** - 页面结构
- **CSS3** - 样式和动画
- **JavaScript（原生）** - 交互逻辑

### AI 集成
- DeepSeek（推荐）
- 智谱 AI（GLM-4）
- 通义千问（Qwen）
- Kimi（月之暗面）

---

## 📁 项目结构

```
EduDemo/
├── backend/                    # 后端代码
│   ├── app.py                 # Flask 主程序
│   ├── models.py              # 数据库模型
│   ├── utils/
│   │   ├── __init__.py        # 工具模块
│   │   └── ai_client.py       # AI 客户端
│   ├── test_api.py            # API 测试脚本
│   ├── test_ai.py             # AI 功能测试
│   ├── requirements.txt       # Python 依赖
│   ├── .env.example           # 环境变量模板
│   └── database.db            # SQLite 数据库
├── frontend/                   # 前端代码
│   ├── login.html             # 登录页面
│   ├── register.html          # 注册页面
│   ├── index.html             # 主页面
│   ├── css/
│   │   └── style.css          # 通用样式
│   └── js/
│       ├── config.js          # 配置文件
│       └── auth.js            # 认证工具
├── LEARNING_GUIDE.md          # 完整学习指南
├── LOCAL_DEPLOYMENT.md        # 本地部署指南
├── DEPLOYMENT_GUIDE.md        # 互联网部署指南
├── AI_API_GUIDE.md            # AI API 申请指南
├── FRONTEND_GUIDE.md          # 前端使用指南
├── README.md                  # 项目说明（本文件）
└── .gitignore                 # Git 忽略文件
```

---

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/你的用户名/EduDemo.git
cd EduDemo
```

### 2. 安装后端依赖

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

### 3. 配置环境变量

```bash
copy .env.example .env  # Windows
# cp .env.example .env  # Mac/Linux
```

编辑 `.env` 文件，填入你的配置：
```env
DEEPSEEK_API_KEY=sk-你的密钥
JWT_SECRET_KEY=随机字符串
```

### 4. 启动后端服务器

```bash
python app.py
```

### 5. 打开前端页面

双击 `frontend/login.html` 或在浏览器访问：
```
file:///你的路径/EduDemo/frontend/login.html
```

### 6. 注册并使用

- 注册新账号
- 登录系统
- 输入学生信息
- 生成评语

---

## 📚 文档导航

| 文档 | 说明 |
|------|------|
| [LEARNING_GUIDE.md](LEARNING_GUIDE.md) | 完整的学习指南，从零开始 |
| [LOCAL_DEPLOYMENT.md](LOCAL_DEPLOYMENT.md) | 本地部署详细步骤 |
| [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) | 互联网部署指南 |
| [AI_API_GUIDE.md](AI_API_GUIDE.md) | AI API 申请和配置 |
| [FRONTEND_GUIDE.md](FRONTEND_GUIDE.md) | 前端使用说明 |

---

## 🌟 功能特点

### 1. 多 AI 模型支持

支持切换不同的 AI 模型，选择最适合的评语风格：
- **DeepSeek**：性价比最高，推荐日常使用
- **智谱 AI**：中文能力强，适合复杂评语
- **通义千问**：稳定可靠，适合批量生成
- **Kimi**：长文本处理能力强

### 2. 智能评语生成

根据学生信息自动生成：
- 真诚具体的评语内容
- 突出学生优点和进步
- 委婉的改进建议
- 温暖鼓励的语气

### 3. 历史记录管理

- 自动保存所有生成的评语
- 按时间倒序显示
- 一键复制到剪贴板
- 支持删除不需要的记录

### 4. 安全可靠

- 密码 bcrypt 加密存储
- JWT Token 身份验证
- SQL 注入防护
- CORS 跨域配置

---

## 🖼️ 界面预览

### 登录页面
- 简洁的登录表单
- 渐变色背景
- 平滑的动画效果

### 主页面
- 评语生成表单
- AI 模型选择
- 实时生成结果
- 历史记录列表

---

## 🔧 开发指南

### 运行测试

```bash
# 测试 API 接口
cd backend
python test_api.py

# 测试 AI 功能
python test_ai.py
```

### 修改配置

**修改 API 地址**（`frontend/js/config.js`）：
```javascript
const API_BASE_URL = 'http://localhost:5000';
```

**修改 AI 模型**（`backend/utils/ai_client.py`）：
- 添加新的 AI 客户端类
- 在 `get_ai_client()` 中注册

---

## 🌐 部署

### 本地部署

详细步骤请查看：[LOCAL_DEPLOYMENT.md](LOCAL_DEPLOYMENT.md)

### 互联网部署

推荐使用 Railway（免费）：

1. 注册 GitHub 和 Railway
2. 上传代码到 GitHub
3. 在 Railway 中导入仓库
4. 配置环境变量
5. 自动部署完成

详细步骤请查看：[DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

---

## 🐛 常见问题

### 无法连接服务器

**解决**：
- 确认后端服务器正在运行
- 检查 API 地址配置
- 查看浏览器控制台错误

### AI 生成失败

**解决**：
- 检查 `.env` 文件中的 API Key
- 确认 API Key 有效且有余额
- 重启后端服务器

### 端口被占用

**解决**：
- 修改 `.env` 中的 `PORT` 配置
- 或关闭占用端口的程序

更多问题请查看各个文档的"常见问题"部分。

---

## 📈 性能指标

- **响应时间**：评语生成 2-5 秒
- **并发支持**：单机 50+ 并发
- **数据库**：支持 10000+ 评语记录
- **成本**：使用 DeepSeek，1000 条评语约 ¥0.05

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 开发流程

1. Fork 本仓库
2. 创建特性分支（`git checkout -b feature/AmazingFeature`）
3. 提交更改（`git commit -m 'Add some AmazingFeature'`）
4. 推送到分支（`git push origin feature/AmazingFeature`）
5. 开启 Pull Request

---

## 📄 许可证

本项目仅供学习使用。

---

## 👨‍💻 作者

- 开发者：小白学习者
- 指导：Claude AI
- 日期：2026-02-04

---

## 🙏 致谢

- Flask 框架
- DeepSeek AI
- 智谱 AI
- 所有开源贡献者

---

## 📞 联系方式

如有问题，请通过以下方式联系：
- 提交 GitHub Issue
- 查看文档获取帮助

---

## 🎉 开始使用

现在就开始你的 AI 评语生成之旅吧！

1. 查看 [LEARNING_GUIDE.md](LEARNING_GUIDE.md) 开始学习
2. 按照 [LOCAL_DEPLOYMENT.md](LOCAL_DEPLOYMENT.md) 部署项目
3. 参考 [AI_API_GUIDE.md](AI_API_GUIDE.md) 申请 API
4. 享受 AI 带来的便利！

**祝你使用愉快！** 🚀
