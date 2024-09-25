import abc
import aiohttp
import asyncio
import requests

class ModelAPIClient(abc.ABC):
    @abc.abstractmethod
    async def request(self, content, instruction):
        pass

class DeepSeekClient(ModelAPIClient):
    def __init__(self, config):
        self.base_url = config['base_url']
        self.api_key = config['api_key']
        self.timeout = aiohttp.ClientTimeout(total=config['timeout'])
    
    async def request(self, content, instruction):
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "content": content,
                "instruction": instruction
            }
            async with session.post(f"{self.base_url}/generate", headers=headers, json=data) as response:
                response.raise_for_status()
                return await response.json()

class OpenAIClient(ModelAPIClient):
    def __init__(self, config):
        self.api_key = config['api_key']
        self.model = config.get('model', 'gpt-3.5-turbo')
        self.timeout = aiohttp.ClientTimeout(total=config['timeout'])
    
    async def request(self, content, instruction):
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": instruction},
                    {"role": "user", "content": content}
                ]
            }
            async with session.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data) as response:
                response.raise_for_status()
                return await response.json()

class HuggingFaceClient(ModelAPIClient):
    def __init__(self, config):
        self.api_key = config['api_key']
        self.model = config['model']
        self.timeout = aiohttp.ClientTimeout(total=config['timeout'])
    
    async def request(self, content, instruction):
        async with aiohttp.ClientSession(timeout=self.timeout) as session:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "inputs": f"{instruction}\n\n{content}",
                "parameters": {"max_length": 2048}
            }
            async with session.post(f"https://api-inference.huggingface.co/models/{self.model}", headers=headers, json=data) as response:
                response.raise_for_status()
                return await response.json()

class APIClient(ModelAPIClient):
    def __init__(self, config):
        self.api_key = config['api_key']
    
    async def request(self, content, instruction):
        # 模拟API请求
        return {'result': 'Success'}

# 确保类被正确定义和导出

# 其他模型平台的客户端类也应该继承自 ModelAPIClient 并实现 request 方法。