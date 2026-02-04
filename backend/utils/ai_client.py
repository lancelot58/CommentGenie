"""
AI 客户端工具
支持多个国内主流 AI API
"""

import requests
import os
from typing import Optional, Dict


class AIClient:
    """AI 客户端基类"""

    def __init__(self, api_key: str):
        self.api_key = api_key

    def generate_comment(self, student_name: str, student_info: str) -> str:
        """
        生成学生评语

        参数:
            student_name: 学生姓名
            student_info: 学生信息

        返回:
            生成的评语
        """
        raise NotImplementedError("子类必须实现此方法")


class DeepSeekClient(AIClient):
    """DeepSeek AI 客户端"""

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = "https://api.deepseek.com/v1/chat/completions"

    def generate_comment(self, student_name: str, student_info: str) -> str:
        """使用 DeepSeek 生成评语"""

        # 构建提示词
        prompt = f"""你是一位经验丰富的班主任老师，请根据以下学生信息，生成一段真诚、具体、有温度的学生评语。

学生姓名：{student_name}
学生情况：{student_info}

要求：
1. 评语要真诚、具体，避免空洞的套话
2. 突出学生的优点和进步
3. 如果有不足，要委婉地提出改进建议
4. 语气要温暖、鼓励，体现对学生的关心
5. 字数控制在150-200字左右
6. 直接输出评语内容，不要有其他说明

请生成评语："""

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }

        try:
            response = requests.post(
                self.base_url,
                headers=headers,
                json=data,
                timeout=30
            )
            response.raise_for_status()

            result = response.json()
            comment = result['choices'][0]['message']['content'].strip()
            return comment

        except requests.exceptions.RequestException as e:
            raise Exception(f"DeepSeek API 调用失败: {str(e)}")


class ZhipuClient(AIClient):
    """智谱 AI（GLM-4）客户端"""

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

    def generate_comment(self, student_name: str, student_info: str) -> str:
        """使用智谱 AI 生成评语"""

        prompt = f"""你是一位经验丰富的班主任老师，请根据以下学生信息，生成一段真诚、具体、有温度的学生评语。

学生姓名：{student_name}
学生情况：{student_info}

要求：
1. 评语要真诚、具体，避免空洞的套话
2. 突出学生的优点和进步
3. 如果有不足，要委婉地提出改进建议
4. 语气要温暖、鼓励，体现对学生的关心
5. 字数控制在150-200字左右
6. 直接输出评语内容，不要有其他说明

请生成评语："""

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": "glm-4",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }

        try:
            response = requests.post(
                self.base_url,
                headers=headers,
                json=data,
                timeout=30
            )
            response.raise_for_status()

            result = response.json()
            comment = result['choices'][0]['message']['content'].strip()
            return comment

        except requests.exceptions.RequestException as e:
            raise Exception(f"智谱 AI API 调用失败: {str(e)}")


class QwenClient(AIClient):
    """通义千问客户端"""

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"

    def generate_comment(self, student_name: str, student_info: str) -> str:
        """使用通义千问生成评语"""

        prompt = f"""你是一位经验丰富的班主任老师，请根据以下学生信息，生成一段真诚、具体、有温度的学生评语。

学生姓名：{student_name}
学生情况：{student_info}

要求：
1. 评语要真诚、具体，避免空洞的套话
2. 突出学生的优点和进步
3. 如果有不足，要委婉地提出改进建议
4. 语气要温暖、鼓励，体现对学生的关心
5. 字数控制在150-200字左右
6. 直接输出评语内容，不要有其他说明

请生成评语："""

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": "qwen-turbo",
            "input": {
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            },
            "parameters": {
                "temperature": 0.7,
                "max_tokens": 500
            }
        }

        try:
            response = requests.post(
                self.base_url,
                headers=headers,
                json=data,
                timeout=30
            )
            response.raise_for_status()

            result = response.json()
            comment = result['output']['text'].strip()
            return comment

        except requests.exceptions.RequestException as e:
            raise Exception(f"通义千问 API 调用失败: {str(e)}")


class KimiClient(AIClient):
    """Kimi（月之暗面）客户端"""

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = "https://api.moonshot.cn/v1/chat/completions"

    def generate_comment(self, student_name: str, student_info: str) -> str:
        """使用 Kimi 生成评语"""

        prompt = f"""你是一位经验丰富的班主任老师，请根据以下学生信息，生成一段真诚、具体、有温度的学生评语。

学生姓名：{student_name}
学生情况：{student_info}

要求：
1. 评语要真诚、具体，避免空洞的套话
2. 突出学生的优点和进步
3. 如果有不足，要委婉地提出改进建议
4. 语气要温暖、鼓励，体现对学生的关心
5. 字数控制在150-200字左右
6. 直接输出评语内容，不要有其他说明

请生成评语："""

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": "moonshot-v1-8k",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }

        try:
            response = requests.post(
                self.base_url,
                headers=headers,
                json=data,
                timeout=30
            )
            response.raise_for_status()

            result = response.json()
            comment = result['choices'][0]['message']['content'].strip()
            return comment

        except requests.exceptions.RequestException as e:
            raise Exception(f"Kimi API 调用失败: {str(e)}")


def get_ai_client(model_name: str = 'deepseek') -> Optional[AIClient]:
    """
    获取 AI 客户端实例

    参数:
        model_name: AI 模型名称（deepseek, zhipu, qwen, kimi）

    返回:
        AI 客户端实例，如果未配置则返回 None
    """

    model_name = model_name.lower()

    # 根据模型名称获取对应的 API Key
    api_key_map = {
        'deepseek': os.getenv('DEEPSEEK_API_KEY'),
        'zhipu': os.getenv('ZHIPU_API_KEY'),
        'qwen': os.getenv('QWEN_API_KEY'),
        'kimi': os.getenv('KIMI_API_KEY')
    }

    # 客户端类映射
    client_map = {
        'deepseek': DeepSeekClient,
        'zhipu': ZhipuClient,
        'qwen': QwenClient,
        'kimi': KimiClient
    }

    api_key = api_key_map.get(model_name)
    client_class = client_map.get(model_name)

    if not api_key:
        raise ValueError(f"未配置 {model_name} 的 API Key，请在 .env 文件中配置")

    if not client_class:
        raise ValueError(f"不支持的 AI 模型: {model_name}")

    return client_class(api_key)


# 测试代码
if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()

    print("[TEST] 测试 AI 客户端...")

    # 测试数据
    student_name = "张三"
    student_info = "性格开朗，成绩优秀，积极参加班级活动，乐于助人"

    # 测试 DeepSeek
    try:
        print("\n[1] 测试 DeepSeek...")
        client = get_ai_client('deepseek')
        comment = client.generate_comment(student_name, student_info)
        print(f"[OK] 生成的评语:\n{comment}")
    except Exception as e:
        print(f"[FAIL] {str(e)}")

    # 测试智谱
    try:
        print("\n[2] 测试智谱 AI...")
        client = get_ai_client('zhipu')
        comment = client.generate_comment(student_name, student_info)
        print(f"[OK] 生成的评语:\n{comment}")
    except Exception as e:
        print(f"[FAIL] {str(e)}")

    print("\n[OK] 测试完成！")
