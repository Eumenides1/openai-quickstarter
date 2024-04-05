import os

import openai

openai.api_key = os.getenv("MY_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")
messages = [
    {
        "role": "user",
        "content": "介绍一下自己"
    }
]
res = openai.ChatCompletion.create(
    model="gpt-4-1106-preview",
    messages=messages,
    stream=False,
)
print(res['choices'][0]['message']['content'])
