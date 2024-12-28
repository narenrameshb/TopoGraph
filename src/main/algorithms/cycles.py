from typing import List, Set, Dict, Any, Optional
from ..graph import Graph


def has_cycle(graph: Graph) -> bool:
    """
    Check if the graph contains any cycles using DFS.

    Args:
        graph: The graph to check

    Returns:
        bool: True if the graph contains a cycle, False otherwise
    """
    visited = set()
    # Track vertices in current DFS path
    path_vertices = set()

    def dfs_cycle_check(vertex: Any) -> bool:
        """
        Helper function for DFS cycle detection.
        Returns True if a cycle is found, False otherwise.
        """
        visited.add(vertex)
        path_vertices.add(vertex)

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                if dfs_cycle_check(neighbor):
                    return True
            elif neighbor in path_vertices:
                # Found a back edge - cycle exists
                return True

        path_vertices.remove(vertex)
        return False

    # Check from each unvisited vertex (handles disconnected components)
    for vertex in graph.get_vertices():
        if vertex not in visited:
            if dfs_cycle_check(vertex):
                return True

    return False


def find_cycle(graph: Graph) -> Optional[List[Any]]:
    """
    Find a cycle in the graph if one exists.

    Args:
        graph: The graph to search

    Returns:
        Optional[List[Any]]: List of vertices forming a cycle if one exists,
                           None otherwise
    """
    visited = set()
    path_vertices = {}  # Maps vertex to its position in current path

    def dfs_find_cycle(vertex: Any, path_pos: int) -> Optional[List[Any]]:
        """
        Helper function for finding a cycle using DFS.
        Returns cycle if found, None otherwise.
        """
        visited.add(vertex)
        path_vertices[vertex] = path_pos

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                cycle = dfs_find_cycle(neighbor, path_pos + 1)
                if cycle is not None:
                    return cycle
            elif neighbor in path_vertices:
                # Found a cycle - reconstruct it
                cycle_start = path_vertices[neighbor]
                current_pos = path_vertices[vertex]

                # Get vertices with positions between cycle_start and current_pos
                cycle = [v for v, pos in path_vertices.items()
                         if cycle_start <= pos <= current_pos]
                return cycle

        path_vertices.pop(vertex)
        return None

    for vertex in graph.get_vertices():
        if vertex not in visited:
            cycle = dfs_find_cycle(vertex, 0)
            if cycle is not None:
                return cycle

    return None


def find_all_cycles(graph: Graph) -> List[List[Any]]:
    """
    Find all simple cycles in the graph.
    A simple cycle is a cycle where no vertex appears more than once,
    except the start/end vertex.

    Args:
        graph: The graph to analyze

    Returns:
        List[List[Any]]: List of cycles, where each cycle is a list of vertices
    """

    def find_cycles_from_start(start: Any, visited: Set[Any],
                               path: List[Any]) -> List[List[Any]]:
        """Helper function to find all cycles starting from a vertex."""
        cycles = []
        visited.add(start)
        path.append(start)

        for neighbor in graph.get_neighbors(start):
            if neighbor not in visited:
                cycles.extend(find_cycles_from_start(neighbor, visited.copy(),
                                                     path.copy()))
            elif neighbor == path[0] and len(path) > 2:
                # Found a cycle - add a copy of the current path
                cycles.append(path[:])

        return cycles

    all_cycles = []
    for vertex in graph.get_vertices():
        cycles = find_cycles_from_start(vertex, set(), [])
        # Remove duplicate cycles (same cycle starting from different vertices)
        for cycle in cycles:
            normalized = tuple(min(cycle[i:] + cycle[:i] for i in range(len(cycle))))
            if normalized not in {tuple(min(c[i:] + c[:i]
                                            for i in range(len(c)))) for c in all_cycles}:
                all_cycles.append(cycle)

    return all_cycles


def get_cycle_basis(graph: Graph) -> List[List[Any]]:
    """
    Find a cycle basis of the graph.
    A cycle basis is a minimal set of cycles such that any cycle in the graph
    can be expressed as a combination of cycles in the basis.

    Args:
        graph: The graph to analyze

    Returns:
        List[List[Any]]: List of cycles forming a cycle basis
    """
    cycle_basis = []
    visited = set()
    parent = {}

    def dfs_cycle_basis(vertex: Any) -> None:
        """Helper function for finding cycle basis using DFS."""
        visited.add(vertex)

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                parent[neighbor] = vertex
                dfs_cycle_basis(neighbor)
            elif neighbor != parent.get(vertex):
                # Found a back edge - construct cycle
                cycle = []
                current = vertex
                while current != neighbor:
                    cycle.append(current)
                    current = parent[current]
                cycle.append(neighbor)
                cycle.append(vertex)
                cycle_basis.append(cycle)

    for vertex in graph.get_vertices():
        if vertex not in visited:
            dfs_cycle_basis(vertex)

    return cycle_basis