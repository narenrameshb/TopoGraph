from src.main.algorithms.connectivity import get_connected_components
from src.main.algorithms.cycles import find_all_cycles
from src.main.graph import Graph
from src.main.visualization.plot import visualize_components, visualize_cycle


def main():
    """Create and analyze a more complex graph."""
    g = Graph()

    # Create a complex structure with multiple components and cycles
    # First component: cube-like structure
    for i in range(1, 5):
        for j in range(5, 9):
            if (i - 1) % 4 + 1 == j - 4:
                g.add_edge(i, j)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 1)
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    g.add_edge(7, 8)
    g.add_edge(8, 5)

    # Second component: pentagon
    for i in range(10, 14):
        g.add_edge(i, i + 1)
    g.add_edge(14, 10)

    # Analyze the graph
    components = get_connected_components(g)
    print(f"Number of components: {len(components)}")
    visualize_components(g, components, "Complex Graph Components")

    cycles = find_all_cycles(g)
    print(f"Number of cycles: {len(cycles)}")
    for i, cycle in enumerate(cycles[:3]):  # Show first 3 cycles
        visualize_cycle(g, cycle, f"Complex Graph Cycle {i + 1}")


if __name__ == "__main__":
    main()