while True : 
    num = input("Enter a number (or type 'exit' to quit): ")
    if num.lower() == 'exit':
        print("Exiting the program.")
        break
    num = int(num)
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")