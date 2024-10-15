this_set = {"apple", "banana", "cherry"}
print(this_set)
print(type(this_set))

# Sets cannot have two items with the same value.
this_set = {"apple", "banana", "cherry", "Bangladesh", "Bangladesh", "bangladesh"}
print(this_set)

# True and 1 is considered the same value
this_set = {"apple", "banana", "cherry", True, 1, 2}
print(this_set)

# False and 0 is considered the same value

this_set = {"apple", "banana", "cherry", False, True, 0}
print(this_set)

# Get the number of items in a set or get the length 
this_set = {"apple", "banana", "cherry", False, True, 0}
print(len(this_set))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {0.1, 5.5, .007}
set4 = {True, False, False}

# Set items can be of any data type
for set in set1:
    print(type(set))

for set in set2:
    print(type(set))

for set in set3:
    print(type(set))

for set in set4:
    print(type(set))

# A set with strings, integers and boolean values
set1 = {"abc", 34, True, 40, "male"}
# # if set1 == set1[0]:
# #     print(type(set1))
# for item in set1:
#     if item == set1[0]:
#         print(type(item))  
print(set1)

# Using the set() constructor to make a set
# what_a_set = set(("apple", "banana", "cherry", False, True, 0)) 
# print(type(what_a_set))