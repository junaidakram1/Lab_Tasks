class Graph:
    def __init__(self):
        self._graph = {}

    def set(self, word1, word2, weight):
        """Add a directed edge from word1 to word2 with the specified weight."""
        if word1 not in self._graph:
            self._graph[word1] = {}
        self._graph[word1][word2] = weight

    def targets(self, word):
        """Get the target words and their weights for the given word."""
        return self._graph.get(word, {})
