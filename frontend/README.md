# CommentGenie Vue 3 Frontend

基于 Vue 3 + Vite + Element Plus 的前端应用。

## 技术栈

- **Vue 3** - 使用 Composition API
- **Vite** - 快速的开发构建工具
- **Element Plus** - UI 组件库
- **Vue Router** - 路由管理
- **Axios** - HTTP 客户端

## 项目结构

```
frontend/
├── src/
│   ├── assets/          # 静态资源
│   ├── components/      # 可复用组件
│   │   ├── CommentCard.vue
│   │   └── CommentForm.vue
│   ├── composables/     # 组合式函数
│   │   ├── useAuth.js
│   │   └── useMessage.js
│   ├── router/          # 路由配置
│   │   └── index.js
│   ├── services/        # API 服务
│   │   ├── api.js
│   │   └── comment.js
│   ├── utils/           # 工具函数
│   │   └── config.js
│   ├── views/           # 页面组件
│   │   ├── HomeView.vue
│   │   ├── LoginView.vue
│   │   └── RegisterView.vue
│   ├── App.vue          # 根组件
│   └── main.js          # 入口文件
├── .env.development     # 开发环境配置
├── .env.production      # 生产环境配置
├── index.html
├── package.json
└── vite.config.js
```

## 开发

### 安装依赖

```bash
npm install
```

### 启动开发服务器

```bash
npm run dev
```

开发服务器将在 http://localhost:3000 启动。

### 构建生产版本

```bash
npm run build
```

构建输出将在 `dist` 目录。

### 预览生产构建

```bash
npm run preview
```

## 环境变量

### 开发环境 (.env.development)

```
VITE_API_BASE_URL=http://localhost:5000
```

### 生产环境 (.env.production)

```
VITE_API_BASE_URL=https://your-backend-api.com
```

**注意**: 部署到生产环境前，需要更新 `.env.production` 中的 API 地址。

## 功能特性

- ✅ 用户注册和登录
- ✅ JWT 认证
- ✅ 评语生成（支持多个 AI 模型）
- ✅ 历史记录查看
- ✅ 评语复制和删除
- ✅ 响应式设计
- ✅ 路由守卫

## API 代理

开发环境下，Vite 会将 `/api` 请求代理到 `http://localhost:5000`。

配置在 `vite.config.js` 中：

```javascript
server: {
  proxy: {
    '/api': {
      target: 'http://localhost:5000',
      changeOrigin: true,
    },
  },
}
```

## 部署

### Vercel 部署

项目已配置 Vercel 部署，根目录的 `vercel.json` 包含构建配置：

```json
{
  "buildCommand": "cd frontend && npm install && npm run build",
  "outputDirectory": "frontend/dist",
  "installCommand": "cd frontend && npm install"
}
```

推送到 GitHub 后，Vercel 会自动构建和部署。

## 注意事项

1. 确保后端服务器在 `localhost:5000` 运行（开发环境）
2. 生产环境需要配置正确的 API 地址
3. 使用 HTML5 History 模式，需要服务器配置 SPA 回退
4. 已在 `vercel.json` 中配置了 rewrites 规则

## 从旧版本迁移

旧的静态 HTML 版本已备份到 `frontend_backup` 目录。

主要变化：
- 从静态 HTML 转换为 Vue 单页应用
- 使用 Element Plus 替代原生 HTML 表单
- 使用 Vue Router 管理路由
- 使用 Axios 替代 fetch API
- 使用 Composition API 组织代码逻辑
