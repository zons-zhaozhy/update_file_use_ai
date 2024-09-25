import logging
from tqdm import tqdm

def setup_logging(config):
    """
    设置日志系统。

    参数:
    config (dict): 日志配置信息

    返回:
    logging.Logger: 配置好的日志记录器
    """
    logging.basicConfig(
        level=config.get('level', logging.INFO),
        format=config.get('format', '%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
        filename=config.get('file')  # 使用 get 方法，如果 'file' 键不存在则返回 None
    )
    logger = logging.getLogger(__name__)
    logger.setLevel(config.get('level', logging.INFO))
    return logger

def create_progress_bar(total_items):
    """
    创建进度条。

    参数:
    total_items (int): 总项目数

    返回:
    tqdm: 进度条对象
    """
    return tqdm(total=total_items, unit='item')