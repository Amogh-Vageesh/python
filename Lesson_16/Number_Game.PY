import random

playing = True
number = random.randint(0, 9)

print("\n=====NUMBER_GAME=====\n")
print("Rules:-\n 1. I will generate a random no. from 0-9, and you have to choose 1 digit at a time.")
print("2. The game ends when you guess the correct number.\n")

while playing:
    try:
        choice = int(input("Enter your choice or '10' to exit!\n : "))
    except ValueError as ex:
        print(f"Error: {ex}\nPlease enter a valid number next time.")
        continue
    except EOFError:
        print("\nInput closed. Exiting game.\n")
        break

    if choice == 10:
        print("\nThank you for playing\n")
        break

    if not 0 <= choice <= 9:
        print("Please enter a number from 0 to 9 or 10 to exit.")
        continue

    if choice == number:
        print(f"You win the game!\nThe number was {number}")
        break

    if choice > number:
        print(f"Your choice of {choice} is greater than the number.")
    elif choice < number:
        print(f"Your choice of {choice} is lower than the number.")