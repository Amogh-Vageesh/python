def pal(tup):
    e = len(tup)-1
    s = 0
    while s<e:
        if tup[e]!=tup[s]:
            return False
        s = s+1
        e = e-1
    return True

my_tup = (1,2,3,4,3,2,1)
if pal(my_tup):
    print("this tupple is a palindrome")
else:
    print("this tupple is not a palindrome")