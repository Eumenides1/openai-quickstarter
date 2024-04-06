import os

from langchain import OpenAI

api_base = os.getenv("OPENAI_API_BASE")
api_key = os.getenv("MY_API_KEY")

# 构造一个llm
llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0,
    openai_api_key=api_key,
    openai_api_base=api_base,
    max_tokens=512,
)

for chunk in llm.stream("写一首关于秋天的诗歌"):
    print(chunk,end="",flush=False)