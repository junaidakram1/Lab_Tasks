import unittest
from expression import Expression, Number, Variable, BinaryOperation


class TestExpression(unittest.TestCase):
    def test_number(self):
        num1 = Number(5)
        num2 = Number(5.0)
        self.assertEqual(str(num1), "5")
        self.assertEqual(num1, num2)
        self.assertEqual(hash(num1), hash(num2))

    def test_variable(self):
        var1 = Variable("x")
        var2 = Variable("x")
        var3 = Variable("y")
        self.assertEqual(str(var1), "x")
        self.assertEqual(var1, var2)
        self.assertNotEqual(var1, var3)
        self.assertNotEqual(hash(var1), hash(var3))

    def test_binary_operation(self):
        expr1 = BinaryOperation(Number(1), "+", Variable("x"))
        expr2 = BinaryOperation(Number(1), "+", Variable("x"))
        expr3 = BinaryOperation(Variable("x"), "+", Number(1))
        self.assertEqual(str(expr1), "(1 + x)")
        self.assertEqual(expr1, expr2)
        self.assertNotEqual(expr1, expr3)
        self.assertEqual(hash(expr1), hash(expr2))
        self.assertNotEqual(hash(expr1), hash(expr3))


if __name__ == "__main__":
    unittest.main()
