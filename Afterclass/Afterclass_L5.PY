# Movie Ticket Pricing Program

def calculate_ticket_price():
    # Get the user's age as an integer
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Evaluate conditional statements to determine the price
    if age < 5:
        # Children under 5 get in for free
        price = 0
        print(f"Age {age}: Your ticket is free!")
    elif age <= 12:
        # Ages 5 to 12 get a child discount
        price = 150
        print(f"Age {age}: You qualify for the child ticket. Price: ₹{price}")
    elif age >= 65:
        # Ages 65 and older get a senior discount
        price = 200
        print(f"Age {age}: You qualify for the senior discount. Price: ₹{price}")
    else:
        # Standard adult pricing for ages 13 to 64
        price = 350
        print(f"Age {age}: Standard adult ticket. Price: ₹{price}")

# Run the program
calculate_ticket_price()
