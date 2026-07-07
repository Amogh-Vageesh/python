weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))

BMI = weight / (height/100) ** 2
print int(BMI)
if BMI <=18.5:
    print ("You are underweight")
elif BMI <=24.9:
    print ("Your are healthy weight") 
elif BMI <=29.9:
    print ("You are overweight")
else:
    print ("You are obese")
