import pytest
from src.main.graph import Graph

def test_create_graph():
    g = Graph()
    assert len(g) == 0
    assert g.size() == 0

def test_add_vertex():
    g = Graph()
    assert g.add_vertex(1)  # New vertex
    assert not g.add_vertex(1)  # Duplicate vertex
    assert len(g) == 1

def test_add_edge():
    g = Graph()
    assert g.add_edge(1, 2)  # New edge
    assert not g.add_edge(1, 2)  # Duplicate edge
    with pytest.raises(ValueError):
        g.add_edge(1, 1)  # Self-loop

def test_get_neighbors():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    assert set(g.get_neighbors(1)) == {2, 3}
    with pytest.raises(KeyError):
        g.get_neighbors(4)