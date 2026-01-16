# Calculator using functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def calculator():
    while True:
        print("\n--- Simple Calculator ---")
        print("Options: +  -  *  /")
        
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        op = input("Enter operator (+ - * /): ")
        
        if op == '+':
            result = add(a, b)
        elif op == '-':
            result = subtract(a, b)
        elif op == '*':
            result = multiply(a, b)
        elif op == '/':
            result = divide(a, b)
        else:
            print("Invalid operator!")
            continue
        
        print(f"Result: {result}")
        
        choice = input("Do you want to calculate again? (y/n): ").lower()
        if choice != 'y':
            print("Exiting calculator.")
            break

# Run the calculator
calculator()
