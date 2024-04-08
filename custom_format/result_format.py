from langchain.llms import OpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.pydantic_v1 import BaseModel, Field, validator
import os

api_base = os.getenv("OPENAI_API_BASE")
api_key = os.getenv("MY_API_KEY")

# 构造LLM
model = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0,
    openai_api_key=api_key,
    openai_api_base=api_base,
)


# 定义个数据模型，用来描述最终的实例结构
class Joke(BaseModel):
    setup: str = Field(description="设置笑话的问题")
    punchline: str = Field(description="回答笑话的答案")

    # 验证问题是否符合要求
    @validator("setup")
    def question_mark(cls, field):
        if field[-1] != "？":
            raise ValueError("不符合预期的问题格式!")
        return field


# 将Joke数据模型传入
parser = PydanticOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="回答用户的输入.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt_and_model = prompt | model
out_put = prompt_and_model.invoke({"query": "给我讲一个笑话"})
print("out_put:", out_put)
parser.invoke(out_put)
