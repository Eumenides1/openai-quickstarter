# 用文件管理提示词模板
from langchain.prompts import load_prompt

# 加载yaml格式的prompt模版
prompt_yml = load_prompt("simple_prompt.yaml")
print(prompt_yml.format(name="小黑", what="恐怖的"))

# 加载json格式的prompt模版
prompt_json = load_prompt("simple_prompt.json")
print(prompt_json.format(name="小红", what="搞笑的"))

# 支持加载文件格式的模版，并且对prompt的最终解析结果进行自定义格式化
prompt_parse = load_prompt("prompt_with_output_parser.json")
strs = prompt_parse.output_parser.parse(
    "George Washington was born in 1732 and died in 1799.\nScore: 1/2"
)
print(strs)
