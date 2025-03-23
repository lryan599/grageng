from typing import Any

import litellm


class LiteLLMEmbeddingClient:
    def __init__(self, model_name: str):
        self.model_name = model_name

    def embed(self, text: str, **kwargs: Any) -> list[float]:
        resp = litellm.embedding(model=self.model_name, input=text, **kwargs)
        return resp["data"][0]["embedding"]

    def embed_batch(self, text_list: list[str], **kwargs: Any) -> list[list[float]]:
        resp = litellm.embedding(model=self.model_name, input=text_list, **kwargs)
        return [item["embedding"] for item in resp["data"]]

    async def aembed(self, text: str, **kwargs: Any) -> list[float]:
        resp = await litellm.aembedding(model=self.model_name, input=text, **kwargs)
        return resp["data"][0]["embedding"]

    async def aembed_batch(
        self, text_list: list[str], **kwargs: Any
    ) -> list[list[float]]:
        resp = await litellm.aembedding(
            model=self.model_name, input=text_list, **kwargs
        )
        return [item["embedding"] for item in resp["data"]]


if __name__ == "__main__":
    import dotenv

    dotenv.load_dotenv()
    client = LiteLLMEmbeddingClient("openai/text-embedding-3-small")
    print(client.embed("你是谁？"))
    print(client.embed_batch(["你是谁？", "你是哪里的？"]))
