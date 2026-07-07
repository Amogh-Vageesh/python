text = input(str("Enter a string to reverse : "))
reverse = ""
for letter in text:
    reverse = letter + reverse 
print(reverse)