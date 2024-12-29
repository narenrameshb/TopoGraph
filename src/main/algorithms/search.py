from collections import deque
from typing import List, Dict, Any, Optional

from src.main.graph import Graph


def breadth_first_search(graph: Graph, start: Any) -> Dict[str, Any]:
    """Perform breadth-first search starting from a given vertex."""
    if start not in graph.get_vertices():
        raise KeyError(f"Start vertex {start} not found in graph")

    visited_order = []
    distances = {start: 0}
    predecessors = {start: None}
    queue = deque([start])

    while queue:
        current = queue.popleft()
        visited_order.append(current)

        for neighbor in graph.get_neighbors(current):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                predecessors[neighbor] = current
                queue.append(neighbor)

    return {
        'visited_order': visited_order,
        'distances': distances,
        'predecessors': predecessors
    }


def depth_first_search(graph: Graph, start: Any) -> Dict[str, Any]:
    """Perform depth-first search starting from a given vertex."""
    if start not in graph.get_vertices():
        raise KeyError(f"Start vertex {start} not found in graph")

    visited_order = []
    discovery_times = {}
    finish_times = {}
    predecessors = {start: None}
    time = 0

    def dfs_visit(vertex: Any) -> None:
        nonlocal time
        time += 1
        discovery_times[vertex] = time
        visited_order.append(vertex)

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in discovery_times:
                predecessors[neighbor] = vertex
                dfs_visit(neighbor)

        time += 1
        finish_times[vertex] = time

    dfs_visit(start)

    return {
        'visited_order': visited_order,
        'discovery_times': discovery_times,
        'finish_times': finish_times,
        'predecessors': predecessors
    }


def find_path_bfs(graph: Graph, start: Any, end: Any) -> Optional[List[Any]]:
    """Find shortest path between start and end vertices using BFS."""
    if start not in graph.get_vertices():
        raise KeyError(f"Start vertex {start} not found in graph")

    # Return None if end vertex doesn't exist
    if end not in graph.get_vertices():
        return None

    result = breadth_first_search(graph, start)
    predecessors = result['predecessors']

    if end not in predecessors:
        return None

    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]

    return list(reversed(path))


def find_all_paths_dfs(graph: Graph, start: Any, end: Any) -> List[List[Any]]:
    """Find all possible paths between start and end vertices using DFS."""
    if start not in graph.get_vertices() or end not in graph.get_vertices():
        raise KeyError("Start or end vertex not found in graph")

    def dfs_paths(current: Any, path: List[Any], paths: List[List[Any]]) -> None:
        if current == end:
            paths.append(path[:])
            return

        for neighbor in graph.get_neighbors(current):
            if neighbor not in path:
                path.append(neighbor)
                dfs_paths(neighbor, path, paths)
                path.pop()

    all_paths = []
    dfs_paths(start, [start], all_paths)
    return all_paths


def get_search_tree(predecessors: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    """Convert predecessors dictionary to a tree representation."""
    tree = {vertex: [] for vertex in predecessors}

    for vertex, pred in predecessors.items():
        if pred is not None:
            tree[pred].append(vertex)

    return tree