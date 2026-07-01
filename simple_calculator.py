def calculate(a, operator, b):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    raise ValueError("Unsupported operator")


def parse_expression(expr):
    parts = expr.strip().split()
    if len(parts) != 3:
        raise ValueError("Enter expression as: number operator number")
    a_str, operator, b_str = parts
    a = float(a_str)
    b = float(b_str)
    return a, operator, b


def main():
    print("Simple calculator. Supported operators: + - * /")
    print("Type 'quit' or 'exit' to stop.")
    while True:
        try:
            expr = input("Enter expression: ")
            if expr.lower() in {"quit", "exit"}:
                print("Bye")
                break
            a, operator, b = parse_expression(expr)
            result = calculate(a, operator, b)
            print(result)
        except ValueError as err:
            print("Error:", err)
        except KeyboardInterrupt:
            print("\nBye")
            break


if __name__ == "__main__":
    main()
