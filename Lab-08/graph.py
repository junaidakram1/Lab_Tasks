# graph.py

class Graph:
    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}

    def add(self, vertex):
        """
        Add a vertex to the graph.
        
        :param vertex: The label of the vertex to add.
        :return: True if the vertex was added, False if it was already in the graph.
        """
        if vertex in self.graph:
            return False
        self.graph[vertex] = {}
        return True

    def set(self, source, target, weight):
        """
        Add, change, or remove an edge in the graph.
        
        :param source: The label of the source vertex.
        :param target: The label of the target vertex.
        :param weight: The weight of the edge. If zero, remove the edge.
        :return: The previous weight of the edge, or zero if there was no edge.
        """
        if weight < 0:
            raise ValueError("Edge weight cannot be negative")
        
        if source not in self.graph:
            self.add(source)
        if target not in self.graph:
            self.add(target)
        
        prev_weight = self.graph[source].get(target, 0)
        if weight == 0:
            self.graph[source].pop(target, None)
        else:
            self.graph[source][target] = weight
        return prev_weight

    def remove(self, vertex):
        """
        Remove a vertex and all associated edges from the graph.
        
        :param vertex: The label of the vertex to remove.
        :return: True if the vertex was in the graph, False otherwise.
        """
        if vertex not in self.graph:
            return False
        self.graph.pop(vertex)
        
        for src in self.graph:
            self.graph[src].pop(vertex, None)
        return True

    def vertices(self):
        """
        Get all vertices in the graph.
        
        :return: A set of all vertex labels in the graph.
        """
        return set(self.graph.keys())

    def sources(self, target):
        """
        Get source vertices with directed edges to a target vertex.
        
        :param target: The target vertex label.
        :return: A dictionary of source vertices and their edge weights to the target.
        """
        sources = {}
        for src in self.graph:
            if target in self.graph[src]:
                sources[src] = self.graph[src][target]
        return sources

    def targets(self, source):
        """
        Get target vertices with directed edges from a source vertex.
        
        :param source: The source vertex label.
        :return: A dictionary of target vertices and their edge weights from the source.
        """
        return self.graph.get(source, {})
