# The union() method returns a new set with all items from both sets
# Join set1 and set2 into a new se

what_a_set_bro = {"apple", "banana", "cherry", "abc", 34, True, 40, "male", 0}
suicide_squad = {5, 2, 3, 4}

mix = what_a_set_bro.union(suicide_squad)
print(mix)

#The | operator instead of the union() method, and you will get the same result.
# Use | to join two sets
newSet = what_a_set_bro | suicide_squad
print(newSet)

# Join a set with a tuple
suicide_squad2 = {5, 2, 3, 4}
joker = (1,6,9)
newOne = suicide_squad.union(joker)
print(newOne)

# Join set1 and set2, but keep only the duplicates
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

#Using & to join two sets
set0 = {"apple", "banana", "cherry"}
set02 = {"google", "microsoft", "apple"}
come_on_bro = set0 & set02 
print(come_on_bro)

# Keep the items that exist in both set1, and set2
set_1 = {"apple", "banana", "cherry"}
set_2 = {"google", "microsoft", "apple"}
set_1.intersection_update(set_2)
print(set_1)

# Keep all items from set1 that are not in set2
fruits = {"apple", "banana", "cherry"}
company = {"google", "microsoft", "apple"}
another = fruits.difference(company)
print(another)

# Use the difference_update() method to keep the items that are not present in both sets
fruits = {"apple", "banana", "cherry"}
company = {"google", "microsoft", "apple"}
fruits.difference_update(company)
print(fruits)