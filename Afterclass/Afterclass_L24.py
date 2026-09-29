# ── GRADE BOOK ─────────────────────────────────────────────────
# Create a dictionary called grades with at least 5 student name-score pairs.
grades = {
    "Alice": 88,
    "Bob": 73,
    "Charlie": 95,
    "Diana": 61,
    "Eve": 82,
}

print("=" * 38)
print("       📚  STUDENT GRADE BOOK")
print("=" * 38)

# ── CLASS AVERAGE ──────────────────────────────────────────────
# Use a for loop to add up all the scores in grades.values()
total = 0
for score in grades.values():
    total += score

# Divide total by the number of students to get the average
average = total / len(grades)

# Print the average formatted to one decimal place
print(f"Class average : {average:.1f}")

# ── TOP AND BOTTOM ─────────────────────────────────────────────
# Use max() with key=grades.get to find the top student's name
top_student = max(grades, key=grades.get)

# Use min() with key=grades.get to find the bottom student's name
bottom_student = min(grades, key=grades.get)

# Print both names and their scores
print(f"Highest score : {top_student} ({grades[top_student]})")
print(f"Lowest score  : {bottom_student} ({grades[bottom_student]})")
print()

# ── STUDENT LOOKUP ─────────────────────────────────────────────
# Ask the user to type a student name using input()
name = input("Look up a student (enter name): ")

# Use grades.get(name, None) to look up their score
score = grades.get(name, None)

# Check if found and display the result
if score is not None:
    print(f"{name}'s score: {score}")
else:
    print(f"{name} was not found in the grade book.")