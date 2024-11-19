from Graph import Graph

class GraphPoet:
    def __init__(self, corpus_file):
        self.graph = Graph()
        self._load_corpus(corpus_file)

    def _load_corpus(self, corpus_file):
        """Load the corpus file and build the graph."""
        with open(corpus_file, 'r') as file:
            words = file.read().lower().split()
            for i in range(len(words) - 1):
                word1, word2 = words[i], words[i + 1]
                current_weight = self.graph.targets(word1).get(word2, 0)
                self.graph.set(word1, word2, current_weight + 1)

    def poem(self, input_text):
        """Generate a poem with bridge words between adjacent words."""
        input_words = input_text.split()
        poem_words = [input_words[0]]  # Start with the first word

        for i in range(len(input_words) - 1):
            word1, word2 = input_words[i].lower(), input_words[i + 1].lower()
            bridge_word, max_weight = None, 0

            # Look for a bridge word between word1 and word2
            for potential_bridge, weight1 in self.graph.targets(word1).items():
                weight2 = self.graph.targets(potential_bridge).get(word2, 0)
                if weight1 > 0 and weight2 > 0:
                    if weight1 + weight2 > max_weight:
                        bridge_word, max_weight = potential_bridge, weight1 + weight2

            # If we found a bridge word, insert it
            if bridge_word:
                poem_words.append(bridge_word)

            # Always add the next word
            poem_words.append(input_words[i + 1])

        # Join the words back into a poem (with proper spacing)
        return ' '.join(poem_words)

# Ensure that 'mugar' isn't introduced in the poem when it's not relevant.
