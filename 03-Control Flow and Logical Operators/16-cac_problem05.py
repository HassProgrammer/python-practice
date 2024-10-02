# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book,
# Snowy - Build a snowman).

weather_mood = input("Enter the weather mood of your area:\t").lower()

if weather_mood == "sunny":
    what_you_can_do = "Go for a walk"
elif weather_mood == "rainy":
    what_you_can_do = "Read a book"
elif weather_mood == "snowy":
    what_you_can_do = "Build a snowman"
else:
    what_you_can_do = "go to planet neptune"

print(f"You can {what_you_can_do}")

