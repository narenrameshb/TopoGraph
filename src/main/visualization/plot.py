import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Set, Dict, Any, Optional
from ..graph import Graph


def visualize_graph(graph: Graph,
                    title: str = "Graph Visualization",
                    node_color: str = 'lightblue',
                    node_size: int = 500,
                    with_labels: bool = True) -> None:
    """
    Visualize a graph using networkx and matplotlib.

    Args:
        graph: The graph to visualize
        title: Title of the plot
        node_color: Color of the nodes
        node_size: Size of the nodes
        with_labels: Whether to show vertex labels
    """
    # Convert our graph to networkx format
    G = nx.Graph()

    # Add all edges
    G.add_edges_from(graph.get_edges())

    # Create the visualization
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)  # Position nodes using spring layout

    nx.draw(G, pos,
            with_labels=with_labels,
            node_color=node_color,
            node_size=node_size,
            font_size=16,
            font_weight='bold')

    plt.title(title)
    plt.show()


def visualize_path(graph: Graph,
                   path: List[Any],
                   title: str = "Path Visualization") -> None:
    """
    Visualize a path in the graph by highlighting the path edges.

    Args:
        graph: The graph to visualize
        path: List of vertices forming the path
        title: Title of the plot
    """
    if len(path) < 2:
        raise ValueError("Path must contain at least 2 vertices")

    # Convert graph to networkx format
    G = nx.Graph()
    G.add_edges_from(graph.get_edges())

    # Create path edges list
    path_edges = list(zip(path[:-1], path[1:]))

    # Set up the plot
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)

    # Draw the regular edges
    nx.draw_networkx_edges(G, pos,
                           edgelist=[e for e in G.edges if e not in path_edges],
                           edge_color='gray')

    # Draw the path edges
    nx.draw_networkx_edges(G, pos,
                           edgelist=path_edges,
                           edge_color='red',
                           width=2)

    # Draw all nodes
    nx.draw_networkx_nodes(G, pos,
                           node_color='lightblue',
                           node_size=500)

    # Highlight path nodes
    nx.draw_networkx_nodes(G, pos,
                           nodelist=path,
                           node_color='lightgreen',
                           node_size=500)

    # Add labels
    nx.draw_networkx_labels(G, pos,
                            font_size=16,
                            font_weight='bold')

    plt.title(title)
    plt.show()


def visualize_components(graph: Graph,
                         components: List[Set[Any]],
                         title: str = "Connected Components") -> None:
    """
    Visualize connected components in different colors.

    Args:
        graph: The graph to visualize
        components: List of sets, where each set contains vertices in a component
        title: Title of the plot
    """
    # Convert graph to networkx format
    G = nx.Graph()
    G.add_edges_from(graph.get_edges())

    # Set up the plot
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)

    # Create a color map for nodes
    color_map = []
    colors = ['lightblue', 'lightgreen', 'salmon', 'yellow', 'lightgray']

    for vertex in G.nodes():
        # Find which component the vertex belongs to
        for i, component in enumerate(components):
            if vertex in component:
                color_map.append(colors[i % len(colors)])
                break

    # Draw the graph
    nx.draw(G, pos,
            node_color=color_map,
            with_labels=True,
            node_size=500,
            font_size=16,
            font_weight='bold')

    plt.title(title)
    plt.show()


def visualize_cycle(graph: Graph,
                    cycle: List[Any],
                    title: str = "Cycle Visualization") -> None:
    """
    Visualize a cycle in the graph by highlighting cycle edges.

    Args:
        graph: The graph to visualize
        cycle: List of vertices forming the cycle
        title: Title of the plot
    """
    if len(cycle) < 3:
        raise ValueError("Cycle must contain at least 3 vertices")

    # Convert graph to networkx format
    G = nx.Graph()
    G.add_edges_from(graph.get_edges())

    # Create cycle edges list (including closing edge)
    cycle_edges = list(zip(cycle, cycle[1:] + [cycle[0]]))

    # Set up the plot
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)

    # Draw regular edges
    nx.draw_networkx_edges(G, pos,
                           edgelist=[e for e in G.edges if e not in cycle_edges],
                           edge_color='gray')

    # Draw cycle edges
    nx.draw_networkx_edges(G, pos,
                           edgelist=cycle_edges,
                           edge_color='red',
                           width=2)

    # Draw all nodes
    nx.draw_networkx_nodes(G, pos,
                           node_color='lightblue',
                           node_size=500)

    # Highlight cycle nodes
    nx.draw_networkx_nodes(G, pos,
                           nodelist=cycle,
                           node_color='lightgreen',
                           node_size=500)

    # Add labels
    nx.draw_networkx_labels(G, pos,
                            font_size=16,
                            font_weight='bold')

    plt.title(title)
    plt.show()