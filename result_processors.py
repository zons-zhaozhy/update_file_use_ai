import abc
import re

class ResultProcessor(abc.ABC):
    """
    结果处理器的抽象基类。
    定义了处理API响应的接口。
    """
    @abc.abstractmethod
    def process(self, response):
        """
        处理API响应的抽象方法。

        参数:
        response (dict): API的响应数据

        返回:
        str: 处理后的结果
        """
        pass

class TestCaseProcessor(ResultProcessor):
    """
    处理测试用例生成结果的处理器。
    """
    def process(self, response):
        """
        从API响应中提取Java测试代码。

        参数:
        response (dict): API的响应数据,预期包含'generated_code'键

        返回:
        str: 提取的Java测试代码,如果没有找到则返回空字符串
        """
        # 假设 API 返回的是包含 Java 代码的 JSON
        java_code = response.get('generated_code', '')
        # 使用正则表达式提取 Java 代码
        match = re.search(r'```java\n(.*?)```', java_code, re.DOTALL)
        if match:
            return match.group(1)
        return ''

class CodeReviewProcessor(ResultProcessor):
    """
    处理代码审查结果的处理器。
    """
    def process(self, response):
        """
        从API响应中提取代码审查结果。

        参数:
        response (dict): API的响应数据,预期包含'code_review'键

        返回:
        str: 格式化的代码审查结果
        """
        review = response.get('code_review', '')
        return f"Code Review:\n{review}"

class BugFixProcessor(ResultProcessor):
    """
    处理bug修复结果的处理器。
    """
    def process(self, response):
        """
        从API响应中提取bug修复结果和解释。

        参数:
        response (dict): API的响应数据,预期包含'fixed_code'和'explanation'键

        返回:
        str: 格式化的bug修复结果,包括修复后的代码和解释
        """
        fixed_code = response.get('fixed_code', '')
        explanation = response.get('explanation', '')
        return f"Fixed Code:\n{fixed_code}\n\nExplanation:\n{explanation}"

class DocumentationProcessor(ResultProcessor):
    """
    处理文档生成结果的处理器。
    """
    def process(self, response):
        """
        从API响应中提取生成的文档。

        参数:
        response (dict): API的响应数据,预期包含'documentation'键

        返回:
        str: 格式化的文档内容
        """
        docs = response.get('documentation', '')
        return f"Documentation:\n{docs}"

def get_result_processor(mode):
    """
    根据指定的模式返回相应的结果处理器实例。

    参数:
    mode (str): 处理模式,可选值包括"test_case", "code_review", "bug_fix", "documentation"

    返回:
    ResultProcessor: 对应模式的结果处理器实例
    """
    processors = {
        "test_case": TestCaseProcessor(),
        "code_review": CodeReviewProcessor(),
        "bug_fix": BugFixProcessor(),
        "documentation": DocumentationProcessor()
    }
    return processors.get(mode, ResultProcessor())