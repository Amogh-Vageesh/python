limit = int(input("Enter limit : "))
for num in range (2,limit+1):
    prime  = True
    i = 2
    while prime and i < num:
        if num%i == 0:
            prime = False
        i =i+1
    if prime:
        print(num)
