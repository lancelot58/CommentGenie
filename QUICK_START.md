# CommentGenie Vue 版本快速启动指南

## 前提条件

- Node.js 16+ 已安装
- Python 3.8+ 已安装（后端）
- Git 已安装

## 快速启动

### 1. 启动后端服务器

```bash
# 进入后端目录
cd backend

# 安装 Python 依赖（首次运行）
pip install -r requirements.txt

# 启动后端服务器
python app.py
```

后端将在 http://localhost:5000 运行。

### 2. 启动前端开发服务器

打开新的终端窗口：

```bash
# 进入前端目录
cd frontend

# 安装依赖（首次运行）
npm install

# 启动开发服务器
npm run dev
```

前端将在 http://localhost:3000 运行。

### 3. 访问应用

在浏览器中打开 http://localhost:3000

## 功能测试清单

### 用户认证
- [ ] 注册新用户
- [ ] 登录
- [ ] 退出登录
- [ ] 未登录访问主页自动跳转到登录页

### 评语生成
- [ ] 填写学生姓名和情况
- [ ] 选择 AI 模型（DeepSeek、智谱 AI、通义千问、Kimi）
- [ ] 生成评语
- [ ] 查看生成结果
- [ ] 复制评语到剪贴板

### 历史记录
- [ ] 查看历史记录列表
- [ ] 刷新历史记录
- [ ] 复制历史评语
- [ ] 删除历史评语

## 常见问题

### 前端无法连接后端

**问题**: 前端显示网络错误

**解决方案**:
1. 确认后端服务器正在运行（http://localhost:5000）
2. 检查后端是否配置了 CORS
3. 查看浏览器控制台的错误信息

### 端口被占用

**问题**: 端口 3000 或 5000 已被占用

**解决方案**:
1. 修改前端端口：编辑 `frontend/vite.config.js`，更改 `server.port`
2. 修改后端端口：编辑 `backend/app.py`，更改 `app.run(port=...)`
3. 同时更新 `frontend/.env.development` 中的 API 地址

### 构建失败

**问题**: npm run build 失败

**解决方案**:
1. 删除 `node_modules` 和 `package-lock.json`
2. 重新运行 `npm install`
3. 再次尝试 `npm run build`

## 生产环境部署

### 构建前端

```bash
cd frontend
npm run build
```

构建输出在 `frontend/dist` 目录。

### 更新生产环境 API 地址

编辑 `frontend/.env.production`：

```
VITE_API_BASE_URL=https://your-backend-api.com
```

### 部署到 Vercel

1. 提交代码到 GitHub：
   ```bash
   git add .
   git commit -m "Update Vue frontend"
   git push
   ```

2. Vercel 会自动检测到更改并重新部署

## 项目结构说明

```
CommentGenie/
├── backend/              # Flask 后端
│   ├── app.py           # 主应用
│   ├── models.py        # 数据模型
│   └── requirements.txt # Python 依赖
├── frontend/            # Vue 3 前端
│   ├── src/
│   │   ├── components/  # 可复用组件
│   │   ├── composables/ # 组合式函数
│   │   ├── router/      # 路由配置
│   │   ├── services/    # API 服务
│   │   ├── utils/       # 工具函数
│   │   └── views/       # 页面组件
│   └── package.json
├── frontend_backup/     # 原静态版本备份
└── vercel.json         # Vercel 部署配置
```

## 开发建议

### 代码风格
- 使用 Vue 3 Composition API
- 遵循 Element Plus 组件使用规范
- 保持代码简洁和可读性

### Git 提交
- 使用有意义的提交信息
- 每个功能一个提交
- 提交前测试功能

### 调试
- 使用 Vue DevTools 浏览器扩展
- 查看浏览器控制台的错误信息
- 使用 `console.log` 调试（开发环境）

## 获取帮助

如果遇到问题：
1. 查看 `frontend/README.md` 了解详细文档
2. 查看 `MIGRATION_SUMMARY.md` 了解转换详情
3. 检查浏览器控制台的错误信息
4. 检查后端日志

## 下一步

- [ ] 完成功能测试
- [ ] 配置生产环境 API 地址
- [ ] 部署到 Vercel
- [ ] 测试生产环境功能

祝开发愉快！
