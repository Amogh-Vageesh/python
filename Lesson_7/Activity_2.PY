# exam qualification program
# condition : have to have atleast 80% or more attendance unless you have medical reason if so only 60% is required

MR = None
attendance = int(input("Enter your attendance percentage for this year in numbers : "))
if attendance >= 80:
    print("You are eligible for the final exam")
else:
    if attendance >= 60:
        MR = input(("Do u have medical reasons?(yes/no)"))
        if MR in ("yes", "no", "Yes", "No"):
            if MR.lower() == "yes":
                print("You are eligible for the final exam")
            else:
                print("You are not eligible for the final exam")
    else:
        if attendance < 60:
            print("You are not eligible for the final exam")