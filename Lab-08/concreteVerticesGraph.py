class Vertex:
    """
    Represents a vertex in the graph with directed edges.
    
    Abstract function:
        - A vertex has a label and can have outgoing edges to other vertices with weights.
    
    Representation invariant:
        - The label is a string.
        - The edges are stored as a list of tuples (target vertex, weight).
    """

    def __init__(self, label: str):
        self.label = label
        self.edges = []  # List of outgoing edges

    def add_edge(self, target: 'Vertex', weight: int):
        """Adds a directed edge to another vertex with the given weight."""
        if target not in [v for v, _ in self.edges]:
            self.edges.append((target, weight))

    def __str__(self):
        return f"Vertex({self.label}, Edges: " + ", ".join(f"{v.label}({w})" for v, w in self.edges) + ")"

    def __repr__(self):
        return self.__str__()

class ConcreteVerticesGraph:
    """
    Represents a graph with vertices that can have directed edges to other vertices.
    
    Abstract function:
        - The graph consists of vertices, and each vertex can have edges to other vertices.
    
    Representation invariant:
        - Each vertex must have a unique label.
        - Each vertex can have multiple edges to other vertices with positive weights.
    
    Rep exposure prevention:
        - The internal list of vertices is not directly accessible.
    """
    
    def __init__(self):
        self.vertices = []

    def add_vertex(self, label: str):
        """Adds a vertex to the graph."""
        vertex = Vertex(label)
        self.vertices.append(vertex)

    def add_edge(self, source_label: str, target_label: str, weight: int):
        """Adds a directed edge between two vertices."""
        source = next((v for v in self.vertices if v.label == source_label), None)
        target = next((v for v in self.vertices if v.label == target_label), None)
        
        if source and target:
            source.add_edge(target, weight)

    def checkRep(self):
        """Checks if the representation invariant holds."""
        assert len(self.vertices) == len(set(v.label for v in self.vertices)), \
            "Vertices must have unique labels."
        assert all(len(v.edges) == len(set(v.edges)) for v in self.vertices), \
            "Each vertex must have unique edges."

    def __str__(self):
        """Provides a human-readable representation of the graph."""
        return "Vertices: " + ", ".join(map(str, self.vertices))

    def __repr__(self):
        return self.__str__()

# Example of how the graph works
graph = ConcreteVerticesGraph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_edge("A", "B", 5)
graph.checkRep()

print(graph)  # Prints human-readable representation
