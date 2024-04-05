import inspect
from typing import Any
from langchain.llms import OpenAI
import os

from langchain.prompts import StringPromptTemplate


# 定义一个简单的函数作为示例效果
def hello_world(abc):
    print("Hello, world!")
    return abc


PROMPT = """\
你是一个非常有经验和天赋的程序员，现在给你如下函数名称，你会按照如下格式，输出这段代码的名称、源代码、中文解释。
函数名称: {function_name}
源代码:
{source_code}
代码解释:
"""


def get_source_code(function_name):
    # 获得源代码
    return inspect.getsource(function_name)


class CustmPrompt(StringPromptTemplate):
    def format(self, **kwargs: Any) -> str:
        # 获得源代码
        source_code = get_source_code(kwargs["function_name"])
        # 生成提示词模板
        prompt = PROMPT.format(
            function_name=kwargs["function_name"].__name__, source_code=source_code
        )
        return prompt


a = CustmPrompt(input_variables=["function_name"])
pm = a.format(function_name=hello_world)

print(pm)

# 和LLM连接起来
api_base = os.getenv("OPENAI_API_BASE")
api_key = os.getenv("MY_API_KEY")

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0,
    openai_api_key=api_key,
    openai_api_base=api_base
)
msg = llm.predict(pm)
print(msg)
