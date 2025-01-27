# * Ques : Print the given pattern
# *
# **
# ***
# ****
# - Star Triangle reverse

value = int(input("Enter the value:\t"))

for i in range(1,value):
    print("")
    for j in range(1,value+1-i):
        print("* ",end="")