# 5. Find the First Non-Repeated Character
input_str = input("Enter Your word:\t")

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Find the First Non-Repeated Character is: ",char)
        break
