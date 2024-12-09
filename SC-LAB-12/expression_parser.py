class ExpressionParser:
    def __init__(self, expression):
        self.tokens = self.tokenize(expression)
        self.index = 0

    def tokenize(self, expression):
        """
        Tokenize the input string into numbers, operators, and parentheses.
        """
        import re
        return re.findall(r'\d+\.?\d*|[+\-*/()]', expression)

    def parse(self):
        """
        Parse the expression starting with the lowest precedence (addition/subtraction).
        """
        return self.parse_expression()

    def parse_expression(self):
        """
        Parse addition and subtraction by recursively parsing multiplication/division first.
        """
        result = self.parse_term()
        while self.index < len(self.tokens) and self.tokens[self.index] in ('+', '-'):
            operator = self.tokens[self.index]
            self.index += 1
            if operator == '+':
                result += self.parse_term()
            elif operator == '-':
                result -= self.parse_term()
        return result

    def parse_term(self):
        """
        Parse multiplication and division by recursively parsing factors.
        """
        result = self.parse_factor()
        while self.index < len(self.tokens) and self.tokens[self.index] in ('*', '/'):
            operator = self.tokens[self.index]
            self.index += 1
            if operator == '*':
                result *= self.parse_factor()
            elif operator == '/':
                denominator = self.parse_factor()
                if denominator == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                result /= denominator
        return result

    def parse_factor(self):
        """
        Parse numbers and handle parentheses recursively.
        """
        token = self.tokens[self.index]
        self.index += 1
        if token == '(':
            result = self.parse_expression()
            if self.tokens[self.index] != ')':
                raise ValueError("Mismatched parentheses.")
            self.index += 1
            return result
        try:
            return float(token)
        except ValueError:
            raise ValueError(f"Invalid token: {token}")


def evaluate_expression(expression):
    """
    Public function to evaluate a mathematical expression.
    """
    parser = ExpressionParser(expression)
    return parser.parse()


if __name__ == "__main__":
    # Example expressions for testing
    expressions = [
        "3 + 5 * 2",
        "(3 + 5) * 2",
        "10 / 2 - 3",
        "3.5 * 2 + (1.2 - 0.2)",
        "1 + 2 * (3 - (4 / 2))"
    ]
    for expr in expressions:
        try:
            print(f"{expr} = {evaluate_expression(expr)}")
        except Exception as e:
            print(f"Error in '{expr}': {e}")
