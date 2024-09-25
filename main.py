import argparse
import asyncio
import logging
from pathlib import Path
import yaml
from api_client import DeepSeekClient, OpenAIClient, HuggingFaceClient

from file_handlers import get_file_handler
from result_processors import get_result_processor
from utils import setup_logging, create_progress_bar

def get_api_client(config):
    """
    根据配置创建并返回相应的API客户端。

    参数:
    config (dict): 包含API配置信息的字典。

    返回:
    ModelAPIClient: 对应平台的API客户端实例。

    异常:
    ValueError: 如果指定了不支持的平台。
    """
    platform = config['api']['platform']
    if platform == "deepseek":
        return DeepSeekClient(config['api']['deepseek'])
    elif platform == "openai":
        return OpenAIClient(config['api']['openai'])
    elif platform == "huggingface":
        return HuggingFaceClient(config['api']['huggingface'])
    else:
        raise ValueError(f"Unsupported platform: {platform}")

async def process_file(file_path, file_handler, api_client, result_processor, instruction):
    """
    异步处理单个文件。

    参数:
    file_path (Path): 要处理的文件路径。
    file_handler (FileHandler): 用于读写文件的处理器。
    api_client (ModelAPIClient): 用于发送API请求的客户端。
    result_processor (ResultProcessor): 用于处理API响应的处理器。
    instruction (str): 发送给AI模型的指令。

    返回:
    bool: 处理成功返回True,否则返回False。
    """
    try:
        # 读取文件内容
        content = file_handler.read(file_path)
        # 发送API请求
        response = await api_client.request(content, instruction)
        # 处理API响应
        result = result_processor.process(response)
        # 写入处理结果
        file_handler.write(file_path, result)
        return True
    except Exception as e:
        logging.error(f"Error processing {file_path}: {str(e)}")
        return False

async def main(args, config):
    """
    主函数,协调整个文件处理流程。

    参数:
    args (Namespace): 命令行参数。
    config (dict): 配置信息。
    """
    # 设置日志
    setup_logging(config['logging'])
    
    # 获取文件处理器、API客户端和结果处理器
    file_handler = get_file_handler(args.file_type)
    api_client = get_api_client(config)
    result_processor = get_result_processor(args.mode)
    
    # 获取所有需要处理的文件
    files = list(Path(args.input_path).rglob(f"*.{args.file_type}"))
    progress_bar = create_progress_bar(len(files))
    
    # 创建异步任务
    tasks = []
    for file_path in files:
        task = asyncio.create_task(process_file(file_path, file_handler, api_client, result_processor, args.instruction))
        tasks.append(task)
    
    # 等待所有任务完成
    results = await asyncio.gather(*tasks)
    
    # 关闭进度条
    progress_bar.close()
    
    # 统计处理结果
    successful = sum(results)
    logging.info(f"Processed {successful} out of {len(files)} files successfully.")

if __name__ == "__main__":
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="Process files using AI API")
    parser.add_argument("input_path", help="Path to the input directory")
    parser.add_argument("--file-type", default="java", help="File type to process")
    parser.add_argument("--mode", choices=["test_case", "code_review", "bug_fix", "documentation"], default="test_case", help="Processing mode")
    parser.add_argument("--instruction", help="Instruction for AI API")
    
    args = parser.parse_args()
    
    # 读取配置文件
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    # 运行主函数
    asyncio.run(main(args, config))