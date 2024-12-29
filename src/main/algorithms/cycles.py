from typing import List, Set, Any, Optional
from src.main.graph import Graph


def has_cycle(graph: Graph) -> bool:
    """Check if the graph contains any cycles using DFS."""
    visited = set()
    path_vertices = set()

    def dfs_cycle_check(vertex: Any, parent: Any = None) -> bool:
        visited.add(vertex)
        path_vertices.add(vertex)

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                if dfs_cycle_check(neighbor, vertex):
                    return True
            elif neighbor in path_vertices and neighbor != parent:
                return True

        path_vertices.remove(vertex)
        return False

    for vertex in graph.get_vertices():
        if vertex not in visited:
            if dfs_cycle_check(vertex):
                return True

    return False


def find_cycle(graph: Graph) -> Optional[List[Any]]:
    """Find a cycle in the graph if one exists."""
    visited = set()
    path_vertices = {}
    parent = {}

    def dfs_find_cycle(vertex: Any, path_pos: int) -> Optional[List[Any]]:
        visited.add(vertex)
        path_vertices[vertex] = path_pos

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                parent[neighbor] = vertex
                cycle = dfs_find_cycle(neighbor, path_pos + 1)
                if cycle is not None:
                    return cycle
            elif neighbor in path_vertices and neighbor != parent.get(vertex):
                # Found a cycle - reconstruct it
                cycle_start = path_vertices[neighbor]
                current_pos = path_vertices[vertex]
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
    """Find all simple cycles in the graph."""
    def normalize_cycle(cycle: List[Any]) -> tuple:
        """Helper function to normalize cycle representation."""
        min_vertex = min(cycle)
        min_idx = cycle.index(min_vertex)
        normalized = cycle[min_idx:] + cycle[:min_idx]
        return tuple(normalized)

    def find_cycles_from_start(start: Any, visited: Set[Any],
                             path: List[Any]) -> List[List[Any]]:
        cycles = []
        visited.add(start)
        path.append(start)

        for neighbor in graph.get_neighbors(start):
            if neighbor not in visited:
                cycles.extend(find_cycles_from_start(neighbor, visited.copy(),
                                                   path.copy()))
            elif neighbor == path[0] and len(path) > 2:
                cycles.append(path[:])

        return cycles

    all_cycles = []
    seen_normalized_cycles = set()

    for vertex in graph.get_vertices():
        cycles = find_cycles_from_start(vertex, set(), [])
        for cycle in cycles:
            normalized = normalize_cycle(cycle)
            if normalized not in seen_normalized_cycles:
                all_cycles.append(cycle)
                seen_normalized_cycles.add(normalized)

    return all_cycles


def get_cycle_basis(graph: Graph) -> List[List[Any]]:
    """Find a cycle basis of the graph."""
    cycle_basis = []
    visited = set()
    parent = {}

    def dfs_cycle_basis(vertex: Any, parent_vertex: Any = None) -> None:
        visited.add(vertex)
        parent[vertex] = parent_vertex

        for neighbor in graph.get_neighbors(vertex):
            if neighbor not in visited:
                dfs_cycle_basis(neighbor, vertex)
            elif neighbor != parent_vertex and vertex == parent.get(neighbor, vertex):
                # Found a fundamental cycle
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