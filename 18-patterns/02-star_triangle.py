# * Ques : Print the given pattern
# *
# **
# ***
# ****
# - Star Triangle
value = int(input("Enter the value:\t"))
for i in range(1, value +1):
    for j in range(1,i+1):
        print("* ", end="")
    print("")