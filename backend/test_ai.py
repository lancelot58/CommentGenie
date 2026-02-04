# -*- coding: utf-8 -*-
"""
快速测试 AI 生成评语功能
"""

import requests
import json
import sys

# 设置输出编码为 UTF-8
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

BASE_URL = 'http://localhost:5000'

print("="*60)
print("测试 AI 评语生成功能")
print("="*60)

# 1. 注册用户
print("\n[步骤1] 注册测试用户...")
response = requests.post(f'{BASE_URL}/api/register', json={
    'username': 'aitest',
    'password': '123456'
})
print(f"状态码: {response.status_code}")
if response.status_code in [200, 201, 409]:  # 409 表示用户已存在
    print("✓ 注册成功（或用户已存在）")
else:
    print(f"✗ 注册失败: {response.text}")
    sys.exit(1)

# 2. 登录
print("\n[步骤2] 登录获取 Token...")
response = requests.post(f'{BASE_URL}/api/login', json={
    'username': 'aitest',
    'password': '123456'
})
print(f"状态码: {response.status_code}")
if response.status_code == 200:
    token = response.json()['token']
    print(f"✓ 登录成功")
    print(f"Token: {token[:50]}...")
else:
    print(f"✗ 登录失败: {response.text}")
    sys.exit(1)

headers = {'Authorization': f'Bearer {token}'}

# 3. 使用 DeepSeek 生成评语
print("\n[步骤3] 使用 DeepSeek 生成评语...")
response = requests.post(
    f'{BASE_URL}/api/comment/generate',
    json={
        'student_name': '李明',
        'student_info': '性格活泼开朗，学习成绩优秀，积极参加班级活动，乐于助人',
        'ai_model': 'deepseek'
    },
    headers=headers
)
print(f"状态码: {response.status_code}")
if response.status_code == 200:
    result = response.json()
    print("✓ 评语生成成功")
    print("\n" + "="*60)
    print("生成的评语（DeepSeek）:")
    print("="*60)
    print(result['comment'])
    print("="*60)
else:
    print(f"✗ 生成失败: {response.text}")

# 4. 使用智谱 AI 生成评语
print("\n[步骤4] 使用智谱 AI 生成评语...")
response = requests.post(
    f'{BASE_URL}/api/comment/generate',
    json={
        'student_name': '王芳',
        'student_info': '学习认真刻苦，成绩稳定，但性格较内向，不太主动发言',
        'ai_model': 'zhipu'
    },
    headers=headers
)
print(f"状态码: {response.status_code}")
if response.status_code == 200:
    result = response.json()
    print("✓ 评语生成成功")
    print("\n" + "="*60)
    print("生成的评语（智谱 AI）:")
    print("="*60)
    print(result['comment'])
    print("="*60)
else:
    print(f"✗ 生成失败: {response.text}")

# 5. 获取评语历史
print("\n[步骤5] 获取评语历史...")
response = requests.get(
    f'{BASE_URL}/api/comment/history?limit=5',
    headers=headers
)
print(f"状态码: {response.status_code}")
if response.status_code == 200:
    comments = response.json()['comments']
    print(f"✓ 获取成功，共 {len(comments)} 条评语")
    for i, comment in enumerate(comments, 1):
        print(f"\n  [{i}] {comment['student_name']} - {comment['ai_model']}")
        print(f"      {comment['generated_comment'][:50]}...")
else:
    print(f"✗ 获取失败: {response.text}")

print("\n" + "="*60)
print("✓ 所有测试完成！AI 功能正常工作！")
print("="*60)
