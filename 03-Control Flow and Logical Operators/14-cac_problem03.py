# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79),
# D (60-69), F (below 60).

marks = int(input("Enter your marks:\t"))

if marks >= 101:
    print("Please verify your marks again.")
    exit()

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"
print("Grade", grade)