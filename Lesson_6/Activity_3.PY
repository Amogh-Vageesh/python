marks = float(input("Enter your marks : "))

if marks <= 100 and marks >= 90:
    print("U scored 'A+' congrats!")
elif marks <= 89.9 and marks >= 80:
    print("U scored 'A' congrats!")
elif marks <= 79.9 and marks >= 75:
    print("U scored 'A-' congrats!")
elif marks <= 74.9 and marks >= 60:
    print("U scored 'B' try better next time!")
elif marks <= 59.9 and marks >= 50:
    print("U scored 'C' try better next time!")
elif marks <= 49.9 and marks >= 35:
    print("U scored 'D' try better next time!")
elif marks <= 35.9:
    print("U scored 'F' try better next time!")



