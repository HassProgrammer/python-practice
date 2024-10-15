# Add an item to a set, using the add() method
what_a_set_bro = {"apple", "banana", "cherry", "abc", 34, True, 40, "male", 0}
what_a_set_bro.add("cat")
print(what_a_set_bro)

# To add items from another set into the current set, using the update() method
what_a_set_bro = {"apple", "banana", "cherry", "abc", 34, True, 40, "male", 0}
what_a_set_bro2 = {"Orange cat"}
cat_food = {"cat food", "Water"}
what_a_set_bro2.update(what_a_set_bro)
print(what_a_set_bro2)
print(what_a_set_bro)

if "Orange cat" in what_a_set_bro2:
    print("adding plz wait........")
    what_a_set_bro2.update(cat_food)
    print(what_a_set_bro2)
else:
    print("303 not found")
    
# Add elements of a list to at set
master_set = {"apple", "banana", "cherry", 34, True, 40}
my_list = ["orange", "male", 0]
master_set.update(my_list)
print(master_set)