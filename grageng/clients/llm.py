import litellm
import asyncio

messages = [{"content": "Hello, how are you?", "role": "user"}]


resp = asyncio.run(litellm.acompletion(
    model="deepseek/deepseek-chat",
    messages=[
        {
            "role": "user",
            "content": "你是谁？",
        }
    ],
))

print(resp)
