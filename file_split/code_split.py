from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    Language,
)

# 支持解析的编程语言
# [e.value for e in Language]

# 要切割的代码文档
PYTHON_CODE = """
def hello_world():
    print("Hello, World!")
#调用函数
hello_world()
"""
py_spliter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=50,
    chunk_overlap=10,
)
python_docs = py_spliter.create_documents([PYTHON_CODE])
print(python_docs)
