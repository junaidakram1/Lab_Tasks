from Expression import Expression

class BinaryOperation(Expression):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        return f"({self.left} {self.operator} {self.right})"

    def __eq__(self, other):
        return (
            isinstance(other, BinaryOperation)
            and self.left == other.left
            and self.operator == other.operator
            and self.right == other.right
        )

    def __hash__(self):
        return hash((self.left, self.operator, self.right))
