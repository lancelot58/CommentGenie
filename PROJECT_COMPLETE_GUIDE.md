# CommentGenie 完整项目指南

## 项目概述

**CommentGenie** 是一个基于 AI 的学生评语生成系统，已成功从静态 HTML 迁移到现代化的 Vue 3 架构，并完成云端部署。

### 技术栈

**前端**:
- Vue 3 (Composition API)
- Vite (构建工具)
- Element Plus (UI 组件库)
- Vue Router (路由管理)
- Axios (HTTP 客户端)

**后端**:
- Flask (Python Web 框架)
- SQLite (数据库)
- Flask-CORS (跨域支持)
- Flask-JWT-Extended (JWT 认证)
- bcrypt (密码加密)

**AI 集成**:
- DeepSeek API
- 智谱 AI (GLM-4)
- 通义千问 (Qwen)
- Kimi (月之暗面)

### 部署平台

- **前端**: Vercel
- **后端**: Railway
- **域名**: edukit.xyz

---

## 项目架构

```
CommentGenie
│
├── 前端 (Vercel)
│   ├── URL: https://www.edukit.xyz
│   ├── 框架: Vue 3 + Vite
│   ├── UI: Element Plus
│   └── 路由: Vue Router
│
├── 后端 (Railway)
│   ├── URL: https://commentgenie-production.up.railway.app
│   ├── 框架: Flask
│   ├── 数据库: SQLite
│   └── AI: 4 个模型集成
│
└── GitHub
    └── 仓库: lancelot58/CommentGenie
```

---

## 功能特性

### 用户功能
- ✅ 用户注册和登录
- ✅ JWT 令牌认证
- ✅ 密码加密存储

### 评语生成
- ✅ 支持 4 个 AI 模型
  - DeepSeek（推荐）
  - 智谱 AI
  - 通义千问
  - Kimi
- ✅ 自定义学生信息输入
- ✅ 实时生成评语

### 历史管理
- ✅ 查看历史记录
- ✅ 复制评语到剪贴板
- ✅ 删除历史记录
- ✅ 刷新功能

---

## 项目结构

### 前端结构

```
frontend/
├── src/
│   ├── assets/
│   │   └── styles/
│   ├── components/
│   │   ├── CommentCard.vue      # 评语卡片组件
│   │   └── CommentForm.vue      # 评语生成表单
│   ├── composables/
│   │   ├── useAuth.js           # 认证逻辑
│   │   └── useMessage.js        # 消息提示
│   ├── router/
│   │   └── index.js             # 路由配置
│   ├── services/
│   │   ├── api.js               # Axios 配置
│   │   └── comment.js           # 评语 API
│   ├── utils/
│   │   └── config.js            # 配置文件
│   ├── views/
│   │   ├── HomeView.vue         # 主页面
│   │   ├── LoginView.vue        # 登录页面
│   │   └── RegisterView.vue     # 注册页面
│   ├── App.vue                  # 根组件
│   └── main.js                  # 入口文件
├── .env.development             # 开发环境配置
├── .env.production              # 生产环境配置
├── package.json
├── vite.config.js
└── vercel.json                  # Vercel 配置
```

### 后端结构

```
backend/
├── utils/
│   └── ai_client.py             # AI 客户端
├── app.py                       # Flask 主程序
├── models.py                    # 数据模型
├── requirements.txt             # Python 依赖
├── Procfile                     # Railway 进程配置
├── railway.json                 # Railway 配置
├── runtime.txt                  # Python 版本
└── .env                         # 环境变量（不提交）
```

---

## 环境配置

### 前端环境变量

**开发环境** (`.env.development`):
```
VITE_API_BASE_URL=http://localhost:5000
```

**生产环境** (`.env.production`):
```
VITE_API_BASE_URL=https://commentgenie-production.up.railway.app
```

### 后端环境变量

**Railway 配置** (在 Railway 项目设置中配置):
```
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxx
ZHIPU_API_KEY=xxxxxxxxxxxxx
QWEN_API_KEY=sk-xxxxxxxxxxxxx
KIMI_API_KEY=xxxxxxxxxxxxx
JWT_SECRET_KEY=随机生成的32位密钥
FLASK_ENV=production
PORT=5000
```

---

## 本地开发

### 前端开发

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 访问 http://localhost:3000
```

### 后端开发

```bash
# 进入后端目录
cd backend

