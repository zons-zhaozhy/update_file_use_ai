# AI辅助编程系统

## 项目简介

update_file_use_ai 是一个基于AI技术的文件处理工具,专门用于批量处理和更新代码文件。它利用AI模型来分析、修改和生成代码,适用于代码审查、bug修复、测试用例生成和文档编写等多种场景。该系统提供了灵活的配置选项、详细的日志记录和直观的进度跟踪功能,使得大规模代码处理任务变得更加高效和可控。

## 开发说明

本项目全程由AI辅助编程工具Cursor开发完成。Cursor是一款强大的AI编程助手,能够帮助开发者更高效地编写代码、解决问题和学习新技术。

## 主要功能

1. **AI辅助代码处理**：
   - 利用AI模型智能分析和修改代码 
   - 支持多种编程语言（如Java、Python、JavaScript、C++等）
   - 提供多种处理模式：测试用例生成、代码审查、bug修复、文档生成

2. **批量文件处理**：
   - 递归处理指定目录及其子目录中的所有匹配文件
   - 支持按文件类型筛选处理对象

3. **灵活的配置系统**：
   - 通过命令行参数和配置文件自定义处理为
   - 支持设置AI模型参数、API密钥等重要信息

4. **详细的日志记录**：
   - 配置和初始化日志系统
   - 支持自定义日志级别、格式和输出位置
   - 便于跟踪应用程序的运行状态和调试

5. **可视化进度跟踪**：
   - 生成实时更新的进度条
   - 显示处理进度和预估完成时间

6. **错误处理和重试机制**：
   - 实现最大重试次数和超时设置
   - 确保在网络不稳定等情况下的稳定运行

## 安装要求

### 依赖库

本项目依赖以下Python库：

- `logging`：Python内置日志库
- `tqdm`：用于创建进度条
- `argparse`：用于解析命令行参数

### 安装步骤

1. 克隆项目仓库：
   ```bash
   git clone https://github.com/zons-zhaozhy/update_file_use_ai.git
   cd update_file_use_ai
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 使用说明

### 设置日志

使用`setup_logging`函数来配置日志系统：

```python
from utils import setup_logging

log_config = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'filename': 'app.log'
}

logger = setup_logging(log_config)
```

### 创建进度条

使用`create_progress_bar`函数来创建进度条：

```python
from utils import create_progress_bar

total_items = 100
progress_bar = create_progress_bar(total_items)

for item in items:
    # 处理项目
    progress_bar.update(1)
