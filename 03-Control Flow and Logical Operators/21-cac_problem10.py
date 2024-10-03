# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years -
# Puppy food, Cat: >5 years - Senior cat food).
animal_type = input("Enter your animal type:\t").lower()
animal_age = int(input("Enter your animal age:\t"))

if (animal_type == "dog") and (animal_age < 2):
    food = "Puppy food"
elif (animal_type == "cat") and (animal_age > 5):
    food = "Senior cat food"
else:
    food = "I thing you just came out from a bar!"

print(f"The Result is: {food}")
