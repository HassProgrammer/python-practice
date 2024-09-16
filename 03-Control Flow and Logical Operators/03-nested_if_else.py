height = int(input("Enter your height cm:\t"))
if height >= 120:
    print("You can ride.")
    age = int(input("Enter your age:\t"))
    if age >= 18:
        print("Pay $12")
    if age < 18:
        print("Pay $7")
else:
    print("Eat and growup.")
    