# 7. Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of
# espresso.

coffeeSize = input("Enter Coffee size(S, M or L):\t").lower()
extra = input("Do you want Extra shot of espresso? (Y/N):\t").lower()

if coffeeSize == "s":
    if extra == "y":  
        coffee = "Take Your Small Coffee With Extra shot of Espresso"
    else:
        coffee = "Take Your Small Coffee"
elif coffeeSize == "m":
    if extra == "y":
        coffee = "Take Your Medium Coffee With Extra shot of Espresso"
    else:
        coffee = "Take Your Medium Coffee"
elif coffeeSize == "l":
    if extra == "y":
        coffee = "Take Your Large Coffee With Extra shot of Espresso"
    else:
        coffee = "Take Your Large Coffee"
else:
    coffee = "Not Found!"

print(coffee)
