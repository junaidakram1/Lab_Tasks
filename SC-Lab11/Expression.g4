// Expression.g4

grammar Expression;

expression: term ((PLUS | MINUS) term)*;

term: factor ((MUL | DIV) factor)*;

factor: NUMBER | variable | LPAREN expression RPAREN;

PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';

LPAREN: '(';
RPAREN: ')';

NUMBER: [0-9]+ ('.' [0-9]+)?;

variable: [a-zA-Z]+;

WS: [ \t\r\n]+ -> skip;
