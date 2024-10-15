# Loop through the set, and print the values
what_a_set_bro = {"apple", "banana", "cherry", "abc", 34, True, 40, "male", 0}
for item in what_a_set_bro:
    print(item, end=", ")

print("\n-------------------\n")

# Check if "banana" is present in the set
what_a_set_bro2 = {"apple", "banana", "cherry", "abc", 34, True, 40, "male", 0}
print("banana" in what_a_set_bro2)

# Check if 0 is NOT present in the set
what_a_set_bro2 = {"apple", "banana", "cherry", "abc", 34, True, 40, "male", 0}
print(0 not in what_a_set_bro2)