# 安装依赖
pip install -r requirements.txt

# 启动服务器
python app.py

# 访问 http://localhost:5000
```

---

## 部署指南

### Vercel 前端部署

#### 1. 配置项目

在 Vercel 项目设置中：
- **Root Directory**: `frontend`
- **Framework Preset**: Vite
- **Build Command**: `npm run build`
- **Output Directory**: `dist`

#### 2. 添加自定义域名

1. 进入 Vercel 项目 → Settings → Domains
2. 添加域名：`edukit.xyz`
3. 配置 DNS 记录：
   ```
   类型: A
   名称: @
   值: 76.76.21.21

   类型: CNAME
   名称: www
   值: cname.vercel-dns.com
   ```

#### 3. 部署

推送代码到 GitHub，Vercel 自动部署：
```bash
git push origin master
```

### Railway 后端部署

#### 1. 创建项目

1. 访问 https://railway.app/
2. 连接 GitHub 仓库
3. 选择 CommentGenie 项目

#### 2. 配置项目

- **Root Directory**: `backend`
- **Start Command**: `python app.py`

#### 3. 配置环境变量

在 Railway 项目 → Variables 中添加：
```
DEEPSEEK_API_KEY=你的密钥
ZHIPU_API_KEY=你的密钥
QWEN_API_KEY=你的密钥
KIMI_API_KEY=你的密钥
JWT_SECRET_KEY=随机密钥
FLASK_ENV=production
PORT=5000
```

#### 4. 生成域名

在 Settings → Domains 中点击 "Generate Domain"

---

## CORS 配置

### 后端 CORS 设置

在 `backend/app.py` 中：

```python
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:3000",  # 开发环境
            "https://*.vercel.app",  # Vercel 部署
            "https://commentgenie.vercel.app",
            "https://edukit.xyz",  # 自定义域名
            "https://www.edukit.xyz",  # www 子域名
            "https://*.edukit.xyz"  # 所有子域名
        ],
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})
```

---

## API 文档

### 基础 URL

- **开发环境**: `http://localhost:5000`
- **生产环境**: `https://commentgenie-production.up.railway.app`

### 认证接口

#### 注册
```
POST /api/register
Content-Type: application/json

{
  "username": "用户名",
  "password": "密码",
  "email": "邮箱（可选）"
}
```

#### 登录
```
POST /api/login
Content-Type: application/json

{
  "username": "用户名",
  "password": "密码"
}

响应:
{
  "success": true,
  "token": "JWT令牌",
  "user": {
    "id": 1,
    "username": "用户名"
  }
}
```

### 评语接口

#### 生成评语
```
POST /api/comment/generate
Authorization: Bearer <token>
Content-Type: application/json

{
  "student_name": "学生姓名",
  "student_info": "学生情况描述",
  "ai_model": "deepseek"
}

响应:
{
  "success": true,
  "comment": "生成的评语内容",
  "comment_id": 1
}
```

#### 获取历史记录
```
GET /api/comment/history?limit=50
Authorization: Bearer <token>

响应:
{
  "success": true,
  "comments": [
    {
      "id": 1,
      "student_name": "张三",
      "generated_comment": "评语内容",
      "ai_model": "deepseek",
      "created_at": "2026-02-05T12:00:00"
    }
  ]
}
```

#### 删除评语
```
DELETE /api/comment/<id>
Authorization: Bearer <token>

响应:
{
  "success": true,
  "message": "删除成功"
}
```

---

## 常见问题

### 1. CORS 错误

**问题**: 前端无法连接后端，提示 CORS 错误

**解决方案**:
1. 检查后端 CORS 配置是否包含前端域名
2. 确认 Railway 已重新部署最新代码
3. 清除浏览器缓存

### 2. 登录没反应

**问题**: 点击登录按钮没有响应

**解决方案**:
1. 打开浏览器开发者工具（F12）
2. 查看 Console 标签的错误信息
3. 查看 Network 标签的请求状态
4. 确认后端服务正在运行

### 3. Railway 部署失败

**问题**: Railway 显示 Crashed 状态

**解决方案**:
1. 查看 Railway 部署日志
2. 检查环境变量是否配置完整
3. 确认 requirements.txt 中的依赖正确
4. 检查 Python 版本兼容性

### 4. Vercel 构建失败

**问题**: Vercel 构建过程出错

