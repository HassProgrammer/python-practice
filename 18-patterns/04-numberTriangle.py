# Ques : Print the given pattern
# 1
# 12
# 123
# 1234

number = int(input("Enter a number:\t"))

for i in range(1, number+1):
    print("")
    for j in range(1, i+1):
        print(j, end="")
    