def count_digits(number):
    # Handle the special case where the number is exactly 0
    if number == 0:
        return 1
        
    # Convert negative numbers to positive
    number = abs(number)
    count = 0
    
    while number > 0:
        count += 1
        number //= 10  # Removes the last digit
        
    return count

# Take input from the user
user_input = int(input("Enter an integer: "))
result = count_digits(user_input)

print(f"Total digits: {result}")