```

### 运行程序

使用以下命令运行主程序：

```
python main.py /path/to/input/directory --file-type java --mode <processing_mode> --instruction "<instruction>"
```

参数说明：
- `/path/to/input/directory`：输入文件目录。程序会递归处理该目录及其所有子目录中的文件。
- `--file-type`：要处理的文件类型（如 java、py 等）
- `--mode`：处理模式，可选值包括：
  - `test_case`: 生成单元测试用例
  - `code_review`: 进行代码审查
  - `bug_fix`: 修复代码中的bug
  - `documentation`: 生成代码文档
- `--instruction`：处理指令，用于指导AI模型的行为

示例：

1. 生成Java单元测试：
   ```
   python main.py ./src --file-type java --mode test_case --instruction "Generate unit tests for this Java class"
   ```

2. 进行代码审查：
   ```
   python main.py ./src --file-type python --mode code_review --instruction "Review this Python code for best practices and potential improvements"
   ```

3. 修复代码中的bug：
   ```
   python main.py ./src --file-type javascript --mode bug_fix --instruction "Identify and fix any bugs in this JavaScript code"
   ```

4. 生成代码文档：
   ```
   python main.py ./src --file-type cpp --mode documentation --instruction "Generate comprehensive documentation for this C++ code"
   ```

注意：程序会自动遍历指定目录及其所有子目录,处理所有匹配指定文件类型的文件。

## 测试

本项目使用Python的`unittest`模块进行单元测试。测试文件为`test_update_file_use_ai.py`。

### 运行测试

要运行测试，请在项目根目录执行以下命令：

```
python
```

## 配置选项

可以通过修改`config.py`文件来自定义程序的行为：

- `MAX_RETRIES`：最大重试次数
- `TIMEOUT`：请求超时时间
- `BATCH_SIZE`：批处理大小

## 贡献指南

我们热烈欢迎其他开源开发者为本项目做出贡献!无论是提出新的想法、报告问题还是提交代码,您的参与都将帮助我们不断改进这个AI辅助编程系统。如果您有兴趣参与,请遵循以下步骤：

1. Fork 本仓库
2. 创建您的特性分支 (git checkout -b feature/AmazingFeature)
3. 提交您的更改 (git commit -m 'Add some AmazingFeature')
4. 将您的更改推送到分支 (git push origin feature/AmazingFeature)
5. 开启一个Pull Request

我们期待看到您的创意和贡献!

## 文件结构

项目包含以下主要文件：

- `main.py`: 主程序入口
- `utils.py`: 通用工具函数
- `result_processors.py`: 结果处理器
- `api_client.py`: API客户端
- `config.yaml`: 配置文件
- `file_handlers.py`: 文件处理器

## 配置

请参考 `config.yaml` 文件进行配置。您可以在此文件中设置AI模型参数、API密钥等重要信息。

## 贡献

我们欢迎各种形式的贡献,包括但不限于报告问题、提交改进建议和代码贡献。请参考贡献指南部分了解详细流程。

## 许可证

本项目采用 MIT 许可证。详情请查阅 [LICENSE](LICENSE) 文件。

## 联系方式

如有任何问题或建议，请通过以下方式联系我们：

- 项目维护者：zons-zhaozhy
- 电子邮件：zhaozhy_zons@163.com
- 项目 GitHub 主页：https://github.com/zons-zhaozhy/update_file_use_ai

## 致谢

感谢所有为这个项目做出贡献的开发者和用户。您的支持是我们不断改进的动力。

## Prompt 提示词指南

为了获得最佳的AI处理结果,针对不同的大模型平台,我们建议使用以下prompt提示词策略:

### DeepSeek

1. **明确指令**: 在指令开始时使用明确的动作词,如"生成"、"分析"、"总结"等。
2. **上下文提供**: 简要说明任务背景和期望输出。
3. **格式指定**: 明确指定所需的输出格式。
4. **示例提供**: 如果可能,提供一个期望输出的示例。
5. **限制说明**: 明确指出任何限制或约束条件。

示例:
```
生成一个Python函数，用于计算给定列表中的最大值和最小值。
上下文：这个函数将用于数据分析项目中。
输出格式：请提供完整的函数定义，包括函数名、参数和返回值。
限制：不要使用内置的max()和min()函数。
示例输出：
def find_max_min(numbers):
    # 函数实现
    return max_value, min_value
```

### GPT系列 (如GPT-3.5, GPT-4)

1. **角色设定**: 为AI设定一个特定的角色,如"你是一位经验丰富的Python开发者"。
2. **任务描述**: 清晰描述需要完成的任务。
3. **步骤引导**: 如果任务复杂,可以将其分解为多个步骤。
4. **输出规范**: 指定期望的输出格式和风格。
5. **知识深度**: 指明所需的专业程度或技术深度。

示例:
```
角色：你是一位精通代码优化的高级Python开发者。
任务：请审查并优化以下Python代码片段，提高其性能和可读性。
步骤：
1. 分析代码的时间复杂度
2. 识别可能的性能瓶颈
3. 提供优化建议
4. 重写优化后的代码
输出：请提供详细的分析报告，包括原始代码的问题、优化建议和重写后的代码。
专业度：请使用高级Python概念和最佳实践。

[在此插入需要优化的代码]
```

### Claude系列

1. **明确目标**: 清晰陈述您想要达成的目标。
2. **背景信息**: 提供必要的背景信息或上下文。
3. **输出结构**: 指定期望的输出结构或格式。
4. **交互性**: 鼓励AI提出澄清性问题或请求额外信息。
5. **评估标准**: 如果适用,提供评估输出质量的标准。

示例:
```
目标：创建一个简洁的技术文档，解释RESTful API的核心概念。
背景：这份文档将用于培训初级开发人员。
输出结构：
1. 简介
2. RESTful API的关键原则（列表形式）
3. HTTP方法及其用途（表格形式）
4. 示例API端点及其解释
5. 最佳实践总结

请在需要时提出任何澄清性问题。文档应该易于理解，同时保持技术准确性。
评估标准：清晰度、准确性和对初学者的适用性。
```

通过遵循这些指南并根据具体任务和目标平台进行调整,您可以显著提高AI生成内容的质量和相关性。