# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = input("Enter Fruit Name:\t").lower()
color = input("Enter Fruit Color:\t ").lower()

if fruit == "banana":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("Overripe")
    else:
        print("No info!")