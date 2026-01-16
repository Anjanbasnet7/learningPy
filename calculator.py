def calculate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Error: division by zero"
        return a / b
    else:
        return "Invalid operator"


while True:
    try:
        x = float(input("Enter first number: "))
        op = input("Enter operator (+ - * /): ")
        y = float(input("Enter second number: "))

        print("Result:", calculate(x, y, op))

    except ValueError:
        print("Enter numbers only")

    again = input("Continue? (y/n): ").lower()
    if again != "y":
        break
