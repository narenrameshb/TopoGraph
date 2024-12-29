from src.main.graph import Graph
from src.main.algorithms.connectivity import is_connected, find_path, get_connected_components, is_tree
from src.main.visualization.plot import visualize_path, visualize_components, visualize_graph


def main():
    """Demonstrate connectivity-related operations."""
    # Create a disconnected graph
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(4, 5)
    g.add_edge(5, 6)

    # Check connectivity
    print(f"Is graph connected? {is_connected(g)}")

    # Find path between vertices
    path = find_path(g, 1, 3)
    print(f"Path from 1 to 3: {path}")
    if path:
        visualize_path(g, path, "Path from 1 to 3")

    # Get connected components
    components = get_connected_components(g)
    print(f"Connected components: {components}")
    visualize_components(g, components, "Connected Components")

    # Create and test a tree
    tree = Graph()
    tree.add_edge(1, 2)
    tree.add_edge(1, 3)
    tree.add_edge(2, 4)
    print(f"Is the new graph a tree? {is_tree(tree)}")
    visualize_graph(tree, title="Tree Graph")


if __name__ == "__main__":
    main()