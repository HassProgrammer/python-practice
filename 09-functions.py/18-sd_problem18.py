# Write a recursive function to print all elements in a list.
# Hint: use list & index as parameters.
def print_list(list ,idx=0):
    if idx == len(list):
        return
    else:
        print(list[idx])
        print_list(list, idx+1)
fruits = ["mango", "litchi", "apple", "banana"]
print_list (fruits)