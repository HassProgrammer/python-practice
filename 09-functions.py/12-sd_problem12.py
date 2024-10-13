# WAF to print the elements of a list in a single line. ( list is the parameter)
heros = ["thor", "iron man", "captain america", "shakti man"]

def print_list(list):
    for item in list:
        print(item, end=" ")
print_list(heros)