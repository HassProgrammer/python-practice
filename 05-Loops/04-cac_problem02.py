# 2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter n number:\t"))
sum_even = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += 1

print(f"The sum of even numbers is: {sum_even} ")   