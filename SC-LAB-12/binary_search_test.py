import unittest
from binary_search_recursive import binary_search_recursive, binary_search_all_indices, binary_search_recursive_strings


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_recursive(self):
        arr = [1, 3, 5, 7, 9]
        self.assertEqual(binary_search_recursive(arr, 5, 0, len(arr) - 1), 2)
        self.assertEqual(binary_search_recursive(arr, 2, 0, len(arr) - 1), -1)

    def test_binary_search_all_indices(self):
        arr = [1, 2, 2, 3, 4, 5, 5]
        self.assertEqual(binary_search_all_indices(arr, 2, 0, len(arr) - 1, []), [1, 2])
        self.assertEqual(binary_search_all_indices(arr, 6, 0, len(arr) - 1, []), [])

    def test_binary_search_recursive_strings(self):
        arr = ["apple", "banana", "cherry", "date", "fig"]
        self.assertEqual(binary_search_recursive_strings(arr, "cherry", 0, len(arr) - 1), 2)
        self.assertEqual(binary_search_recursive_strings(arr, "grape", 0, len(arr) - 1), -1)

if __name__ == "__main__":
    unittest.main()
