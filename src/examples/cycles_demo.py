from src.main.graph import Graph
from src.main.algorithms.cycles import has_cycle, find_cycle, find_all_cycles, get_cycle_basis
from src.main.visualization.plot import visualize_cycle


def main():
    """Demonstrate cycle-related operations."""
    # Create a graph with multiple cycles
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)  # First cycle
    g.add_edge(3, 4)
    g.add_edge(4, 1)  # Second cycle

    # Check for cycles
    print(f"Graph has cycles: {has_cycle(g)}")

    # Find a single cycle
    cycle = find_cycle(g)
    if cycle:
        print(f"Found cycle: {cycle}")
        visualize_cycle(g, cycle, "Single Cycle")

    # Find all cycles
    all_cycles = find_all_cycles(g)
    print(f"All cycles in graph: {all_cycles}")
    for i, cycle in enumerate(all_cycles):
        visualize_cycle(g, cycle, f"Cycle {i + 1}")

    # Get cycle basis
    basis = get_cycle_basis(g)
    print(f"Cycle basis: {basis}")


if __name__ == "__main__":
    main()