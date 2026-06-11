actual_cost=float(input("Enter the actual cost of the item : "))
sale_amount=float(input("Enter the sale amount of the item : "))

if sale_amount > actual_cost:
    amount = sale_amount - actual_cost
    print("total profit made is : ",amount)
else:
    print("No profit is made")
    amount = sale_amount - actual_cost
    print("Loss is",amount)