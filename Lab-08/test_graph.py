# test_graph.py
import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    
    def setUp(self):
        """Set up a new empty graph before each test."""
        self.graph = Graph()

    def test_add_vertex(self):
        """Test adding vertices."""
        self.assertTrue(self.graph.add("A"))
        self.assertFalse(self.graph.add("A"))  # Vertex already exists

    def test_set_edge(self):
        """Test adding and modifying edges."""
        self.graph.add("A")
        self.graph.add("B")
        self.assertEqual(self.graph.set("A", "B", 5), 0)  # New edge
        self.assertEqual(self.graph.set("A", "B", 10), 5)  # Update edge
        self.assertEqual(self.graph.set("A", "B", 0), 10)  # Remove edge

    def test_remove_vertex(self):
        """Test removing vertices."""
        self.graph.add("A")
        self.assertTrue(self.graph.remove("A"))
        self.assertFalse(self.graph.remove("A"))  # Vertex already removed

    def test_vertices(self):
        """Test getting all vertices."""
        self.graph.add("A")
        self.graph.add("B")
        self.assertEqual(self.graph.vertices(), {"A", "B"})

    def test_sources(self):
        """Test retrieving sources for a target."""
        self.graph.set("A", "B", 5)
        self.graph.set("C", "B", 10)
        self.assertEqual(self.graph.sources("B"), {"A": 5, "C": 10})

    def test_targets(self):
        """Test retrieving targets for a source."""
        self.graph.set("A", "B", 5)
        self.graph.set("A", "C", 10)
        self.assertEqual(self.graph.targets("A"), {"B": 5, "C": 10})

if __name__ == "__main__":
    unittest.main()
