
import os
from doctran import Doctran

# 加载文档
with open("letter.txt") as f:
    content = f.read()

OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
OPENAI_API_KEY = os.getenv("MY_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo-16k"
OPENAI_TOKEN_LIMIT = 8000

doctrans = Doctran(
    openai_api_key=OPENAI_API_KEY,
    openai_model=OPENAI_MODEL,
    openai_token_limit=OPENAI_TOKEN_LIMIT,
)
documents = doctrans.parse(content=content)

# 总结文档
summary = documents.summarize(token_limit=100).execute()
print(summary.transformed_content)

# 翻译一下文档
translation = documents.translate(language="chinese").execute()
print(translation.transformed_content)

# 精炼文档，删除除了某个主题或关键词之外的内容，仅保留与主题相关的内容
refined = documents.refine(topics=["marketing","Development"]).execute()
print(refined.transformed_content)
