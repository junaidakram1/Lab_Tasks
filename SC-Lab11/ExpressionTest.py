import unittest
from Expression import Expression

class TestExpressionParsing(unittest.TestCase):
    def test_valid_expressions(self):
        expressions = [
            "3 + 2.4",
            "3 * x + 2.4",
            "3 * (x + 2.4)",
            "((3 + 4) * x * x)",
            "foo + bar + baz",
            "(2 * x) + (y * x)",
            "4 + 3 * x + 2 * x * x + 1 * x * x * (((x)))"
        ]
        for expr in expressions:
            with self.subTest(expr=expr):
                result = Expression.parse(expr)
                self.assertIsNotNone(result)

    def test_invalid_expressions(self):
        expressions = [
            "3 *",
            "( 3",
            "3 x"
        ]
        for expr in expressions:
            with self.subTest(expr=expr):
                with self.assertRaises(ValueError):
                    Expression.parse(expr)

    def test_differentiation(self):
        expressions = [
            ("x*x*x", "x", "3*x*x"),
            ("3*x*x", "x", "6*x"),
            ("x + x", "x", "1 + 1"),
            ("x*x + x", "x", "2*x + 1")
        ]
        for expr, var, expected in expressions:
            with self.subTest(expr=expr, var=var):
                result = Expression.parse(expr).differentiate(var)
                self.assertEqual(str(result), expected)

    def test_simplification(self):
        expressions = [
            ("x*x*x", {"x": 5}, 125),
            ("x*x*x + y*y*y", {"y": 10}, "x*x*x+1000"),
            ("1+2*3+8*0.5", {}, 11.0),
            ("x*x*y + y*(1+x)", {"x": 2}, "7*y")
        ]
        for expr, env, expected in expressions:
            with self.subTest(expr=expr):
                result = Expression.parse(expr).simplify(env)
                if isinstance(expected, (int, float)):
                    self.assertAlmostEqual(result, expected, places=4)
                else:
                    self.assertEqual(str(result), expected)

if __name__ == '__main__':
    unittest.main()
