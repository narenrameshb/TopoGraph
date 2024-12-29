# TopoGraph

## Overview
TopoGraph is a Python implementation that explores the intersection of graph theory and topology. This project represents my personal exploration into these mathematical fields, combining fundamental graph theory algorithms with topological concepts.

## Author
**Naren Ramesh**

This project stems from my interest in both graph theory and topology, showcasing implementations of various algorithms and concepts I've studied. While graph theory and topology are vast fields, this implementation focuses on core concepts that demonstrate the beautiful connections between these areas of mathematics.

## Features

### Graph Theory Components
- **Basic Graph Operations**: Implementation of undirected graphs with fundamental operations
- **Connectivity Analysis**: Path finding, component identification, and tree verification
- **Cycle Detection**: Multiple approaches to finding and analyzing cycles
- **Search Algorithms**: Both breadth-first and depth-first search implementations
- **Visualization**: Various ways to visualize graph structures and algorithms

### Key Implementations
1. **Graph Structure**
   - Adjacency list representation
   - Vertex and edge management
   - Basic graph properties

2. **Connectivity**
   - Path finding algorithms
   - Connected component analysis
   - Tree verification
   - Basic topological properties

3. **Cycle Analysis**
   - Cycle detection
   - Finding fundamental cycles
   - Cycle basis computation
   - Relationship to homology

4. **Search Algorithms**
   - Breadth-first search (BFS)
   - Depth-first search (DFS)
   - Multiple path finding approaches
   - Search tree construction

5. **Visualization**
   - Graph structure visualization
   - Path and cycle highlighting
   - Component visualization
   - Search tree representation

## Installation

```bash
# Clone the repository
git clone https://github.com/narenramesh/TopoGraph.git

# Navigate to the directory
cd TopoGraph

# Install required packages
pip install -r requirements.txt
```

## Usage

Basic usage examples:

```python
from topograph.graph import Graph
from topograph.connectivity import find_path
from topograph.plot import visualize_graph

# Create a new graph
g = Graph()

# Add some edges
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)

# Find a path
path = find_path(g, 1, 3)

# Visualize the graph
visualize_graph(g, title="Simple Triangle")
```

More examples can be found in the `examples` directory.

## Mathematical Background

This implementation draws from several mathematical concepts:

1. **Graph Theory**
   - Graph structures and properties
   - Path and circuit theory
   - Connectivity and components
   - Trees and spanning trees

2. **Topological Concepts**
   - Basic homology groups
   - Fundamental groups
   - Path connectedness

## Testing

The project includes a comprehensive test suite:

```bash
# Run all tests
pytest tests/

# Run specific test files
pytest tests/test_graph.py
pytest tests/test_connectivity.py
```

## Future Directions

Future developments may include:
- Integration with more topological concepts
- Implementation of homology computations
- Additional visualization capabilities
- Extended algorithm implementations
- Performance optimizations

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
*Note: This project is part of my personal exploration into graph theory and topology. While it implements many standard algorithms, its primary purpose is educational and demonstrates my understanding of these mathematical concepts.*
