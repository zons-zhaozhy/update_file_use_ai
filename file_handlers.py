import abc
from abc import ABC, abstractmethod
import os

class FileHandler(ABC):
    """
    文件处理器的抽象基类。
    定义了读取和写入文件的接口。
    """
    @abstractmethod
    def read(self, file_path):
        """
        读取文件内容的抽象方法。

        参数:
        file_path (str): 文件路径

        返回:
        str: 文件内容
        """
        pass
    
    @abstractmethod
    def write(self, file_path, content):
        """
        写入文件内容的抽象方法。

        参数:
        file_path (str): 文件路径
        content (str): 要写入的内容
        """
        pass

class ConcreteFileHandler(FileHandler):
    """
    通用文件处理器的具体实现。
    """
    def read(self, filename):
        """
        读取文件内容。

        参数:
        filename (str): 文件名

        返回:
        str: 文件内容
        """
        with open(filename, 'r') as file:
            return file.read()

    def write(self, filename, content):
        """
        写入文件内容。

        参数:
        filename (str): 文件名
        content (str): 要写入的内容
        """
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(filename, 'w') as file:
            file.write(content)

class JavaFileHandler(FileHandler):
    """
    Java文件处理器的具体实现。
    """
    def read(self, file_path):
        """
        读取Java文件内容。

        参数:
        file_path (str): 文件路径

        返回:
        str: 文件内容
        """
        with open(file_path, 'r') as f:
            return f.read()
    
    def write(self, file_path, content):
        """
        写入Java测试文件内容。

        参数:
        file_path (str): 原Java文件路径
        content (str): 要写入的测试内容
        """
        test_file_path = str(file_path).replace(".java", "Test.java")
        with open(test_file_path, 'w') as f:
            f.write(content)

def get_file_handler(file_type):
    """
    根据文件类型获取相应的文件处理器。

    参数:
    file_type (str): 文件类型

    返回:
    FileHandler: 对应文件类型的处理器实例
    """
    handlers = {
        "java": JavaFileHandler()
    }
    return handlers.get(file_type, ConcreteFileHandler())