from langchain.text_splitter import CharacterTextSplitter

# 加载要切分的文档
with open("test.txt") as f:
    poem = f.read()

# 初始化切分器
text_splitter = CharacterTextSplitter(
    separator="。",  # 切割的标志字符，默认是\n\n
    chunk_size=50,  # 切分的文本块大小，一般通过长度函数计算
    chunk_overlap=20,  # 切分的文本块重叠大小，一般通过长度函数计算
    length_function=len,  # 长度函数,也可以传递tokenize函数
    add_start_index=True,  # 是否添加起始索引
    is_separator_regex=False,  # 是否是正则表达式
)
text = text_splitter.create_documents([poem])
print(text[0])
