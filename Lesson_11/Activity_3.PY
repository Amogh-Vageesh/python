row_size = int(input("Enter number of rows : "))
if row_size < 1:
    print("Please enter a positive integer.")
if row_size % 2 == 0:
    half_diamond_size=int(row_size/2)
else:
    half_diamond_size=int((row_size/2)+1)
space = half_diamond_size - 1
for i in range(1, half_diamond_size + 1):
    for j in range(1, space + 1):
        print(end=" ")
    space -= 1
    for j in range(2 * i-1):
        print(end="*")
    print()
space = 1
for i in range(1, half_diamond_size+1):
    for j in range(1, space + 1):
        print(end=" ")
    space += 1
    for j in range(1,2*(half_diamond_size-i)):
        print(end="*")
    print()