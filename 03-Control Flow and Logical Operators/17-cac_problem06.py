# 6. Transportation Mode Selection
# Problem: Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15
# km: Car).
km = int(input("Enter The Distance:\t"))
if km < 3:
    go = "Walk"
elif km < 15:
    go = "Bike"
elif km >= 15:
    go = "Car"
else:
    go = "Catch Rocket"
print(f"AI recommends you the transport of: {go}")