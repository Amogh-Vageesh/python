try:
    x = int(input("Please enter a number: "))
    print(f"You entered: {x}")
except ValueError as ex:
    print(f"Error : {ex}\n Please enter a valid number next time.")