import os
from langchain.document_loaders import TextLoader, CSVLoader, DirectoryLoader, BSHTMLLoader, JSONLoader

api_base = os.getenv("OPENAI_API_BASE")
api_key = os.getenv("MY_API_KEY")

# 使用loader来加载markdown文本
loader = TextLoader("loader.md")
print(loader.load())

# loader = CSVLoader(file_path="loader.csv")
loader = CSVLoader(file_path="loader.csv", source_column="Location")
data = loader.load()
print(data)

# 使用loader来加载html文件
loader = BSHTMLLoader("loader.html")
data = loader.load()
print(data)

# loader = DirectoryLoader("目录地址",glob="指定加载说明格式的文件")
loader = DirectoryLoader(path="./example/", glob="*.xlsx")
docs = loader.load()
print(len(docs))

# 使用loader来加载json文件
loader = JSONLoader(
    file_path="simple_prompt.json", jq_schema=".template", text_content=True
)
data = loader.load()
print(data)
