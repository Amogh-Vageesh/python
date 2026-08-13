import random
show_answer = False
computer_action = ""

while True:
    print("\n =====Rock-Paper-Scissors===== \n")

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    if show_answer:
        print(f"the computer chose: {computer_action.title()}\n")

    user_action = input("Enter a Choice (Rock, Paper, Scissors): ").strip().lower()

    if user_action not in possible_actions:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.\n")
        continue

    if user_action == computer_action:
        print(f"Both players chose {user_action.title()}, it's a tie\n")

    elif user_action == "rock":
        if computer_action == "scissors":
            print(f"\n{user_action.title()} beats {computer_action.title()} you win!\n")
        else:
            print(f"\n{computer_action.title()} covers {user_action.title()} you lose.\n")

    elif user_action == "paper":
        if computer_action == "rock":
            print(f"\n{user_action.title()} beats {computer_action.title()} you win!\n")
        else:
            print(f"\n{computer_action.title()} covers {user_action.title()} you lose.\n")

    elif user_action == "scissors":
        if computer_action == "paper":
            print(f"\n{user_action.title()} beats {computer_action.title()} you win!\n")
        else:
            print(f"\n{computer_action.title()} covers {user_action.title()} you lose.\n")

    play_again = input("Play again? (y/n): ").strip().lower()
    if play_again != "y":
        print("Thank you for playing\n")
        break