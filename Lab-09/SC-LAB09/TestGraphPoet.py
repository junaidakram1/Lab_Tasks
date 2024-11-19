import unittest
from GraphPoet import GraphPoet

class TestGraphPoet(unittest.TestCase):
    def test_poem_generation(self):
        corpus_path = "corpus.txt"
        with open(corpus_path, 'w') as file:
            file.write("This is a test of the Mugar Omni Theater sound system.")
        
        poet = GraphPoet(corpus_path)
        input_text = "Test the system."
        expected_output = "Test of the system."
        self.assertEqual(poet.poem(input_text), expected_output)

if __name__ == "__main__":
    unittest.main()
