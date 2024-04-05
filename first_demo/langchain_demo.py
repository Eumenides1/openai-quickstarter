import os

from langchain.llms import OpenAI

api_base = os.getenv("OPENAI_API_BASE")
api_key = os.getenv("MY_API_KEY")
llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0,
    openai_api_key=api_key,
    openai_api_base=api_base,
)
print(llm.predict("我要做一个应用，用来解释代码，给这个应用起一个英文名字吧"))
