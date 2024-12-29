from collections import defaultdict
from typing import Dict, List, Set, Any


class Graph:
    """
    A class representing an undirected graph using an adjacency list representation.
    """

    def __init__(self):
        """Initialize an empty graph."""
        self._graph: Dict[Any, List[Any]] = defaultdict(list)
        self._vertex_count: int = 0
        self._edge_count: int = 0

    def add_vertex(self, vertex: Any) -> bool:
        """Add a vertex to the graph if it doesn't already exist."""
        if vertex not in self._graph:
            self._graph[vertex] = []
            self._vertex_count += 1
            return True
        return False

    def add_edge(self, v1: Any, v2: Any) -> bool:
        """Add an undirected edge between vertices v1 and v2."""
        if v1 == v2:
            raise ValueError("Self-loops are not allowed")

        # Add vertices if they don't exist
        self.add_vertex(v1)
        self.add_vertex(v2)

        # Check if edge already exists
        if v2 in self._graph[v1]:
            return False

        # Add edge in both directions (undirected graph)
        self._graph[v1].append(v2)
        self._graph[v2].append(v1)
        self._edge_count += 1
        return True

    def remove_vertex(self, vertex: Any) -> bool:
        """Remove a vertex and all its edges from the graph."""
        if vertex not in self._graph:
            return False

        # Remove all edges containing this vertex
        for neighbor in self._graph[vertex]:
            self._graph[neighbor].remove(vertex)
            self._edge_count -= 1

        # Remove the vertex
        del self._graph[vertex]
        self._vertex_count -= 1
        return True

    def remove_edge(self, v1: Any, v2: Any) -> bool:
        """Remove the edge between vertices v1 and v2 if it exists."""
        if v1 not in self._graph or v2 not in self._graph:
            return False

        if v2 not in self._graph[v1]:
            return False

        self._graph[v1].remove(v2)
        self._graph[v2].remove(v1)
        self._edge_count -= 1
        return True

    def get_neighbors(self, vertex: Any) -> List[Any]:
        """Get all vertices that share an edge with the given vertex."""
        if vertex not in self._graph:
            raise KeyError(f"Vertex {vertex} not found in graph")
        return self._graph[vertex].copy()

    def get_vertices(self) -> Set[Any]:
        """Get all vertices in the graph."""
        return set(self._graph.keys())

    def get_edges(self) -> List[tuple]:
        """Get all edges in the graph."""
        edges = []
        seen = set()

        for v1 in self._graph:
            for v2 in self._graph[v1]:
                edge = tuple(sorted([v1, v2]))
                if edge not in seen:
                    edges.append(edge)
                    seen.add(edge)
        return edges

    def __len__(self) -> int:
        """Return the number of vertices in the graph."""
        return self._vertex_count

    def size(self) -> int:
        """Return the number of edges in the graph."""
        return self._edge_count

    def __str__(self) -> str:
        """Return a string representation of the graph."""
        return f"Graph with {self._vertex_count} vertices and {self._edge_count} edges"

    def __repr__(self) -> str:
        """Return a detailed string representation of the graph."""
        return f"Graph(vertices={list(self._graph.keys())}, edges={self.get_edges()})"