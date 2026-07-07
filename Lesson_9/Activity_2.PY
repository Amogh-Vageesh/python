while True:
    num = input("Enter a number (or type 'exit' to quit): ")
    if num.lower() == 'exit':
        print("Exiting the program.")
        break

    try:
        n = int(num)
    except ValueError:
        print("Invalid input — please enter an integer or 'exit'.")
        continue

    if n < 1:
        print("Please enter a positive integer.")
        continue

    total = sum(range(1, n + 1))
    print("The sum of numbers from 1 to", n, "is:", total)
