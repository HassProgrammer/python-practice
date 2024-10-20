# *****
# ****
# ***
# **
# *
n = int(input("How many stars do you want:\t"))
for i in range(n):
    for j in range(i,n):
        print('*', end="")
    print()