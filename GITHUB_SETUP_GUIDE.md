# GitHub 仓库创建指南

## 📋 准备工作

在创建 GitHub 仓库之前，请确保：
- ✅ 已注册 GitHub 账号
- ✅ 本地已安装 Git
- ✅ 项目代码已准备好

---

## 🚀 第一步：创建 GitHub 仓库

### 1. 登录 GitHub

访问：https://github.com/

### 2. 创建新仓库

1. 点击右上角的 **"+"** 按钮
2. 选择 **"New repository"**
3. 或直接访问：https://github.com/new

### 3. 配置仓库信息

**Repository name（仓库名称）**：
```
CommentGenie
```

**Description（描述）**：
```
🧚 评语精灵 - 基于 AI 的学生评语智能生成工具，让每一句评语都有温度
```

**可见性**：
- ✅ **Public**（公开）- 推荐，任何人都可以看到
- ⬜ **Private**（私有）- 只有你和授权的人可以看到

**初始化选项**：
- ⬜ **不要**勾选 "Add a README file"（我们已经有了）
- ⬜ **不要**勾选 "Add .gitignore"（我们已经有了）
- ⬜ **不要**选择 License（可以后续添加）

### 4. 创建仓库

点击 **"Create repository"** 按钮

---

## 💻 第二步：本地 Git 配置

### 1. 打开命令行

```bash
# 进入项目目录
cd C:\Users\admin\Desktop\EduDemo
```

### 2. 初始化 Git 仓库（如果还没有）

```bash
# 初始化 Git
git init

# 查看当前状态
git status
```

### 3. 配置 Git 用户信息（首次使用）

```bash
# 设置用户名
git config --global user.name "你的名字"

# 设置邮箱
git config --global user.email "your-email@example.com"

# 验证配置
git config --global --list
```

---

## 📝 第三步：准备提交代码

### 1. 检查 .gitignore 文件

确保 `.gitignore` 文件包含以下内容：

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
*$py.class
*.so
.Python
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# 操作系统
.DS_Store
Thumbs.db

# 日志
*.log

# 临时文件
*.tmp
*.bak
```

### 2. 添加文件到暂存区

```bash
# 查看将要添加的文件
git status

# 添加所有文件
git add .

# 或者选择性添加
git add README.md
git add backend/
git add frontend/
git add *.md
```

### 3. 创建第一次提交

```bash
git commit -m "Initial commit: CommentGenie - AI-powered student comment generator"
```

---

## 🔗 第四步：连接远程仓库

### 1. 添加远程仓库

```bash
# 添加远程仓库（替换为你的 GitHub 用户名）
git remote add origin https://github.com/你的用户名/CommentGenie.git

# 验证远程仓库
git remote -v
```

### 2. 重命名分支为 main（如果需要）

```bash
# 查看当前分支
git branch

# 如果是 master，重命名为 main
git branch -M main
```

### 3. 推送代码到 GitHub

```bash
# 首次推送（设置上游分支）
git push -u origin main

# 如果遇到认证问题，可能需要使用 Personal Access Token
```

---

## 🔑 第五步：配置 GitHub 认证

### 方法1：使用 Personal Access Token（推荐）

**1. 生成 Token**：
- 访问：https://github.com/settings/tokens
- 点击 "Generate new token" → "Generate new token (classic)"
- 勾选权限：
  - ✅ repo（完整仓库访问）
  - ✅ workflow（如果需要 GitHub Actions）
- 点击 "Generate token"
- **立即复制 Token**（只显示一次！）

**2. 使用 Token 推送**：
```bash
# 推送时会提示输入用户名和密码
# 用户名：你的 GitHub 用户名
# 密码：粘贴刚才复制的 Token
git push -u origin main
```

**3. 保存凭据（可选）**：
```bash
# Windows
git config --global credential.helper wincred

# Mac
git config --global credential.helper osxkeychain

# Linux
git config --global credential.helper store
```

### 方法2：使用 SSH（高级）

**1. 生成 SSH 密钥**：
```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

**2. 添加到 GitHub**：
- 复制公钥：`cat ~/.ssh/id_ed25519.pub`
- 访问：https://github.com/settings/keys
- 点击 "New SSH key"
- 粘贴公钥并保存

**3. 修改远程仓库 URL**：
```bash
git remote set-url origin git@github.com:你的用户名/CommentGenie.git
```

---

## 📋 第六步：配置仓库设置

### 1. 添加 Topics（标签）

