items = ["pencil","eraser","notebook","sharpener","glue"]
stock_counts = [12,0,8,5,3]
prices = [10,5,40,15,20]

inventory = {item: count for item, count in zip(items,stock_counts)}
print(f"Full inventory : {inventory}")

in_stock = [item for item in items if inventory[item]> 0]
print(f"Items in stock : {in_stock}")
print(f"Prices : {prices}")

chosen_item = input("Which item do u want to buy? ")

if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(f"{chosen_item} is out of stock! Stopping the checker")
    exit()

markup = int(input("Enter the markup amount to add to every price : "))

marked_up_prices = list(map(lambda p: p + markup,prices))
print(f"Marked up prices : {marked_up_prices}")

item_index = items.index(chosen_item)
chosen_price = marked_up_prices[item_index]
print(f"Price of {chosen_item} after markup is {chosen_price}")

inventory[chosen_item] = inventory[chosen_item] - 1
print(f"{chosen_item} purchased! Remaining stock : {inventory[chosen_item]}")

print("")
print("===== SCHOOL STORE INVENTORY CHECKER =====")
print(f"Item bought : {chosen_item}")
print(f"Amount paid : {chosen_price}")
print(f"Updated inventory : {inventory}")
print("==============================================")