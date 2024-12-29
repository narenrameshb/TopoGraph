import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Set, Dict, Any, Optional, Union
from src.main.graph import Graph


def visualize_graph(graph: Graph,
                    title: str = "Graph Visualization",
                    node_color: Union[str, List[str]] = 'lightblue',
                    node_size: int = 500,
                    with_labels: bool = True,
                    highlight_nodes: Optional[List[Any]] = None,
                    highlight_color: str = 'lightgreen',
                    highlight_edges: Optional[List[tuple]] = None,
                    edge_color_default: str = 'gray',
                    edge_color_highlight: str = 'red',
                    edge_width_default: float = 1.0,
                    edge_width_highlight: float = 2.0,
                    figsize: tuple = (10, 8)) -> None:
    """
    Visualize a graph with optional highlighting of specific nodes and edges.

    Args:
        graph: The graph to visualize
        title: Title of the plot
        node_color: Color(s) for nodes (default or list for each node)
        node_size: Size of the nodes
        with_labels: Whether to show vertex labels
        highlight_nodes: List of nodes to highlight
        highlight_color: Color for highlighted nodes
        highlight_edges: List of edges to highlight
        edge_color_default: Color for regular edges
        edge_color_highlight: Color for highlighted edges
        edge_width_default: Width for regular edges
        edge_width_highlight: Width for highlighted edges
        figsize: Figure size as (width, height)
    """
    # Convert to networkx format
    G = nx.Graph()
    G.add_edges_from(graph.get_edges())

    # Add any isolated vertices
    for vertex in graph.get_vertices():
        if vertex not in G:
            G.add_node(vertex)

    # Set up the plot
    plt.figure(figsize=figsize)
    pos = nx.spring_layout(G, k=1, iterations=50)  # k=1 for more spread out layout

    # Draw regular edges
    if highlight_edges:
        regular_edges = [e for e in G.edges if e not in highlight_edges
                         and tuple(reversed(e)) not in highlight_edges]
        nx.draw_networkx_edges(G, pos,
                               edgelist=regular_edges,
                               edge_color=edge_color_default,
                               width=edge_width_default)
        # Draw highlighted edges
        nx.draw_networkx_edges(G, pos,
                               edgelist=highlight_edges,
                               edge_color=edge_color_highlight,
                               width=edge_width_highlight)
    else:
        nx.draw_networkx_edges(G, pos,
                               edge_color=edge_color_default,
                               width=edge_width_default)

    # Draw regular nodes
    if highlight_nodes:
        regular_nodes = [n for n in G.nodes if n not in highlight_nodes]
        nx.draw_networkx_nodes(G, pos,
                               nodelist=regular_nodes,
                               node_color=node_color,
                               node_size=node_size)
        # Draw highlighted nodes
        nx.draw_networkx_nodes(G, pos,
                               nodelist=highlight_nodes,
                               node_color=highlight_color,
                               node_size=node_size)
    else:
        nx.draw_networkx_nodes(G, pos,
                               node_color=node_color,
                               node_size=node_size)

    # Add labels if requested
    if with_labels:
        nx.draw_networkx_labels(G, pos,
                                font_size=12,
                                font_weight='bold')

    plt.title(title, pad=20)
    plt.axis('off')  # Hide axes
    plt.tight_layout()
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

    # Create path edges
    path_edges = list(zip(path[:-1], path[1:]))

    # Use the general visualization function with highlighting
    visualize_graph(graph,
                    title=title,
                    highlight_nodes=path,
                    highlight_edges=path_edges,
                    node_color='lightblue',
                    highlight_color='lightgreen',
                    edge_color_default='gray',
                    edge_color_highlight='red')


def visualize_components(graph: Graph,
                         components: List[Set[Any]],
                         title: str = "Connected Components") -> None:
    """
    Visualize connected components using different colors.

    Args:
        graph: The graph to visualize
        components: List of sets, where each set contains vertices in a component
        title: Title of the plot
    """
    # Create color map for nodes
    colors = ['lightblue', 'lightgreen', 'salmon', 'yellow', 'lightgray',
              'lightpink', 'lightyellow', 'lightcyan']
    color_map = []
    vertices = list(graph.get_vertices())

    # Assign colors to vertices based on their component
    for vertex in vertices:
        for i, component in enumerate(components):
            if vertex in component:
                color_map.append(colors[i % len(colors)])
                break

    visualize_graph(graph,
                    title=title,
                    node_color=color_map)


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

    # Create cycle edges (including closing edge)
    cycle_edges = list(zip(cycle, cycle[1:] + [cycle[0]]))

    # Use the general visualization function with highlighting
    visualize_graph(graph,
                    title=title,
                    highlight_nodes=cycle,
                    highlight_edges=cycle_edges,
                    node_color='lightblue',
                    highlight_color='lightgreen',
                    edge_color_default='gray',
                    edge_color_highlight='red')


def visualize_search_tree(graph: Graph,
                          tree: Dict[Any, List[Any]],
                          root: Any,
                          title: str = "Search Tree Visualization") -> None:
    """
    Visualize a search tree (BFS or DFS) within the graph.

    Args:
        graph: The original graph
        tree: Dictionary representing the tree (output of get_search_tree)
        root: Root vertex of the tree
        title: Title of the plot
    """
    # Create tree edges
    tree_edges = []
    for parent, children in tree.items():
        tree_edges.extend((parent, child) for child in children)

    # Use the general visualization function with highlighting
    visualize_graph(graph,
                    title=title,
                    highlight_nodes=[root],  # Highlight root node
                    highlight_edges=tree_edges,
                    node_color='lightblue',
                    highlight_color='lightgreen',
                    edge_color_default='gray',
                    edge_color_highlight='blue',
                    edge_width_highlight=1.5)