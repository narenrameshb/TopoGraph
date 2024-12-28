from typing import Dict, List, Set, Optional, Any
from collections import defaultdict


class Graph:
    """
    A class representing an undirected graph using an adjacency list representation.

    The graph is stored as a dictionary where keys are vertices and values are lists
    of vertices that share an edge with the key vertex.
    """

    def __init__(self):
        """Initialize an empty graph."""
        self._graph: Dict[Any, List[Any]] = defaultdict(list)
        self._vertex_count: int = 0
        self._edge_count: int = 0

    def add_vertex(self, vertex: Any) -> bool:
        """
        Add a vertex to the graph if it doesn't already exist.

        Args:
            vertex: The vertex to add

        Returns:
            bool: True if vertex was added, False if it already existed
        """
        if vertex not in self._graph:
            self._graph[vertex] = []
            self._vertex_count += 1
            return True
        return False

    def add_edge(self, v1: Any, v2: Any) -> bool:
        """
        Add an undirected edge between vertices v1 and v2.
        If either vertex doesn't exist, it will be added.

        Args:
            v1: First vertex
            v2: Second vertex

        Returns:
            bool: True if edge was added, False if it already existed

        Raises:
            ValueError: If attempting to add an edge from a vertex to itself
        """
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
        """
        Remove a vertex and all its edges from the graph.

        Args:
            vertex: The vertex to remove

        Returns:
            bool: True if vertex was removed, False if it didn't exist
        """
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
        """
        Remove the edge between vertices v1 and v2 if it exists.

        Args:
            v1: First vertex
            v2: Second vertex

        Returns:
            bool: True if edge was removed, False if it didn't exist
        """
        if v1 not in self._graph or v2 not in self._graph:
            return False

        if v2 not in self._graph[v1]:
            return False

        self._graph[v1].remove(v2)
        self._graph[v2].remove(v1)
        self._edge_count -= 1
        return True

    def get_neighbors(self, vertex: Any) -> List[Any]:
        """
        Get all vertices that share an edge with the given vertex.

        Args:
            vertex: The vertex to get neighbors for

        Returns:
            List[Any]: List of neighboring vertices

        Raises:
            KeyError: If vertex doesn't exist in the graph
        """
        if vertex not in self._graph:
            raise KeyError(f"Vertex {vertex} not found in graph")
        return self._graph[vertex].copy()  # Return a copy to prevent modification

    def get_vertices(self) -> Set[Any]:
        """
        Get all vertices in the graph.

        Returns:
            Set[Any]: Set of all vertices
        """
        return set(self._graph.keys())

    def get_edges(self) -> List[tuple]:
        """
        Get all edges in the graph.

        Returns:
            List[tuple]: List of tuples (v1, v2) representing edges
        """
        edges = []
        seen = set()  # Track edges we've already seen

        for v1 in self._graph:
            for v2 in self._graph[v1]:
                # Create a canonical representation of the edge
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