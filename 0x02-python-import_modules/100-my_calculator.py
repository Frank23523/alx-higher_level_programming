#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == '+':
        solution = add(a, b)
    elif sys.argv[2] == '-':
        solution = sub(a, b)
    elif sys.argv[2] == '*':
        solution = mul(a, b)
    elif sys.argv[2] == '/':
        solution = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print(f"{a} {sys.argv[2]} {b} = {solution}")
