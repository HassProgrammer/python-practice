# Ques : Print the given pattern
# A B C D
# A B C D
# A B C D
# A B C D
number = int(input("Enter a number:\t"))
for i in range(1, number):
    a= 1;
    print("")
    for j in range(1, number):
        d = a+64
        char = chr(d)
        print(char , end=" ")
        a = a+1
