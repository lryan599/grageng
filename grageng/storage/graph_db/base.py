from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

import numpy as np


@dataclass
class BaseGraphStorage(ABC):
    @abstractmethod
    async def has_node(self, node_id: str) -> bool:
        """Check if an edge exists in the graph."""

    @abstractmethod
    async def has_edge(self, source_node_id: str, target_node_id: str) -> bool:
        """Get the degree of a node."""

    @abstractmethod
    async def node_degree(self, node_id: str) -> int:
        """Get the degree of an edge."""

    @abstractmethod
    async def edge_degree(self, src_id: str, tgt_id: str) -> int:
        """Get a node by its id."""

    @abstractmethod
    async def get_node(self, node_id: str) -> dict[str, str] | None:
        """Get an edge by its source and target node ids."""

    @abstractmethod
    async def get_edge(
        self, source_node_id: str, target_node_id: str
    ) -> dict[str, str] | None:
        """Get all edges connected to a node."""

    @abstractmethod
    async def get_node_edges(self, source_node_id: str) -> list[tuple[str, str]] | None:
        """Upsert a node into the graph."""

    @abstractmethod
    async def upsert_node(self, node_id: str, node_data: dict[str, str]) -> None:
        """Upsert an edge into the graph."""

    @abstractmethod
    async def upsert_edge(
        self, source_node_id: str, target_node_id: str, edge_data: dict[str, str]
    ) -> None:
        """Delete a node from the graph."""

    @abstractmethod
    async def delete_node(self, node_id: str) -> None:
        """Embed nodes using an algorithm."""

    @abstractmethod
    async def embed_nodes(
        self, algorithm: str
    ) -> tuple[np.ndarray[Any, Any], list[str]]:
        """Get all labels in the graph."""

    @abstractmethod
    async def get_all_labels(self) -> list[str]:
        """Get a knowledge graph of a node."""

    # @abstractmethod
    # async def get_knowledge_graph(
    #     self, node_label: str, max_depth: int = 3
    # ) -> KnowledgeGraph:
    #     """Retrieve a subgraph of the knowledge graph starting from a given node."""
