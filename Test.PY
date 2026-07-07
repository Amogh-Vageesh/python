
secret_number = 9

attempts = 0

while attempts < 6:
    guess = int(input("Enter your guess: "))
    
    if guess < 9 or guess >= 10 and guess <= 15 and attempts != 6:
        print("Hot!")
        attempts += 1
        print(f"You have {6 - attempts} attempts left.")
    
    elif guess >= 15 and guess <= 30 and attempts != 6:
        print("warm!")
        attempts += 1
        print(f"You have {6 - attempts} attempts left.")

    elif guess >= 30 and guess <= 65 and attempts != 5:
        print("cold!")
        attempts += 1
        print(f"You have {6 - attempts} attempts left.")

    elif guess >= 65 and attempts != 5:
        print("Ice cold!")
        attempts += 1
        print(f"You have {6 - attempts} attempts left.")
        
