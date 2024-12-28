from typing import List, Set, Dict, Optional, Any
from collections import deque
from ..graph import Graph


def is_connected(graph: Graph) -> bool:
    """
    Check if the graph is connected using BFS.
    A graph is connected if there is a path between any two vertices.

    Args:
        graph: The graph to check

    Returns:
        bool: True if the graph is connected, False otherwise
    """
    if len(graph) <= 1:  # Empty graph or single vertex is connected
        return True

    # Start BFS from first vertex
    vertices = graph.get_vertices()
    start = next(iter(vertices))
    visited = _bfs_visit(graph, start)

    # Graph is connected if BFS reaches all vertices
    return len(visited) == len(graph)


def find_path(graph: Graph, start: Any, end: Any) -> Optional[List[Any]]:
    """
    Find a path between start and end vertices using BFS.
    Returns the shortest path if one exists.

    Args:
        graph: The graph to search in
        start: Starting vertex
        end: Target vertex

    Returns:
        Optional[List[Any]]: List of vertices forming path if one exists, None otherwise

    Raises:
        KeyError: If either start or end vertex is not in the graph
    """
    # Verify vertices exist
    if start not in graph.get_vertices():
        raise KeyError(f"Start vertex {start} not in graph")
    if end not in graph.get_vertices():
        raise KeyError(f"End vertex {end} not in graph")

    if start == end:
        return [start]

    # Track both visited vertices and their predecessors
    visited = {start}
    predecessors: Dict[Any, Any] = {}
    queue = deque([start])

    while queue:
        current = queue.popleft()

        # Check all neighbors
        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                predecessors[neighbor] = current
                queue.append(neighbor)

                if neighbor == end:
                    # Reconstruct path from end to start
                    return _reconstruct_path(predecessors, start, end)

    return None  # No path found


def get_connected_components(graph: Graph) -> List[Set[Any]]:
    """
    Find all connected components in the graph.

    Args:
        graph: The graph to analyze

    Returns:
        List[Set[Any]]: List of sets, where each set contains vertices in a component
    """
    components = []
    unvisited = graph.get_vertices()

    while unvisited:
        # Start a new component from an unvisited vertex
        start = next(iter(unvisited))
        component = _bfs_visit(graph, start)
        components.append(component)
        unvisited -= component

    return components


def _bfs_visit(graph: Graph, start: Any) -> Set[Any]:
    """
    Helper function to perform BFS from a starting vertex.
    Returns set of all vertices reachable from start.

    Args:
        graph: The graph to traverse
        start: Starting vertex

    Returns:
        Set[Any]: Set of all vertices reachable from start
    """
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
    """
    Helper function to reconstruct path from predecessors dictionary.

    Args:
        predecessors: Dictionary mapping vertices to their predecessors
        start: Starting vertex
        end: Ending vertex

    Returns:
        List[Any]: Path from start to end
    """
    path = [end]
    current = end

    while current != start:
        current = predecessors[current]
        path.append(current)

    return list(reversed(path))  # Reverse to get path from start to end


def is_tree(graph: Graph) -> bool:
    """
    Check if the graph is a tree.
    A tree is a connected graph with no cycles.

    Args:
        graph: The graph to check

    Returns:
        bool: True if the graph is a tree, False otherwise
    """
    if len(graph) == 0:
        return True

    # A tree must have exactly |V| - 1 edges
    if graph.size() != len(graph) - 1:
        return False

    # A tree must be connected
    return is_connected(graph)