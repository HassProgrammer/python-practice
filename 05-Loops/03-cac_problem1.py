# 1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.
# numbers = [111, -2, 3, 4, 5, 6, -7, -8, 9, 101]
numbers = [111, -2, 3, 4, 5, 6, -7, -8, 9, 101]
positive_number_count = 0
for num in numbers:
    if num > 0:
        positive_number_count += 1
print(f"The final count of positive number is: {positive_number_count}") 