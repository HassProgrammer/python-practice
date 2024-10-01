# • 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone

age = int(input("Enter your age:\t"))
day = input("What day is it?:\t").lower()

price = 12 if age >= 18 else 8
if day == "wednesday":
    price -= 2

print(f"The ticket price for you is ${price}.")
