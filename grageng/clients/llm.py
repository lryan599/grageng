from typing import Any

import litellm

from grageng.clients.base import ModelResponse


class LiteLLMChatClient:
    def __init__(self, model_name: str):
        self.model_name = model_name

    def chat(
        self, prompt: str, history: list | None = None, **kwargs: Any
    ) -> ModelResponse:
        current_message = {"role": "user", "content": prompt}
        if "system_prompt" in kwargs:
            messages = [
                {"role": "system", "content": kwargs["system_prompt"]},
                current_message,
            ]
        else:
            messages = [current_message]
        if history is not None:
            messages = history + messages
        resp = litellm.completion(model=self.model_name, messages=messages, **kwargs)
        return resp["choices"][0]["message"]["content"]

    async def achat(
        self, prompt: str, history: list | None = None, **kwargs: Any
    ) -> ModelResponse:
        current_message = {"role": "user", "content": prompt}
        if "system_prompt" in kwargs:
            messages = [
                {"role": "system", "content": kwargs["system_prompt"]},
                current_message,
            ]
            kwargs.pop("system_prompt")
        else:
            messages = [current_message]
        if history is not None:
            messages = history + messages
        resp = await litellm.acompletion(
            model=self.model_name, messages=messages, **kwargs
        )
        return resp["choices"][0]["message"]["content"]


if __name__ == "__main__":
    client = LiteLLMChatClient("deepseek/deepseek-chat")
    print(client.chat("你是谁？"))
    import asyncio

    print(asyncio.run(client.achat("你是谁？")))
