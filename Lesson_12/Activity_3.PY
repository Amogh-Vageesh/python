def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return ("Error: Division by zero is not allowed.")
    
Num1 = float(input("Enter first number: "))
Num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = addition(Num1, Num2)
    print("The sum is:", result)
elif operation == "-":
    result = subtraction(Num1, Num2)
    print("The difference is:", result)
elif operation == "*":
    result = multiplication(Num1, Num2)
    print("The product is:", result)
elif operation == "/":
    result = division(Num1, Num2)
    if division != "Error: Division by zero is not allowed.":
        print("Error: Division by zero is not allowed.")
    else:
        print("The quotient is:", result)