def decimal_to_binary(decimal_num):
    # Handle the special case where the input is 0
    if decimal_num == 0:
        return "0"
        
    binary_digits = []
    
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_digits.append(str(remainder))
        decimal_num //= 2  # Integer division to move to the next quotient
        
    # Reverse the digits to get the correct binary order
    binary_digits.reverse()
    return "".join(binary_digits)

# Take input from the user
try:
    user_num = int(input("Enter a positive decimal number: "))
    if user_num < 0:
        print("Please enter a non-negative integer.")
    else:
        print(f"Binary representation: {decimal_to_binary(user_num)}")
except ValueError:
    print("Invalid input. Please enter a whole number.")
