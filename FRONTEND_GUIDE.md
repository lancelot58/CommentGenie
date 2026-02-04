# 前端使用指南

## 📱 页面说明

### 1. 登录页面（login.html）

**功能**：
- 用户登录
- 自动保存登录状态（使用 localStorage）
- 已登录用户自动跳转到主页

**使用方法**：
1. 输入用户名和密码
2. 点击"登录"按钮
3. 登录成功后自动跳转到主页

---

### 2. 注册页面（register.html）

**功能**：
- 新用户注册
- 密码确认验证
- 用户名和密码长度验证

**使用方法**：
1. 输入用户名（3-20个字符）
2. 输入密码（至少6个字符）
3. 再次输入密码确认
4. 可选：输入邮箱
5. 点击"注册"按钮
6. 注册成功后自动跳转到登录页

---

### 3. 主页面（index.html）

**功能**：
- 生成学生评语
- 查看历史记录
- 复制评语
- 删除评语
- 退出登录

**使用方法**：

#### 生成评语
1. 输入学生姓名
2. 输入学生情况（越详细越好）
3. 选择 AI 模型（默认 DeepSeek）
4. 点击"生成评语"按钮
5. 等待几秒，评语生成完成
6. 可以点击"复制评语"按钮复制到剪贴板

#### 查看历史
- 页面加载时自动显示最近10条评语
- 点击"刷新"按钮可以重新加载
- 每条历史记录显示：
  - 学生姓名
  - 生成时间
  - 评语内容
  - 使用的 AI 模型

#### 管理评语
- 点击"复制"按钮：复制评语到剪贴板
- 点击"删除"按钮：删除该条评语（需要确认）

---

## 🚀 如何使用

### 方法1：直接打开（推荐）

1. 确保后端服务器正在运行：
   ```bash
   cd backend
   python app.py
   ```

2. 直接用浏览器打开前端页面：
   - 双击 `frontend/login.html`
   - 或在浏览器地址栏输入：`file:///C:/Users/admin/Desktop/EduDemo/frontend/login.html`

### 方法2：使用本地服务器

如果遇到跨域问题，可以使用 Python 启动一个简单的 HTTP 服务器：

```bash
cd frontend
python -m http.server 8000
```

然后在浏览器访问：`http://localhost:8000/login.html`

---

## 🎨 界面特点

### 设计风格
- **现代简洁**：采用渐变色背景和圆角卡片设计
- **响应式**：自动适配不同屏幕尺寸
- **动画效果**：平滑的过渡和加载动画
- **用户友好**：清晰的提示信息和错误处理

### 颜色方案
- 主色调：紫色渐变（#667eea → #764ba2）
- 背景：白色卡片 + 渐变背景
- 文字：深灰色（#333）和中灰色（#666）
- 成功：绿色（#d4edda）
- 错误：红色（#f8d7da）

---

## 💡 技术说明

### 前端技术栈
- **HTML5**：页面结构
- **CSS3**：样式和动画
- **JavaScript（原生）**：交互逻辑

### 核心功能实现

#### 1. 用户认证
```javascript
// 登录
const result = await login(username, password);

// 检查登录状态
if (isLoggedIn()) {
    // 已登录
}

// 登出
logout();
```

#### 2. API 调用
```javascript
// 生成评语
const response = await fetch(API_ENDPOINTS.generateComment, {
    method: 'POST',
    headers: getAuthHeaders(),
    body: JSON.stringify({
        student_name: '张三',
        student_info: '性格开朗...',
        ai_model: 'deepseek'
    })
});
```

#### 3. 本地存储
```javascript
// 保存 token
localStorage.setItem('auth_token', token);

// 读取 token
const token = localStorage.getItem('auth_token');

// 删除 token
localStorage.removeItem('auth_token');
```

---

## 🔧 配置说明

### API 地址配置

在 `js/config.js` 中修改 API 地址：

```javascript
// 开发环境
const API_BASE_URL = 'http://localhost:5000';

// 生产环境（部署后修改为实际地址）
const API_BASE_URL = 'https://your-domain.com';
```

---

## 🐛 常见问题

### 1. 无法连接到服务器

**错误信息**：网络错误，请检查服务器是否启动

**解决方法**：
- 确认后端服务器正在运行（`python app.py`）
- 检查 API 地址是否正确（`js/config.js`）
- 检查浏览器控制台的错误信息

### 2. 跨域问题（CORS）

**错误信息**：Access to fetch has been blocked by CORS policy

**解决方法**：
- 后端已配置 CORS，应该不会出现此问题
- 如果仍有问题，使用 HTTP 服务器打开前端（方法2）

### 3. 登录后立即退出

**原因**：Token 验证失败

**解决方法**：
- 检查 JWT_SECRET_KEY 是否正确配置
- 清除浏览器的 localStorage
- 重新登录

### 4. 评语生成失败

**可能原因**：
- AI API Key 未配置或无效
- API 调用超时
- 网络问题

**解决方法**：
- 检查 `.env` 文件中的 API Key
- 查看后端服务器日志
- 尝试切换其他 AI 模型

---

## 📝 代码结构

```
frontend/
├── login.html          # 登录页面
├── register.html       # 注册页面
├── index.html          # 主页面
├── css/
│   └── style.css       # 通用样式
└── js/
    ├── config.js       # 配置文件
    └── auth.js         # 认证工具
```

---

## 🎯 下一步优化建议

### 功能增强
- [ ] 批量生成评语
- [ ] 评语模板管理
- [ ] 导出评语（Word/PDF）
- [ ] 评语编辑功能
- [ ] 搜索和筛选历史记录

### 用户体验
- [ ] 添加加载骨架屏
- [ ] 优化移动端体验
- [ ] 添加键盘快捷键
- [ ] 支持暗黑模式

### 性能优化
- [ ] 图片懒加载
- [ ] 代码分割
- [ ] 缓存优化

---

## 🎉 完成！

前端开发已完成！现在你可以：
1. 启动后端服务器
2. 打开前端页面
3. 注册账号
4. 开始使用 AI 生成学生评语

祝使用愉快！