**解决方案**:
1. 检查 package.json 依赖
2. 确认 Root Directory 设置为 `frontend`
3. 查看构建日志中的具体错误
4. 本地运行 `npm run build` 测试

### 5. 域名无法访问

**问题**: 自定义域名无法访问

**解决方案**:
1. 检查 DNS 配置是否正确
2. 等待 DNS 传播（5-30 分钟）
3. 使用 DNS 检查工具验证
4. 清除浏览器 DNS 缓存

---

## 性能优化建议

### 前端优化

1. **代码分割**
   - 使用动态导入
   - 路由懒加载
   - 组件懒加载

2. **资源优化**
   - 图片压缩和懒加载
   - 使用 CDN
   - 启用 Gzip 压缩

3. **缓存策略**
   - Service Worker
   - 浏览器缓存
   - API 响应缓存

### 后端优化

1. **数据库优化**
   - 添加索引
   - 查询优化
   - 迁移到 PostgreSQL

2. **API 优化**
   - 响应压缩
   - 分页查询
   - 缓存热点数据

3. **安全加固**
   - API 限流
   - 请求验证
   - SQL 注入防护

---

## 功能扩展建议

### 短期优化

1. **用户体验**
   - 添加加载动画
   - 优化错误提示
   - 添加操作确认

2. **功能增强**
   - 批量生成评语
   - 评语模板管理
   - 导出功能（Word/PDF）

3. **数据管理**
   - 用户数据导出
   - 历史记录搜索
   - 评语收藏功能

### 长期规划

1. **多用户支持**
   - 团队协作
   - 权限管理
   - 数据共享

2. **AI 增强**
   - 自定义 AI 提示词
   - 评语风格选择
   - 多语言支持

3. **移动端**
   - 响应式优化
   - PWA 支持
   - 移动端 App

---

## 维护指南

### 日常维护

1. **监控**
   - Vercel Analytics
   - Railway Metrics
   - 错误日志监控

2. **备份**
   - 数据库定期备份
   - 代码版本管理
   - 配置文件备份

3. **更新**
   - 依赖包更新
   - 安全补丁
   - 功能迭代

### 故障处理

1. **前端故障**
   - 检查 Vercel 部署状态
   - 查看构建日志
   - 回滚到上一个版本

2. **后端故障**
   - 检查 Railway 服务状态
   - 查看应用日志
   - 重启服务

3. **数据恢复**
   - 从备份恢复
   - 数据迁移
   - 用户通知

---

## 项目成果

### 技术成就

- ✅ 成功迁移到 Vue 3 现代化架构
- ✅ 实现前后端分离
- ✅ 完成云端部署
- ✅ 配置自定义域名
- ✅ 集成 4 个 AI 模型

### 学习收获

1. **前端开发**
   - Vue 3 Composition API
   - Element Plus 组件库
   - Vue Router 路由管理
   - Axios HTTP 客户端

2. **后端开发**
   - Flask Web 框架
   - RESTful API 设计
   - JWT 认证
   - CORS 配置

3. **云端部署**
   - Vercel 静态网站部署
   - Railway 后端部署
   - 域名配置
   - 环境变量管理

4. **问题解决**
   - CORS 跨域问题
   - 网络连接问题
   - 部署配置问题
   - DNS 配置问题

---

## 项目信息

### 访问地址

- **生产环境**: https://www.edukit.xyz
- **后端 API**: https://commentgenie-production.up.railway.app
- **GitHub**: https://github.com/lancelot58/CommentGenie

### 技术支持

如需帮助，请参考：
- 项目 README.md
- 部署文档
- API 文档
- 常见问题

### 版本历史

- **v2.0.0** (2026-02-05): Vue 3 重构版本，完成云端部署
- **v1.0.0** (2026-02-04): 初始静态 HTML 版本

---

## 致谢

感谢以下技术和平台：

- **Vue.js** - 渐进式 JavaScript 框架
- **Element Plus** - Vue 3 组件库
- **Vite** - 下一代前端构建工具
- **Flask** - Python Web 微框架
- **Vercel** - 前端部署平台
- **Railway** - 后端部署平台
- **DeepSeek, 智谱, 通义, Kimi** - AI 服务提供商

---

## 许可证

本项目仅供学习和个人使用。

---

**项目完成日期**: 2026年2月5日

**文档版本**: 1.0.0

**最后更新**: 2026-02-05
