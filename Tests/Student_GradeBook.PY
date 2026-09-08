gradebook = {}
for i in range (5):
    name = input("Enter the students name : ")
    score = int(input("Enter the students score : "))
    gradebook[name] = score

total = 0
for score in gradebook.values():
    total = total + score

avg = total / len(gradebook)
highest = max(gradebook.values())
lowest = min(gradebook.values())
top_student = ""
bottom_student = ""

for name, score in gradebook.items():
    if score == highest:
        top_student = name
    if score == lowest:
        bottom_student = name

print("\n === STUDENT GRADE BOOK ===")

for name,score in gradebook.items():
    if score >= 90:
        Grade = "A"
    elif score >= 80:
        Grade = "B"
    elif score >= 70:
        Grade = "C"
    elif score >= 60:
        Grade = "D"
    else:
        Grade = "F"

print(f"\nClass Average - {avg}")
print(f"Highest Score - {highest} - Student : {top_student}")
print(f"Lowest Score - {lowest} - Student : {bottom_student}")

while True:

    search = input("\n Enter A students name to search them up! : ")
    if search == "exit":
        print("\n")
        break
    score = gradebook.get(search)

    if score is not None:
        if score >= 90:
            Grade = "A"
        elif score >= 80:
            Grade = "B"
        elif score >= 70:
            Grade = "C"
        elif score >= 60:
            Grade = "D"
        else:
            Grade = "F"

        print(f"{search} scored {score} and got grade {Grade}")
    else:
        print("student {search} not found.")