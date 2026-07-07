while True:
    exit_check = input("type 'exit' to quit else press enter: ")
    if exit_check.lower() == 'exit':
        print("Exiting the program.")
        break
    num = input("Enter a number: ")
    digit = len(num)
    num = int(num)
    original_num = num
    sum = 0
    while num > 0:
        temp = num % 10
        temp = temp ** digit
        sum = sum + temp
        num = num // 10
    if original_num == sum:
        print(original_num, "Is an armstrong number")
    else:
        print(original_num, "Is not an armstrong number")