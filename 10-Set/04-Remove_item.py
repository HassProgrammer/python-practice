# Remove item by using the remove() method
what_a_set_bro = {"apple", "banana", "cherry", "abc", 34, True, 40, "male", 0}
what_a_set_bro.remove(34)
print(what_a_set_bro)

# Remove item by using the discard() method
what_a_set_bro.discard(0)
print(what_a_set_bro)

# Remove a random item by using the pop() method
what_is_going_on = what_a_set_bro.pop()
print(what_is_going_on)
print(what_a_set_bro)

# Using clear() method empties the set
nice_set = {"apple", "banana", "cherry"}
print(nice_set)
nice_set.clear()
print(nice_set)

#Using del keyword will delete the set completely
suicide_squad = {"apple", "banana", "cherry"}
print(suicide_squad)
if "apple" not in suicide_squad:
    print("Go find a poison")
else:
    del suicide_squad
    print("Batman")
