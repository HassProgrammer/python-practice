# Q1. Write a program to display "Hello" if a number entered by user is a multiple of five,
# otherwise print "Bye".
number = int(input("Enter a number:\t"))
if number % 5 == 0:
    result = "Hello"
else:
    result = "By"
print(result)