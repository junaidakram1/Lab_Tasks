import re

class Token:
    NUMBER = "NUMBER"
    VARIABLE = "VARIABLE"
    PLUS = "+"
    MINUS = "-"
    MUL = "*"
    DIV = "/"
    LPAREN = "("
    RPAREN = ")"

    @staticmethod
    def tokenize(expression):
        token_specification = [
            (Token.NUMBER, r"\d+(\.\d+)?"),
            (Token.VARIABLE, r"[a-zA-Z][a-zA-Z0-9]*"),
            (Token.PLUS, r"\+"),
            (Token.MINUS, r"-"),
            (Token.MUL, r"\*"),
            (Token.DIV, r"/"),
            (Token.LPAREN, r"\("),
            (Token.RPAREN, r"\)"),
            ("SKIP", r"\s+"),  # Skip whitespace
        ]
        token_regex = "|".join(f"(?P<{pair[0]}>{pair[1]})" for pair in token_specification)
        for match in re.finditer(token_regex, expression):
            kind = match.lastgroup
            value = match.group()
            if kind != "SKIP":
                yield (kind, value)
