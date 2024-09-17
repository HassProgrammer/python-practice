print('😄 Thank you for choosing "🐍 Python Pizza" deliveries.\n')
bill = 0
size  = input("What size pizza do you want?-> s, m or l:\t")
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
     bill += 25
else:
    print("Invalid size.")
   
add_pepperoni = input("Do you want pepperony?-> y or n:\t")
if add_pepperoni == "y":
    if size == "s":
        bill += 2
    elif size == "m":
        bill += 3
    elif size == "l":
        bill += 4
    else:
        print("invalid command.")

extra_cheese = input("Do you want extra cheese?-> y or n:\t")
if extra_cheese == "y":
    if size == "s":
        bill += 3
    elif size == "m":
        bill += 6
    elif size == "l":
        bill += 9
    else:
        print("invalid command.")

print(f"Your final bill is ${bill}")
print("😄Thank you for choosing Python Pizza🐍")



        
        