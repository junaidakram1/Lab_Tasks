from Expression import Expression

def main():
    while True:
        try:
            expression_str = input("Enter an expression: ")
            if expression_str.lower() == 'exit':
                break
            if expression_str.startswith('!d/d'):
                _, expr, var = expression_str.split()
                result = Expression.parse(expr).differentiate(var)
                print(f"Differentiated result: {result}")
            elif expression_str.startswith('!simplify'):
                parts = expression_str.split()
                expr = parts[1]
                env = dict(pair.split('=') for pair in parts[2:])
                env = {k: float(v) for k, v in env.items()}
                result = Expression.parse(expr).simplify(env)
                print(f"Simplified result: {result}")
            else:
                result = Expression.parse(expression_str)
                print(f"Parsed result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
