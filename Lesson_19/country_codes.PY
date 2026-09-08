country_codes = {
    "usa":"+1",
    "india":"+91",
    "uk":"+44"
}

while True:
    inp = input("Enter a country code to search its codes(or 'q' to exit) : ")
    inp = inp.lower()
    if inp == "q":
        print("bye\n")
        break

    elif inp in country_codes:
        print(f"The code for {inp} is {country_codes[inp]}")
    else:
        print(f"country details of {inp} not avalible")