"""
数据库模型定义
使用 SQLite 数据库存储用户和评语数据
"""

import sqlite3
import bcrypt
from datetime import datetime
import os


class Database:
    """数据库管理类"""

    def __init__(self, db_path='database.db'):
        """
        初始化数据库连接

        参数:
            db_path: 数据库文件路径
        """
        self.db_path = db_path
        self.init_database()

    def get_connection(self):
        """获取数据库连接"""
        conn = sqlite3.connect(self.db_path)
        # 让查询结果以字典形式返回，方便使用
        conn.row_factory = sqlite3.Row
        return conn

    def init_database(self):
        """初始化数据库表结构"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # 创建用户表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                email TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # 创建评语表
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                student_name TEXT NOT NULL,
                student_info TEXT,
                generated_comment TEXT NOT NULL,
                ai_model TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        conn.commit()
        conn.close()
        print("[OK] 数据库表创建成功")


class User:
    """用户模型"""

    @staticmethod
    def create(username, password, email=None):
        """
        创建新用户

        参数:
            username: 用户名
            password: 密码（明文，会自动加密）
            email: 邮箱（可选）

        返回:
            成功返回用户ID，失败返回None
        """
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        try:
            # 使用 bcrypt 加密密码
            password_hash = bcrypt.hashpw(
                password.encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')

            cursor.execute(
                'INSERT INTO users (username, password_hash, email) VALUES (?, ?, ?)',
                (username, password_hash, email)
            )
            conn.commit()
            user_id = cursor.lastrowid
            conn.close()
            return user_id
        except sqlite3.IntegrityError:
            # 用户名已存在
            conn.close()
            return None

    @staticmethod
    def verify_password(username, password):
        """
        验证用户密码

        参数:
            username: 用户名
            password: 密码（明文）

        返回:
            验证成功返回用户信息字典，失败返回None
        """
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            'SELECT * FROM users WHERE username = ?',
            (username,)
        )
        user = cursor.fetchone()
        conn.close()

        if user and bcrypt.checkpw(
            password.encode('utf-8'),
            user['password_hash'].encode('utf-8')
        ):
            # 密码正确，返回用户信息（不包含密码）
            return {
                'id': user['id'],
                'username': user['username'],
                'email': user['email'],
                'created_at': user['created_at']
            }
        return None

    @staticmethod
    def get_by_id(user_id):
        """
        根据ID获取用户信息

        参数:
            user_id: 用户ID

        返回:
            用户信息字典，不存在返回None
        """
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            'SELECT id, username, email, created_at FROM users WHERE id = ?',
            (user_id,)
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            return dict(user)
        return None


class Comment:
    """评语模型"""

    @staticmethod
    def create(user_id, student_name, student_info, generated_comment, ai_model):
        """
        保存生成的评语

        参数:
            user_id: 用户ID
            student_name: 学生姓名
            student_info: 学生信息（性格、成绩等）
            generated_comment: 生成的评语
            ai_model: 使用的AI模型名称

        返回:
            评语ID
        """
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            '''INSERT INTO comments
               (user_id, student_name, student_info, generated_comment, ai_model)
               VALUES (?, ?, ?, ?, ?)''',
            (user_id, student_name, student_info, generated_comment, ai_model)
        )
        conn.commit()
        comment_id = cursor.lastrowid
        conn.close()
        return comment_id

    @staticmethod
    def get_by_user(user_id, limit=20):
        """
        获取用户的评语历史

        参数:
            user_id: 用户ID
            limit: 返回数量限制

        返回:
            评语列表
        """
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            '''SELECT * FROM comments
               WHERE user_id = ?
               ORDER BY created_at DESC
               LIMIT ?''',
            (user_id, limit)
        )
        comments = cursor.fetchall()
        conn.close()

        return [dict(comment) for comment in comments]

    @staticmethod
    def delete(comment_id, user_id):
        """
        删除评语（只能删除自己的）

        参数:
            comment_id: 评语ID
            user_id: 用户ID

        返回:
            成功返回True，失败返回False
        """
        db = Database()
        conn = db.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            'DELETE FROM comments WHERE id = ? AND user_id = ?',
            (comment_id, user_id)
        )
        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()
        return deleted


# 测试代码（仅在直接运行此文件时执行）
if __name__ == '__main__':
    print("[TEST] 测试数据库模型...")

    # 初始化数据库
    db = Database()

    # 测试创建用户
    print("\n1. 测试创建用户...")
    user_id = User.create('test_user', 'password123', 'test@example.com')
    if user_id:
        print(f"[OK] 用户创建成功，ID: {user_id}")
    else:
        print("[WARN] 用户已存在或创建失败")

    # 测试验证密码
    print("\n2. 测试验证密码...")
    user = User.verify_password('test_user', 'password123')
    if user:
        print(f"[OK] 密码验证成功: {user}")
    else:
        print("[FAIL] 密码验证失败")

    # 测试错误密码
    print("\n3. 测试错误密码...")
    user = User.verify_password('test_user', 'wrong_password')
    if user:
        print("[FAIL] 不应该验证成功")
    else:
        print("[OK] 正确拒绝了错误密码")

    # 测试创建评语
    if user_id:
        print("\n4. 测试创建评语...")
        comment_id = Comment.create(
            user_id=user_id,
            student_name='张三',
            student_info='性格开朗，成绩优秀',
            generated_comment='该生在本学期表现优异...',
            ai_model='DeepSeek'
        )
        print(f"[OK] 评语创建成功，ID: {comment_id}")

        # 测试获取评语历史
        print("\n5. 测试获取评语历史...")
        comments = Comment.get_by_user(user_id)
        print(f"[OK] 获取到 {len(comments)} 条评语")
        for c in comments:
            print(f"   - {c['student_name']}: {c['generated_comment'][:20]}...")

    print("\n[OK] 所有测试完成！")
