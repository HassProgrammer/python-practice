target = int(input("Enter a number:\t"))
sum = 0
for num in range(1,target + 1):
    # print(num)
    if num % 2 == 0:
        sum = sum + num
print(sum)