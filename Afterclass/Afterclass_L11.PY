# Input: Number of rows for the triangle
rows = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(1, rows + 1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    # Print asterisks
    print("*" * i)
