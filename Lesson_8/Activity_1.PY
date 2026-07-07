n = int(input("Enter a number to print the sum until that number: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i
print("The sum of numbers from 1 to", n, "is:", sum)
