from abc import ABC, abstractmethod
from typing import Any


class Expression(ABC):
    """
    Abstract base class for immutable and recursive expressions.
    """

    @abstractmethod
    def __str__(self) -> str:
        """Returns a string representation of the expression."""
        pass

    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        """Checks structural equality of expressions."""
        pass

    @abstractmethod
    def __hash__(self) -> int:
        """Computes the hash code for the expression."""
        pass


class Number(Expression):
    """
    Represents a numeric constant in the expression.
    """

    def __init__(self, value: float):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Number) and self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)


class Variable(Expression):
    """
    Represents a variable in the expression.
    """

    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Variable) and self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


class BinaryOperation(Expression):
    """
    Represents a binary operation like addition or multiplication.
    """

    def __init__(self, left: Expression, operator: str, right: Expression):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self) -> str:
        return f"({self.left} {self.operator} {self.right})"

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, BinaryOperation)
            and self.operator == other.operator
            and self.left == other.left
            and self.right == other.right
        )

    def __hash__(self) -> int:
        return hash((self.left, self.operator, self.right))
