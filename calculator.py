def calu(firstNum,secondNum,operation):
    if operation == "+":
        return firstNum + secondNum
    elif operation == "-":
        return firstNum - secondNum
    elif operation == "*":
        return firstNum * secondNum
    elif operation == "/":
        if secondNum == 0:
            return "can't divided by zero!"
        else:
            return firstNum / secondNum
    else:
        print("Invali input!")

while True:
    firstNum = float(input("Enter first number:"))
    secondNum = float(input("Enter second number:"))
    operation = input("Enter your operation(+ , - , / , *):")
    result = calu(firstNum,secondNum,operation)
    print("Result:",result)

    check = input("Do you want to use calcualtor again(y/n)").lower()
    if check == "n":
        print("Good bye")
        break
    else:
        print("Please!input the valid(y/n)")
