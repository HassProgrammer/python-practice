# Ques : Print the given pattern
# 1234
# 1234
# 1234
# 1234

row = int(input("Enter the num of row:\t"))
column = int(input("Enter the num of column:\t"))

for i in range(1, row+1):
    print(" ")
    for j in range(1, column+1):
        print(j, end=" ")
        