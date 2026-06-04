import random
from datetime import date, timedelta

# Define a date range for the random birthdays (e.g., the last 30 years)
start_date = date(1996, 1, 1)
end_date = date(2025, 12, 31)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

# Generate random days to add to the start date
random_days_1 = random.randrange(days_between_dates)
random_days_2 = random.randrange(days_between_dates)
random_days_3 = random.randrange(days_between_dates)
random_days_4 = random.randrange(days_between_dates)
random_days_5 = random.randrange(days_between_dates)

# Store the randomly generated birthdays in 5 distinct variables
birthday_1 = start_date + timedelta(days=random_days_1)
birthday_2 = start_date + timedelta(days=random_days_2)
birthday_3 = start_date + timedelta(days=random_days_3)
birthday_4 = start_date + timedelta(days=random_days_4)
birthday_5 = start_date + timedelta(days=random_days_5)

# Output the results
print("Variable 1:", birthday_1)
print("Variable 2:", birthday_2)
print("Variable 3:", birthday_3)
print("Variable 4:", birthday_4)
print("Variable 5:", birthday_5)
