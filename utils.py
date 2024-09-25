import logging
from tqdm import tqdm

def setup_logging(config):
    logging.basicConfig(
        level=config.get('level', logging.INFO),
        format=config.get('format', '%(asctime)s - %(name)s - %(levelname)s - %(message)s'),
        filename=config.get('file')  # 使用 get 方法，如果 'file' 键不存在则返回 None
    )
    logger = logging.getLogger(__name__)
    logger.setLevel(config.get('level', logging.INFO))
    return logger

def create_progress_bar(total_items):
    return tqdm(total=total_items, unit='item')