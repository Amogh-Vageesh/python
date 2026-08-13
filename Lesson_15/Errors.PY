try:
    x,y = eval(input("Please enter two numbers separated by a comma:"))
    print(f"You entered: {x} and {y}")
    result = x / y
    print(f"The result of {x} divided by {y} is: {result}")
except ZeroDivisionError as ex:
    print(f"Error : {ex}\n Division by zero is not allowed. Please enter a non-zero divisor next time.")
except ValueError as ex:
    print(f"Error : {ex}\n Please enter valid numbers next time.")
except SyntaxError as ex:
    print(f"Error : {ex}\n Please enter the numbers in the correct format next time.")
except Exception as x:
    print(f"An unexpected error occurred: {x}\nPlease try again.")
else:
    print("No exceptions")
finally:
    print("Finally")
