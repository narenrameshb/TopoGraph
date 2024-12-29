from src.main.graph import Graph
from src.main.visualization.plot import visualize_graph


def main():
    """Demonstrate basic graph operations."""
    # Create a new graph
    g = Graph()

    # Add vertices and edges
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    # Print graph information
    print(f"Graph has {len(g)} vertices and {g.size()} edges")
    print(f"Neighbors of vertex 2: {g.get_neighbors(2)}")
    print(f"All edges: {g.get_edges()}")

    # Visualize the graph
    visualize_graph(g, title="Basic Triangle Graph")

    # Remove an edge and a vertex
    g.remove_edge(1, 2)
    g.remove_vertex(3)

    # Visualize modified graph
    visualize_graph(g, title="Modified Graph")


if __name__ == "__main__":
    main()