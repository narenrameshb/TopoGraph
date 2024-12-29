from src.main.graph import Graph
from src.main.algorithms.search import (
    breadth_first_search, depth_first_search,
    find_path_bfs, find_all_paths_dfs, get_search_tree
)
from src.main.visualization.plot import visualize_graph, visualize_path


def main():
    """Demonstrate search algorithms."""
    # Create a graph for searching
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)
    g.add_edge(4, 5)

    # Perform BFS
    bfs_result = breadth_first_search(g, 1)
    print("BFS Results:")
    print(f"Visit order: {bfs_result['visited_order']}")
    print(f"Distances: {bfs_result['distances']}")
    print(f"Predecessors: {bfs_result['predecessors']}")

    # Perform DFS
    dfs_result = depth_first_search(g, 1)
    print("\nDFS Results:")
    print(f"Visit order: {dfs_result['visited_order']}")
    print(f"Discovery times: {dfs_result['discovery_times']}")
    print(f"Finish times: {dfs_result['finish_times']}")

    # Find paths
    bfs_path = find_path_bfs(g, 1, 5)
    print(f"\nShortest path (BFS) from 1 to 5: {bfs_path}")
    if bfs_path:
        visualize_path(g, bfs_path, "Shortest Path (BFS)")

    all_paths = find_all_paths_dfs(g, 1, 5)
    print(f"All paths (DFS) from 1 to 5: {all_paths}")
    for i, path in enumerate(all_paths):
        visualize_path(g, path, f"Path {i + 1} (DFS)")

    # Visualize search tree
    bfs_tree = get_search_tree(bfs_result['predecessors'])
    visualize_graph(g, title="BFS Tree",
                    highlight_edges=[(p, c) for p, children in bfs_tree.items()
                                     for c in children])


if __name__ == "__main__":
    main()