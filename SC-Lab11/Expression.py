import re

class Expression:
    def __init__(self, expr):
        self.expr = expr

    @staticmethod
    def parse(expression_str):
        expression_str = re.sub(r'\s+', '', expression_str)
        
        if not re.match(r'^[\d+\-*/().a-zA-Z]+$', expression_str):
            raise ValueError("Invalid characters in expression")
        
        if re.search(r'[\+\-*\/]{2,}|^[\+\-*\/]|[\+\-*\/]$', expression_str) or re.search(r'\(\)', expression_str):
            raise ValueError("Invalid expression format")
        
        return Expression(expression_str)

    def differentiate(self, variable):
        def differentiate_term(term, variable):
            if term == variable:
                return "1"
            elif term.isdigit() or (term.replace('.', '', 1).isdigit() and term.count('.') < 2):
                return "0"
            elif '*' in term:
                factors = term.split('*')
                differentiated_terms = []
                for i in range(len(factors)):
                    if factors[i] == variable:
                        differentiated_terms.append('*'.join(factors[:i] + ['1'] + factors[i+1:]))
                    else:
                        differentiated_terms.append('*'.join(factors[:i] + [differentiate_term(factors[i], variable)] + factors[i+1:]))
                return ' + '.join(differentiated_terms)
            return "0"
        
        terms = re.split(r'(\+|\-)', self.expr)
        differentiated_terms = []
        for term in terms:
            if term not in ['+', '-']:
                differentiated_terms.append(differentiate_term(term, variable))
            else:
                differentiated_terms.append(term)
        
        differentiated_expr = ''.join(differentiated_terms)
        return Expression(differentiated_expr)

    def simplify(self, env):
        def eval_term(term):
            try:
                return eval(term, {}, env)
            except NameError:
                return term
        
        terms = re.split(r'(\+|\-)', self.expr)
        simplified_terms = [str(eval_term(term)) if term not in ['+', '-'] else term for term in terms]
        simplified_expr = ''.join(simplified_terms)

        try:
            result = eval(simplified_expr, {}, {})
            if isinstance(result, (int, float)):
                return result
        except Exception:
            pass

        return Expression(simplified_expr)

    def __str__(self):
        return self.expr
