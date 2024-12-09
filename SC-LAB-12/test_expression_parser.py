import unittest
from expression_parser import evaluate_expression

class TestExpressionParser(unittest.TestCase):
    def test_basic_operations(self):
        self.assertAlmostEqual(evaluate_expression("3 + 5"), 8)
        self.assertAlmostEqual(evaluate_expression("10 - 2"), 8)
        self.assertAlmostEqual(evaluate_expression("4 * 2"), 8)
        self.assertAlmostEqual(evaluate_expression("16 / 2"), 8)

    def test_operator_precedence(self):
        self.assertAlmostEqual(evaluate_expression("3 + 5 * 2"), 13)
        self.assertAlmostEqual(evaluate_expression("(3 + 5) * 2"), 16)
        self.assertAlmostEqual(evaluate_expression("10 / 2 - 3"), 2)
        self.assertAlmostEqual(evaluate_expression("1 + 2 * (3 - 1)"), 5)

    def test_floating_point(self):
        self.assertAlmostEqual(evaluate_expression("3.5 * 2"), 7.0)
        self.assertAlmostEqual(evaluate_expression("1.2 - 0.2"), 1.0)

    def test_parentheses(self):
        self.assertAlmostEqual(evaluate_expression("(3 + 5) * (2 + 1)"), 24)
        self.assertAlmostEqual(evaluate_expression("((3 + 5) * 2) + 1"), 17)

    def test_invalid_expressions(self):
        with self.assertRaises(ValueError):
            evaluate_expression("3 + + 5")
        with self.assertRaises(ValueError):
            evaluate_expression("3 + (5 * 2")
        with self.assertRaises(ValueError):
            evaluate_expression(")3 + 5(")
        with self.assertRaises(ZeroDivisionError):
            evaluate_expression("3 / 0")

if __name__ == "__main__":
    unittest.main()
