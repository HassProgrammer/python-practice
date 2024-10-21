# Write a Python function called multiply to multiply all of the numbers in a list together and return that value. The function should be created in such a way
# that it will work for both lists, tuples, and sets.

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply([1,2,3,4,5,6,7,8,9]))