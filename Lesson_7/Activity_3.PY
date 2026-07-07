units = int(input("Enter your electricity bill in units : "))
amount = None
surcharge = None
if units <= 50:
    amount = units * 2.6
    surcharge = 25
elif units <= 100:
    amount = 130 + ((units - 50)* 2.6)  
    surcharge = 35
elif units <= 200:
    amount = 130 + 162.50 + ((units - 100)* 5.26)  
    surcharge = 45
else:
    amount = 130 + 162.50 + 526 +((units - 200)* 8.45)  
    surcharge = 75

total = amount + surcharge
print("\nElectricity Bill - ",total)