def check_character():
    # Take a single character input from the user
    user_input = input("Enter a single character: ")

    # Ensure the user entered exactly one character
    if len(user_input) != 1:
        print("Error: Please enter exactly one character.")
    
    # Check if the character is an alphabet letter
    elif user_input.isalpha():
        print(f"Success! '{user_input}' is an alphabet letter.")
        
        # Additional nested condition to check the case
        if user_input.isupper():
            print("It is an uppercase letter.")
        else:
            print("It is a lowercase letter.")
            
    # If it is length 1 but not alphabetical, it is something else
    else:
        print(f"Notice: '{user_input}' is NOT an alphabet letter.")

# Run the program
check_character()
