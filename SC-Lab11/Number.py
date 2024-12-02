from Expression import Expression

class Number(Expression):
    def __init__(self, value):
        self.value = float(value)

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return isinstance(other, Number) and self.value == other.value

    def __hash__(self):
        return hash(self.value)
