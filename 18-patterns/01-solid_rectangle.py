# Ques: Print the given pattern
# *****
# *****
# *****
rows = int(input("Enter the number of row you want:\t"))
columns = int(input("Enter the number of columns you want:\t"))

for i in range(1,columns+1):
    for j in range(1, rows+1):
        print("*", end=" ")
    print("")
    