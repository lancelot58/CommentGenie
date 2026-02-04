# -*- coding: utf-8 -*-
"""
API 测试脚本
用于快速测试后端 API 接口
"""

import requests
import json

# 服务器地址
BASE_URL = 'http://localhost:5000'

def print_response(title, response):
    """打印响应结果"""
    print(f"\n{'='*50}")
    print(f"{title}")
    print(f"{'='*50}")
    print(f"状态码: {response.status_code}")
    print(f"响应内容:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))

def test_api():
    """测试所有 API 接口"""

    # 1. 测试服务器
    print("\n[1] 测试服务器连接...")
    response = requests.get(f'{BASE_URL}/')
    print_response("服务器状态", response)

    # 2. 注册用户
    print("\n[2] 测试用户注册...")
    register_data = {
        'username': 'testuser',
        'password': '123456',
        'email': 'test@example.com'
    }
    response = requests.post(f'{BASE_URL}/api/register', json=register_data)
    print_response("用户注册", response)

    # 3. 登录
    print("\n[3] 测试用户登录...")
    login_data = {
        'username': 'testuser',
        'password': '123456'
    }
    response = requests.post(f'{BASE_URL}/api/login', json=login_data)
    print_response("用户登录", response)

    if response.status_code == 200:
        token = response.json()['token']
        print(f"\n[OK] 获取到 Token: {token[:50]}...")

        # 4. 获取用户信息
        print("\n[4] 测试获取用户信息...")
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(f'{BASE_URL}/api/user/info', headers=headers)
        print_response("用户信息", response)

        # 5. 生成评语
        print("\n[5] 测试生成评语...")
        comment_data = {
            'student_name': '张三',
            'student_info': '性格开朗，成绩优秀，积极参加班级活动',
            'ai_model': 'deepseek'
        }
        response = requests.post(
            f'{BASE_URL}/api/comment/generate',
            json=comment_data,
            headers=headers
        )
        print_response("生成评语", response)

        # 6. 获取评语历史
        print("\n[6] 测试获取评语历史...")
        response = requests.get(
            f'{BASE_URL}/api/comment/history?limit=10',
            headers=headers
        )
        print_response("评语历史", response)

    print("\n" + "="*50)
    print("[OK] 所有测试完成！")
    print("="*50)

if __name__ == '__main__':
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("\n[ERROR] 无法连接到服务器！")
        print("请确保服务器正在运行: python app.py")
    except Exception as e:
        print(f"\n[ERROR] 测试失败: {str(e)}")
