def calculate_change(paid,price):
    change = paid - price
    return change

Chips_price = 50  # price of the snack in units
coke_price = 75  # price of the snack in units
lollipop_price = 30  # price of the snack in units
ice_cream_price = 100  # price of the snack in units
biscuit_price = 60  # price of the snack in units

print("===== SNACK VENDING MACHINE =====")

print(f"Chips(1): {Chips_price} units")
print(f"Coke(2): {coke_price} units")
print(f"Lollipops(3): {lollipop_price} units")
print(f"ice cream(4): {ice_cream_price} units")
print(f"biscuits(5): {biscuit_price} units\n")

print("Please select a snack by entering the corresponding number")
print("Please insert money to pay for the snack.")
print("Accepted coins: 1, 5, 10, 25 units\n") 

total_inserted = 0
coins_inserted = 0

snack_choice = int(input("Enter snack number (1-5): "))
if snack_choice == 1:
        snack_price = Chips_price
        print(f"You selected Chips. Price: {snack_price} units\n")
elif snack_choice == 2:
        snack_price = coke_price
        print(f"You selected Coke. Price: {snack_price} units\n")
elif snack_choice == 3:
        snack_price = lollipop_price
        print(f"You selected Lollipops. Price: {snack_price} units\n")
elif snack_choice == 4:
        snack_price = ice_cream_price
        print(f"You selected Ice Cream. Price: {snack_price} units\n")
elif snack_choice == 5:
        snack_price = biscuit_price
        print(f"You selected Biscuits. Price: {snack_price} units\n")


while True:
    
    coin = int(input("Insert coin (or type 0 to finish): "))
    if coin == 0:
        # user chose to finish inserting coins
        print("Finishing coin insertion.\n")
    elif coin not in (1, 5, 10, 25):
        print("Invalid coin. Please insert a valid coin.\n")
        continue
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted: {coin} units Total inserted: {total_inserted} units\n")

    if total_inserted >= snack_price:
        print("Payment complete. Thank you for your purchase!\n")
        break

change_due = calculate_change(total_inserted,snack_price)
print("dispensing snack...\n")
if change_due > 0:
    print(f"Dispensing change: {change_due} units\n")
else:
    print("No change due.\n")

print("===== TRANSACTION SUMMARY =====\n")
print(f"Snack selected: {snack_choice}")
print(f"Snack price: {snack_price} units")
print(f"Total inserted: {total_inserted} units")
print(f"Change given: {change_due} units")
print(f"Coins inserted: {coins_inserted}")
print("================================\n")
print("Thank you for using the snack vending machine!\n")