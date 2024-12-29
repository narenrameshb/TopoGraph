from typing import List, Set, Dict, Optional, Any
from collections import deque
from src.main.graph import Graph


def is_connected(graph: Graph) -> bool:
    """Check if the graph is connected using BFS."""
    if len(graph) <= 1:
        return True

    vertices = graph.get_vertices()
    start = next(iter(vertices))
    visited = _bfs_visit(graph, start)

    return len(visited) == len(graph)


def find_path(graph: Graph, start: Any, end: Any) -> Optional[List[Any]]:
    """Find a path between start and end vertices using BFS."""
    if start not in graph.get_vertices():
        raise KeyError(f"Start vertex {start} not in graph")

    # Return None if end vertex doesn't exist
    if end not in graph.get_vertices():
        return None

    if start == end:
        return [start]

    visited = {start}
    predecessors: Dict[Any, Any] = {}
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                predecessors[neighbor] = current
                queue.append(neighbor)

                if neighbor == end:
                    return _reconstruct_path(predecessors, start, end)

    return None


def get_connected_components(graph: Graph) -> List[Set[Any]]:
    """Find all connected components in the graph."""
    components = []
    unvisited = graph.get_vertices()

    while unvisited:
        start = next(iter(unvisited))
        component = _bfs_visit(graph, start)
        components.append(component)
        unvisited -= component

    return components


def _bfs_visit(graph: Graph, start: Any) -> Set[Any]:
    """Helper function to perform BFS from a starting vertex."""
    visited = {start}
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited


def _reconstruct_path(predecessors: Dict[Any, Any], start: Any, end: Any) -> List[Any]:
    """Helper function to reconstruct path from predecessors dictionary."""
    path = [end]
    current = end

    while current != start:
        current = predecessors[current]
        path.append(current)

    return list(reversed(path))


def is_tree(graph: Graph) -> bool:
    """Check if the graph is a tree."""
    if len(graph) == 0:
        return True

    # A tree must have exactly |V| - 1 edges
    if graph.size() != len(graph) - 1:
        return False

    # A tree must be connected
    return is_connected(graph)
