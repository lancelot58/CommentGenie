# 部署前检查清单

在推送到 GitHub 和部署到 Vercel 之前，请确认以下事项：

## ✅ 必须完成的项目

### 1. 后端部署
- [ ] 已在 Railway/Render 等平台部署后端
- [ ] 已配置所有环境变量（API 密钥）
- [ ] 已获取后端 URL（例如：https://xxx.railway.app）
- [ ] 后端服务正常运行并可访问

### 2. 前端配置
- [ ] 已更新 `frontend/.env.production` 中的 API URL
- [ ] API URL 格式正确（https://your-backend.railway.app）
- [ ] 本地测试通过（npm run build 成功）

### 3. 后端 CORS 配置
- [ ] 已更新 `backend/app.py` 的 CORS 配置
- [ ] 允许 Vercel 域名（https://*.vercel.app）
- [ ] 允许你的自定义域名（如果有）

### 4. Git 配置
- [ ] `.gitignore` 已更新（排除 node_modules, dist, backend/.env）
- [ ] 敏感文件未被追踪（backend/.env, database.db）
- [ ] 所有新文件已添加到 Git

## 📋 推荐完成的项目

### 5. 代码质量
- [ ] 本地开发环境测试通过
- [ ] 所有功能正常工作
- [ ] 没有控制台错误
- [ ] 构建没有警告

### 6. 文档
- [ ] README.md 已更新
- [ ] 部署文档已创建
- [ ] 环境变量说明清晰

### 7. 安全
- [ ] JWT_SECRET_KEY 使用强密码
- [ ] API 密钥未提交到 Git
- [ ] 生产环境关闭 debug 模式

## 🚀 部署步骤

完成上述检查后，按以下步骤部署：

### 步骤 1: 提交代码
```bash
cd /d/Projects/CommentGenie
git add .
git commit -m "Migrate to Vue 3 + Vite + Element Plus"
git push origin master
```

### 步骤 2: Vercel 自动部署
- 推送后 Vercel 会自动开始构建
- 等待 3-5 分钟
- 检查构建日志

### 步骤 3: 验证部署
- 访问 Vercel 提供的 URL
- 测试注册、登录、生成评语
- 检查浏览器控制台是否有错误

## ⚠️ 常见错误预防

### 错误 1: API URL 未更新
**症状**: 前端无法连接后端
**预防**: 确认 `.env.production` 中的 URL 正确

### 错误 2: CORS 错误
**症状**: 浏览器控制台显示 CORS 错误
**预防**: 确认后端 CORS 配置包含 Vercel 域名

### 错误 3: 构建失败
**症状**: Vercel 构建过程出错
**预防**: 本地先运行 `npm run build` 测试

### 错误 4: 环境变量未生效
**症状**: 使用了错误的 API URL
**预防**: 确认 `.env.production` 已提交到 Git

## 📝 部署后验证

部署成功后，测试以下功能：

- [ ] 页面正常加载
- [ ] 用户注册功能
- [ ] 用户登录功能
- [ ] 评语生成功能（测试所有 AI 模型）
- [ ] 历史记录显示
- [ ] 复制功能
- [ ] 删除功能
- [ ] 退出登录功能
- [ ] 路由跳转正常
- [ ] 刷新页面不出现 404

## 🔧 如果部署失败

1. 查看 Vercel 构建日志
2. 检查错误信息
3. 参考 DEPLOYMENT_GUIDE_VERCEL.md 中的常见问题
4. 修复问题后重新推送

## 📞 获取帮助

如果遇到问题：
1. 查看 Vercel 构建日志
2. 查看浏览器控制台错误
3. 查看后端日志（Railway/Render）
4. 参考部署文档

祝部署顺利！🎉
