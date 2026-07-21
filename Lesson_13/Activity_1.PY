def calc(bill, tip_percent):
    total_amount = bill + (bill*0.01*tip_percent)
    total = round(total_amount, 2)
    print(f"Total amount to pay: ${total}")

bill = float(input("Enter the bill amount: "))
tip_percent = float(input("Enter the tip percentage: "))

calc(bill, tip_percent)