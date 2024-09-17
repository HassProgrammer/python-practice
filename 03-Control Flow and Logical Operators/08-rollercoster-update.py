height = int(input("Enter your height cm:\t"))
bill = 0
if height >= 120:
    print("You can ride.")
    age = int(input("Enter your age:\t"))
    if age <= 12:
        bill = 5
        print("Pay 5$")
    elif age <= 18:
        bill = 7
        print("Pay 7$")
    else:
        bill = 12
        print("Pay 12$")

    wants_photo = input("Do you want to photo taken? y or n:\t")
    if wants_photo == "y":
        #Add $3 to their bill
        bill = bill + 3
    
    print(f"Your final bill is ${bill}.")

else:
    print("Eat and growup.")
    