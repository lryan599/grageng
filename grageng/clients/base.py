# Copyright (c) 2025 Microsoft Corporation.
# Licensed under the MIT License

"""Base llm protocol definitions."""

from __future__ import annotations

from collections.abc import AsyncGenerator, Generator
from typing import Any, Generic, Protocol, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T", bound=BaseModel, covariant=True)


class ModelOutput(Protocol):
    """Protocol for Model response's output object."""

    @property
    def content(self) -> str:
        """Return the textual content of the output."""
        ...


class ModelResponse(Protocol, Generic[T]):
    """Protocol for LLM response."""

    @property
    def output(self) -> ModelOutput:
        """Return the output of the response."""
        ...

    @property
    def parsed_response(self) -> T | None:
        """Return the parsed response."""
        ...

    @property
    def history(self) -> list:
        """Return the history of the response."""
        ...


class BaseModelOutput(BaseModel):
    """Base class for LLM output."""

    content: str = Field(..., description="The textual content of the output.")
    """The textual content of the output."""


class BaseModelResponse(BaseModel, Generic[T]):
    """Base class for a Model response."""

    output: BaseModelOutput
    """"""
    parsed_response: T | None = None
    """Parsed response."""
    history: list[Any] = Field(default_factory=list)
    """History of the response."""
    tool_calls: list = Field(default_factory=list)
    """Tool calls required by the Model. These will be instances of the LLM tools (with filled parameters)."""
    metrics: Any | None = None
    """Request/response metrics."""
    cache_hit: bool | None = None
    """Whether the response was a cache hit."""


class EmbeddingModel(Protocol):
    """
    Protocol for an embedding-based Language Model (LM).

    This protocol defines the methods required for an embedding-based LM.
    """

    async def aembed_batch(
        self, text_list: list[str], **kwargs: Any
    ) -> list[list[float]]:
        """
        Generate an embedding vector for the given list of strings.

        Args:
            text: The text to generate an embedding for.
            **kwargs: Additional keyword arguments (e.g., model parameters).

        Returns
        -------
            A collections of list of floats representing the embedding vector for each item in the batch.
        """
        ...

    async def aembed(self, text: str, **kwargs: Any) -> list[float]:
        """
        Generate an embedding vector for the given text.

        Args:
            text: The text to generate an embedding for.
            **kwargs: Additional keyword arguments (e.g., model parameters).

        Returns
        -------
            A list of floats representing the embedding vector.
        """
        ...

    def embed_batch(self, text_list: list[str], **kwargs: Any) -> list[list[float]]:
        """
        Generate an embedding vector for the given list of strings.

        Args:
            text: The text to generate an embedding for.
            **kwargs: Additional keyword arguments (e.g., model parameters).

        Returns
        -------
            A collections of list of floats representing the embedding vector for each item in the batch.
        """
        ...

    def embed(self, text: str, **kwargs: Any) -> list[float]:
        """
        Generate an embedding vector for the given text.

        Args:
            text: The text to generate an embedding for.
            **kwargs: Additional keyword arguments (e.g., model parameters).

        Returns
        -------
            A list of floats representing the embedding vector.
        """
        ...


class ChatModel(Protocol):
    """
    Protocol for a chat-based Language Model (LM).

    This protocol defines the methods required for a chat-based LM.
    Prompt is always required for the chat method, and any other keyword arguments are forwarded to the Model provider.
    """

    async def achat(
        self, prompt: str, history: list | None = None, **kwargs: Any
    ) -> ModelResponse:
        """
        Generate a response for the given text.

        Args:
            prompt: The text to generate a response for.
            history: The conversation history.
            **kwargs: Additional keyword arguments (e.g., model parameters).

        Returns
        -------
            A string representing the response.

        """
        ...

    async def achat_stream(
        self, prompt: str, history: list | None = None, **kwargs: Any
    ) -> AsyncGenerator[str, None]:
        """
        Generate a response for the given text using a streaming interface.

        Args:
            prompt: The text to generate a response for.
            history: The conversation history.
            **kwargs: Additional keyword arguments (e.g., model parameters).

        Returns
        -------
            A generator that yields strings representing the response.
        """
        yield ""  # Yield an empty string so that the function is recognized as a generator
        ...

    def chat(
        self, prompt: str, history: list | None = None, **kwargs: Any
    ) -> ModelResponse:
        """
        Generate a response for the given text.

        Args:
            prompt: The text to generate a response for.
            history: The conversation history.
            **kwargs: Additional keyword arguments (e.g., model parameters).

        Returns
        -------
            A string representing the response.

        """
        ...

    def chat_stream(
        self, prompt: str, history: list | None = None, **kwargs: Any
    ) -> Generator[str, None]:
        """
        Generate a response for the given text using a streaming interface.

        Args:
            prompt: The text to generate a response for.
            history: The conversation history.
            **kwargs: Additional keyword arguments (e.g., model parameters).

        Returns
        -------
            A generator that yields strings representing the response.
        """
        ...
