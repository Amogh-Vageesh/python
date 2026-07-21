def cube(num):
    return num ** 3
def by_3(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return False
    
print(by_3(9),by_3(4),by_3(3))  # Output: 729 False 216 