"""
Flask 主程序
这是后端服务器的入口文件
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from dotenv import load_dotenv
import os
from datetime import timedelta

# 导入数据库模型
from models import Database, User, Comment

# 导入 AI 客户端
from utils.ai_client import get_ai_client

# 加载环境变量（从 .env 文件）
load_dotenv()

# 创建 Flask 应用实例
app = Flask(__name__)

# ===== 配置部分 =====

# JWT 配置（用于用户登录验证）
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=7)  # Token 有效期7天

# 初始化 JWT
jwt = JWTManager(app)

# 配置 CORS（允许前端跨域访问）
# 开发环境允许所有来源，生产环境需要指定具体域名
CORS(app, resources={
    r"/api/*": {
        "origins": "*",  # 生产环境改为具体域名，如 "https://yourdomain.com"
        "methods": ["GET", "POST", "PUT", "DELETE"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# 初始化数据库
db = Database()

# ===== 路由部分 =====

@app.route('/')
def index():
    """
    首页路由 - 测试服务器是否正常运行
    访问: http://localhost:5000/
    """
    return jsonify({
        'message': '学生评语生成器 API',
        'version': '1.0.0',
        'status': 'running'
    })


@app.route('/api/register', methods=['POST'])
def register():
    """
    用户注册接口

    请求方法: POST
    请求地址: /api/register
    请求体: {
        "username": "用户名",
        "password": "密码",
        "email": "邮箱（可选）"
    }

    返回: {
        "success": true/false,
        "message": "提示信息",
        "user_id": 用户ID（成功时）
    }
    """
    try:
        # 获取请求数据
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        # 验证必填字段
        if not username or not password:
            return jsonify({
                'success': False,
                'message': '用户名和密码不能为空'
            }), 400

        # 验证用户名长度
        if len(username) < 3 or len(username) > 20:
            return jsonify({
                'success': False,
                'message': '用户名长度必须在3-20个字符之间'
            }), 400

        # 验证密码长度
        if len(password) < 6:
            return jsonify({
                'success': False,
                'message': '密码长度至少6个字符'
            }), 400

        # 创建用户
        user_id = User.create(username, password, email)

        if user_id:
            return jsonify({
                'success': True,
                'message': '注册成功',
                'user_id': user_id
            }), 201
        else:
            return jsonify({
                'success': False,
                'message': '用户名已存在'
            }), 409

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'服务器错误: {str(e)}'
        }), 500


@app.route('/api/login', methods=['POST'])
def login():
    """
    用户登录接口

    请求方法: POST
    请求地址: /api/login
    请求体: {
        "username": "用户名",
        "password": "密码"
    }

    返回: {
        "success": true/false,
        "message": "提示信息",
        "token": "JWT token"（成功时）,
        "user": 用户信息（成功时）
    }
    """
    try:
        # 获取请求数据
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # 验证必填字段
        if not username or not password:
            return jsonify({
                'success': False,
                'message': '用户名和密码不能为空'
            }), 400

        # 验证密码
        user = User.verify_password(username, password)

        if user:
            # 生成 JWT token（identity 必须是字符串）
            token = create_access_token(identity=str(user['id']))

            return jsonify({
                'success': True,
                'message': '登录成功',
                'token': token,
                'user': user
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': '用户名或密码错误'
            }), 401

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'服务器错误: {str(e)}'
        }), 500


@app.route('/api/user/info', methods=['GET'])
@jwt_required()
def get_user_info():
    """
    获取当前登录用户信息

    请求方法: GET
    请求地址: /api/user/info
    请求头: Authorization: Bearer <token>

    返回: {
        "success": true/false,
        "user": 用户信息
    }
    """
    try:
        # 从 token 中获取用户ID（转换为整数）
        user_id = int(get_jwt_identity())

        # 获取用户信息
        user = User.get_by_id(user_id)

        if user:
            return jsonify({
                'success': True,
                'user': user
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': '用户不存在'
            }), 404

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'服务器错误: {str(e)}'
        }), 500


@app.route('/api/comment/generate', methods=['POST'])
@jwt_required()
def generate_comment():
    """
    生成学生评语接口

    请求方法: POST
    请求地址: /api/comment/generate
    请求头: Authorization: Bearer <token>
    请求体: {
        "student_name": "学生姓名",
        "student_info": "学生信息（性格、成绩等）",
        "ai_model": "AI模型名称（可选，默认deepseek）"
    }

    返回: {
        "success": true/false,
        "comment": "生成的评语",
        "comment_id": 评语ID
    }
    """
    try:
        # 从 token 中获取用户ID（转换为整数）
        user_id = int(get_jwt_identity())

        # 获取请求数据
        data = request.get_json()
        student_name = data.get('student_name')
        student_info = data.get('student_info')
        ai_model = data.get('ai_model', 'deepseek')

        # 验证必填字段
        if not student_name or not student_info:
            return jsonify({
                'success': False,
                'message': '学生姓名和信息不能为空'
            }), 400

        # 使用 AI 生成评语
        try:
            ai_client = get_ai_client(ai_model)
            generated_comment = ai_client.generate_comment(student_name, student_info)
        except ValueError as e:
            # API Key 未配置
            return jsonify({
                'success': False,
                'message': str(e)
            }), 400
        except Exception as e:
            # AI API 调用失败
            return jsonify({
                'success': False,
                'message': f'AI 生成失败: {str(e)}'
            }), 500

        # 保存到数据库
        comment_id = Comment.create(
            user_id=user_id,
            student_name=student_name,
            student_info=student_info,
            generated_comment=generated_comment,
            ai_model=ai_model
        )

        return jsonify({
            'success': True,
            'comment': generated_comment,
            'comment_id': comment_id
        }), 200

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'服务器错误: {str(e)}'
        }), 500


@app.route('/api/comment/history', methods=['GET'])
@jwt_required()
def get_comment_history():
    """
    获取评语历史记录

    请求方法: GET
    请求地址: /api/comment/history?limit=20
    请求头: Authorization: Bearer <token>

    返回: {
        "success": true/false,
        "comments": [评语列表]
    }
    """
    try:
        # 从 token 中获取用户ID（转换为整数）
        user_id = int(get_jwt_identity())

        # 获取查询参数
        limit = request.args.get('limit', 20, type=int)

        # 获取评语历史
        comments = Comment.get_by_user(user_id, limit)

        return jsonify({
            'success': True,
            'comments': comments
        }), 200

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'服务器错误: {str(e)}'
        }), 500


@app.route('/api/comment/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete_comment(comment_id):
    """
    删除评语

    请求方法: DELETE
    请求地址: /api/comment/<comment_id>
    请求头: Authorization: Bearer <token>

    返回: {
        "success": true/false,
        "message": "提示信息"
    }
    """
    try:
        # 从 token 中获取用户ID（转换为整数）
        user_id = int(get_jwt_identity())

        # 删除评语
        success = Comment.delete(comment_id, user_id)

        if success:
            return jsonify({
                'success': True,
                'message': '删除成功'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': '评语不存在或无权删除'
            }), 404

    except Exception as e:
        return jsonify({
            'success': False,
            'message': f'服务器错误: {str(e)}'
        }), 500


# ===== 错误处理 =====

@app.errorhandler(404)
def not_found(error):
    """处理 404 错误"""
    return jsonify({
        'success': False,
        'message': '接口不存在'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """处理 500 错误"""
    return jsonify({
        'success': False,
        'message': '服务器内部错误'
    }), 500


# ===== 启动服务器 =====

if __name__ == '__main__':
    # 获取端口号（从环境变量或默认5000）
    port = int(os.getenv('PORT', 5000))

    print("=" * 50)
    print("学生评语生成器 API 服务器")
    print("=" * 50)
    print(f"服务器地址: http://localhost:{port}")
    print(f"API 文档: http://localhost:{port}/")
    print("=" * 50)

    # 启动服务器
    # debug=True: 开发模式，代码修改后自动重启
    # host='0.0.0.0': 允许外部访问
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True
    )
