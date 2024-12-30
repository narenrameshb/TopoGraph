import pytest
from src.main.graph import Graph
from src.main.algorithms.connectivity import is_connected, find_path, get_connected_components, is_tree


def test_is_connected():
    g = Graph()
    assert is_connected(g)  # Empty graph
    g.add_vertex(1)
    assert is_connected(g)  # Single vertex
    g.add_edge(1, 2)
    assert is_connected(g)  # Connected pair
    g.add_vertex(3)  # Disconnected vertex
    assert not is_connected(g)


def test_find_path():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    # Test existing path
    path = find_path(g, 1, 3)
    assert path == [1, 2, 3]

    # Test non-existent path
    assert find_path(g, 1, 4) is None

    # Test invalid start vertex
    with pytest.raises(KeyError):
        find_path(g, 5, 1)


def test_get_components():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(3, 4)

    components = get_connected_components(g)
    assert len(components) == 2
    assert {1, 2} in components
    assert {3, 4} in components


def test_is_tree():
    g = Graph()
    assert is_tree(g)  # Empty graph is a tree
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    assert is_tree(g)  # Simple path is a tree
    g.add_edge(1, 3)  # Creates cycle
    assert not is_tree(g)