import abc
import re

class ResultProcessor(abc.ABC):
    @abc.abstractmethod
    def process(self, response):
        pass

class TestCaseProcessor(ResultProcessor):
    def process(self, response):
        # 假设 API 返回的是包含 Java 代码的 JSON
        java_code = response.get('generated_code', '')
        # 使用正则表达式提取 Java 代码
        match = re.search(r'```java\n(.*?)```', java_code, re.DOTALL)
        if match:
            return match.group(1)
        return ''

class CodeReviewProcessor(ResultProcessor):
    def process(self, response):
        review = response.get('code_review', '')
        return f"Code Review:\n{review}"

class BugFixProcessor(ResultProcessor):
    def process(self, response):
        fixed_code = response.get('fixed_code', '')
        explanation = response.get('explanation', '')
        return f"Fixed Code:\n{fixed_code}\n\nExplanation:\n{explanation}"

class DocumentationProcessor(ResultProcessor):
    def process(self, response):
        docs = response.get('documentation', '')
        return f"Documentation:\n{docs}"

def get_result_processor(mode):
    processors = {
        "test_case": TestCaseProcessor(),
        "code_review": CodeReviewProcessor(),
        "bug_fix": BugFixProcessor(),
        "documentation": DocumentationProcessor()
    }
    return processors.get(mode, ResultProcessor())