在 GitHub 仓库页面：
1. 点击右侧的 ⚙️ 图标（About 部分）
2. 添加 Topics：
   ```
   ai, education, flask, python, student-comments,
   teacher-tools, comment-generator, deepseek,
   zhipu-ai, web-application
   ```

### 2. 设置 About 描述

在 About 部分填写：
```
🧚 评语精灵 - 基于 AI 的学生评语智能生成工具，让每一句评语都有温度
```

Website（可选）：
```
https://your-app.vercel.app
```

### 3. 添加 README Badges（可选）

在 README.md 顶部添加徽章：

```markdown
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![Stars](https://img.shields.io/github/stars/你的用户名/CommentGenie?style=social)](https://github.com/你的用户名/CommentGenie)
```

---

## 🔒 第七步：安全检查

### 1. 确认敏感文件未提交

```bash
# 检查是否有 .env 文件被提交
git ls-files | grep .env

# 如果误提交了，立即删除
git rm --cached backend/.env
git commit -m "Remove .env file from repository"
git push
```

### 2. 添加 LICENSE 文件

创建 `LICENSE` 文件（MIT License 示例）：

```
MIT License

Copyright (c) 2026 你的名字

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

提交 LICENSE：
```bash
git add LICENSE
git commit -m "Add MIT License"
git push
```

---

## 📊 第八步：启用 GitHub Features

### 1. 启用 Issues

在仓库页面：
- Settings → Features → Issues ✅

### 2. 启用 Discussions（可选）

- Settings → Features → Discussions ✅

### 3. 设置分支保护（可选）

- Settings → Branches → Add rule
- Branch name pattern: `main`
- 勾选：
  - ✅ Require pull request reviews before merging
  - ✅ Require status checks to pass before merging

---

## 🔄 日常使用流程

### 提交新更改

```bash
# 1. 查看修改
git status
git diff

# 2. 添加文件
git add .

# 3. 提交
git commit -m "描述你的修改"

# 4. 推送到 GitHub
git push
```

### 拉取最新代码

```bash
# 拉取远程更新
git pull origin main
```

### 创建新分支

```bash
# 创建并切换到新分支
git checkout -b feature/new-feature

# 推送新分支
git push -u origin feature/new-feature
```

---

## 🎯 完整命令速查

```bash
# 初始化和配置
git init
git config --global user.name "你的名字"
git config --global user.email "your-email@example.com"

# 添加和提交
git add .
git commit -m "提交信息"

# 连接远程仓库
git remote add origin https://github.com/你的用户名/CommentGenie.git
git branch -M main
git push -u origin main

# 日常操作
git status          # 查看状态
git diff            # 查看修改
git log             # 查看历史
git pull            # 拉取更新
git push            # 推送更新

# 分支操作
git branch          # 查看分支
git checkout -b 分支名  # 创建新分支
git merge 分支名     # 合并分支
```

---

## ❓ 常见问题

### 1. 推送时提示认证失败

**解决**：使用 Personal Access Token 而不是密码

### 2. 误提交了敏感文件

**解决**：
```bash
git rm --cached 文件名
git commit -m "Remove sensitive file"
git push
```

### 3. 想要撤销最后一次提交

**解决**：
```bash
# 保留修改
git reset --soft HEAD~1

# 不保留修改
git reset --hard HEAD~1
```

### 4. 远程仓库地址错误

**解决**：
```bash
git remote set-url origin https://github.com/正确的用户名/CommentGenie.git
```

---

## ✅ 检查清单

创建仓库后，确认以下事项：

- [ ] 仓库已成功创建
- [ ] 代码已推送到 GitHub
- [ ] .env 文件未被提交
- [ ] README.md 显示正常
- [ ] About 描述已填写
- [ ] Topics 标签已添加
- [ ] LICENSE 文件已添加
- [ ] .gitignore 配置正确

---

## 🎉 完成！

现在你的项目已经成功托管在 GitHub 上了！

**仓库地址**：`https://github.com/你的用户名/CommentGenie`

**下一步**：
1. 配置 Vercel 和 Railway 自动部署
2. 邀请协作者（如果需要）
3. 开始接受 Issues 和 Pull Requests
4. 分享给更多人使用

---

## 📚 相关资源

- [GitHub 官方文档](https://docs.github.com/)
- [Git 官方文档](https://git-scm.com/doc)
- [GitHub Desktop](https://desktop.github.com/) - 图形化 Git 工具
- [Git 速查表](https://training.github.com/downloads/zh_CN/github-git-cheat-sheet/)
