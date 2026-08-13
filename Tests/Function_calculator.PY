result = 0
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b


while True:

    print("=== FUNCTION CALCULATOR ===\n")
    print("1. Add (+)")
    print("2. minus (-)")
    print("3. multiply (*)")
    print("4. Divide (/)")
    print("5. quit/stop the program\n")

    try:
        choice = int(input("select a  operator (1-5)\n : "))

        if choice == 5:
            print("Thank you for playing\n")
            break

        a = float(input("Enter 1st number: "))
        b = float(input("Enter 2nd number: "))

        if choice == 1:
            result = add(a,b)
            print(f"result is {result}")
        elif choice == 2:
            subtract(a,b)
            print(f"result is {result}")
        elif choice == 3:
            multiply(a,b)
            print(f"result is {result}")
        elif choice == 4:
            divide(a,b)
            print(f"result is {result}")
        else:
            print(f"{choice} is an invalid choice")

    except ValueError as ve:
        print(f"Error: {ve} is not a valid numerical value")

    except ZeroDivisionError as zde:
        print(f"Error: cannot divide by 0")