# Write a Python function called max _of_three to find the maximum value between three numbers. Do not use the max ( ) function.


def max_of_two(a,b):
    if a>b:
        return a
    else:
        return b
def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b,c))
print(max_of_three(1, 6, 9))
