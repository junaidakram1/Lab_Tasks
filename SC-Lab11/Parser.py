from Token import Token
from Number import Number
from Variable import Variable
from BinaryOperation import BinaryOperation

class Parser:
    def __init__(self, tokens):
        self.tokens = list(tokens)
        self.current = 0

    def peek(self):
        return self.tokens[self.current] if self.current < len(self.tokens) else None

    def consume(self):
        token = self.peek()
        self.current += 1
        return token

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        node = self.parse_term()
        while self.peek() and self.peek()[0] in {Token.PLUS, Token.MINUS}:
            operator = self.consume()[1]
            right = self.parse_term()
            node = BinaryOperation(node, operator, right)
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.peek() and self.peek()[0] in {Token.MUL, Token.DIV}:
            operator = self.consume()[1]
            right = self.parse_factor()
            node = BinaryOperation(node, operator, right)
        return node

    def parse_factor(self):
        token = self.consume()
        if token[0] == Token.NUMBER:
            return Number(token[1])
        elif token[0] == Token.VARIABLE:
            return Variable(token[1])
        elif token[0] == Token.LPAREN:
            node = self.parse_expression()
            if self.consume()[0] != Token.RPAREN:
                raise ValueError("Mismatched parentheses")
            return node
        raise ValueError(f"Unexpected token: {token}")
