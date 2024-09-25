import abc
from abc import ABC, abstractmethod
import os

class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass
    
    @abstractmethod
    def write(self):
        pass

class ConcreteFileHandler(FileHandler):
    def read(self, filename):  # 将 read_file 改为 read
        with open(filename, 'r') as file:
            return file.read()

    def write(self, filename, content):  # 将 write_file 改为 write
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(filename, 'w') as file:
            file.write(content)

class JavaFileHandler(FileHandler):
    def read(self, file_path):
        with open(file_path, 'r') as f:
            return f.read()
    
    def write(self, file_path, content):
        test_file_path = str(file_path).replace(".java", "Test.java")
        with open(test_file_path, 'w') as f:
            f.write(content)

def get_file_handler(file_type):
    handlers = {
        "java": JavaFileHandler()
    }
    return handlers.get(file_type, FileHandler())