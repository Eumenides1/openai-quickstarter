from langchain.text_splitter import RecursiveCharacterTextSplitter

# 加载要切割的文档
with open("test.txt") as f:
    poem = f.read()
# 初始化切割器
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,  # 切分的文本块大小，一般通过长度函数计算
    chunk_overlap=20,  # 切分的文本块重叠大小，一般通过长度函数计算
    length_function=len,  # 长度函数,也可以传递tokenize函数
    add_start_index=True,  # 是否添加起始索引
)

text = text_splitter.create_documents([poem])
print(text[0])
print(text[1])
