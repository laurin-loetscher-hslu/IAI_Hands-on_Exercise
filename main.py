import sys
from calculator.operations import *


def main():
    # Check if enough arguments are provided
    if len(sys.argv) < 4:
        print("Usage: python main.py <operation> <a> <b>")
        print("Available operations: add, subtract, multiply, divide, exponentiate")
        sys.exit(1)

    # Retrieve command-Line arguments
    operation = sys.argv[1]
    try:
        a = float(sys.argv[2])
        b = float(sys.argv[3])
    except ValueError:
        print("Error: Arguments 'a' and 'b' must be numbers.")
        sys.exit(1)

    match operation:
        case 'add':
            print(f"{a} + {b} = ", add(a, b))
        case 'subtract':
            print(f"{a} - {b} = ", subtract(a, b))
        case 'multiply':
            print(f"{a} * {b} = ", multiply(a, b))
        case 'divide':
            print(f"{a} / {b} = ", divide(a, b))
        case 'exponentiate':
            print(f"{a} ^ {b} = ", exponentiate(a, b))
        case _:
            print("Available operations: add, subtract, multiply, divide, exponentiate")
            sys.exit(1)


if __name__ == "__main__":
    main()
