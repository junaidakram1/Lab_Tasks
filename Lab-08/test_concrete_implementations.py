# test_graphs.py

from concreteEdgesGraph import ConcreteEdgesGraph
from concreteVerticesGraph import ConcreteVerticesGraph

def test_concrete_edges_graph():
    # Create a new graph
    graph = ConcreteEdgesGraph()

    # Add vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")

    # Add edges
    graph.add_edge("A", "B", 10)
    graph.add_edge("A", "C", 5)
    graph.add_edge("B", "C", 15)

    # Check representation invariant
    graph.checkRep()

    # Separate tests for vertices and edges to avoid ordering issues
    vertices_output = str(graph).split("\n")[0]
    edges_output = str(graph).split("\n")[1]

    expected_vertices_output = "Vertices: {'A', 'B', 'C'}"
    assert set(vertices_output[10:].strip("{}").split(", ")) == set(expected_vertices_output[10:].strip("{}").split(", ")), \
        f"Expected vertices: {expected_vertices_output}, but got: {vertices_output}"

    expected_edges_output = "Edges: Edge(A -> B, weight=10), Edge(A -> C, weight=5), Edge(B -> C, weight=15)"
    assert edges_output == expected_edges_output, f"Expected edges: {expected_edges_output}, but got: {edges_output}"
    
    print("ConcreteEdgesGraph Test Passed!")


def test_concrete_vertices_graph():
    # Create a new graph
    graph = ConcreteVerticesGraph()

    # Add vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")

    # Add edges
    graph.add_edge("A", "B", 10)
    graph.add_edge("A", "C", 5)
    graph.add_edge("B", "C", 15)

    # Check representation invariant
    graph.checkRep()

    # Test the string representation of the graph
    expected_output = "Vertices: Vertex(A, Edges: B(10), C(5)), Vertex(B, Edges: C(15)), Vertex(C, Edges: )"
    assert str(graph) == expected_output, f"Expected: {expected_output}, but got: {str(graph)}"
    
    print("ConcreteVerticesGraph Test Passed!")

# Run the tests
if __name__ == "__main__":
    test_concrete_edges_graph()
    test_concrete_vertices_graph()
