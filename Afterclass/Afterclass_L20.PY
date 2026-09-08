# Step 1: Create a tuple with different data types (Habit Name, Active Status, Days, Avg Time in mins)
habit_info = ("Reading", True, 7, 20.5)
print("Habit Info:", habit_info)

# Step 2: Create a tuple of daily habit completion (1 = completed, 0 = missed)
weekly_habits = (1, 0, 1, 1, 0, 1, 1)
print("Weekly Habits Record:", weekly_habits)

# Step 3: Find the length of the tuple
print("Total days tracked:", len(weekly_habits))

# Step 4: Access items using indexing
print("Day 1 status:", weekly_habits[0])
print("Day 4 status:", weekly_habits[3])

# Step 5: Access a range using slicing
first_three_days = weekly_habits[0:3]
print("First three days:", first_three_days)

weekend_days = weekly_habits[5:7]
print("Weekend days:", weekend_days)

# Step 6: Tuples are immutable, so add a new day using the + operator
weekly_habits = weekly_habits + (1,)
print("After adding one more day:", weekly_habits)

# Step 7: Count completed and missed days
completed = weekly_habits.count(1)
missed = weekly_habits.count(0)
print("Completed days:", completed)
print("Missed days:", missed)

# Check progress using a loop
done = 0
not_done = 0

for i in range(0, len(weekly_habits)):
    if weekly_habits[i] == 1:
        done += 1
    else:
        not_done += 1

if done > not_done:
    print("Great habit progress!")
else:
    print("Try to be more consistent!")

# Step 8: Final Weekly Habit Tracker summary
print("")
print("===== WEEKLY HABIT TRACKER =====")
print("Habit Name:", habit_info[0])
print("Weekly Record:", weekly_habits)
print("Completed Days:", done)
print("Missed Days:", not_done)
print("================================")