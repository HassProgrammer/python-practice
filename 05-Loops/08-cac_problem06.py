# 6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.
number = int(input("Enter a number:\t"))
factorial = int(input("Factorial:\t"))

while number > 0:
    factorial *= number
    number -= 1
print(f"Factorial: {factorial}")