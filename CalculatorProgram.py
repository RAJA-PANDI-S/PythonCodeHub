def calculator():
    a = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if operator == "+":
        result = a + b

    elif operator == "-":
        result = a - b

    elif operator == "*":
        result = a * b

    elif operator == "/":
        if b == 0:
            print("Cannot divide by zero.")
            return
        result = a / b

    else:
        print("Invalid operator.")
        return

    print("Result:", result)


calculator()
