import os

from langchain import OpenAI
from langchain.callbacks import get_openai_callback

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


with get_openai_callback() as cb:
    result = llm.invoke("给我讲一个笑话")
    print(result)
    print(cb)