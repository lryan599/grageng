import litellm

resp = litellm.embedding(
    model="text-embedding-3-small", input="测试文本embedding，这是一段测试文本"
)

print(resp)
