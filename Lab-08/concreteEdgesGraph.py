class Edge:
    """
    Represents a directed edge with a weight.
    
    Abstract function:
        - An edge connects two vertices with a specific weight.
    
    Representation invariant:
        - The weight of an edge must be a positive integer.
        - The source and target vertices must be valid strings.
    """
    
    def __init__(self, source: str, target: str, weight: int):
        assert weight > 0, "Edge weight must be positive."
        self.source = source
        self.target = target
        self.weight = weight

    def __str__(self):
        return f"Edge({self.source} -> {self.target}, weight={self.weight})"
    
    def __repr__(self):
        return self.__str__()

class ConcreteEdgesGraph:
    """
    Represents a weighted directed graph using a set of vertices and a list of edges.
    
    Abstract function:
        - The graph consists of vertices and directed edges with weights.
    
    Representation invariant:
        - Vertices are unique and each edge connects valid vertices with positive weights.
        - The list of edges contains only valid edges.
    
    Rep exposure prevention:
        - The internal vertices set and edges list are not directly accessible outside the class.
    """

    def __init__(self):
        self.vertices = set()  # Unique set of vertices
        self.edges = []        # List of edges

    def add_vertex(self, vertex: str):
        """Adds a vertex to the graph."""
        self.vertices.add(vertex)

    def add_edge(self, source: str, target: str, weight: int):
        """Adds a directed edge to the graph."""
        if source in self.vertices and target in self.vertices:
            edge = Edge(source, target, weight)
            self.edges.append(edge)

    def checkRep(self):
        """Checks if the representation invariant holds."""
        # Check all edges have valid source and target vertices
        assert all(e.source in self.vertices and e.target in self.vertices for e in self.edges), \
            "All edges must reference valid vertices."
        
        # Check that all vertices are unique
        assert len(self.vertices) == len(set(self.vertices)), "Vertices must be unique."

    def __str__(self):
        """Provides a human-readable representation of the graph."""
        edges_str = ", ".join(map(str, self.edges))
        return f"Vertices: {self.vertices}\nEdges: {edges_str}"

    def __repr__(self):
        return self.__str__()

# Example of how the graph works
graph = ConcreteEdgesGraph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_edge("A", "B", 10)
graph.checkRep()

print(graph)  # Prints human-readable representation
