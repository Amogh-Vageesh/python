    
while True:
    tuple = ()

    q = input("enter exit to exit or type anything else ")

    if q or un or n or password or dob or pob == "exit":
        break

    un = input("enter a username ")
    n = input("enter a name ")
    password = input("enter a password ")
    dob = input("enter a date of birth ")
    pob = input("enter a place of birth ")

    tuple = tuple + (un, n, password, dob, pob)
    print(f"the details u entered are {tuple}\n")

