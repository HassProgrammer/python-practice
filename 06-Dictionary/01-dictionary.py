chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

print(chai_types["Masala"])

print(chai_types.get("Ginger"))
chai_types["Green"] = "Fresh"
print(chai_types)

# Printing dictionary using for loop
for chai in chai_types:
    print(chai, chai_types[chai])

# Using two variable in one for loop
for key, value in chai_types.items():
    print(key, value) 


#find any type of chai
if "Masala" in chai_types:
    print("Yes Sir")

#find the length
print(len(chai_types))

# Add another item on list
chai_types["Earl Gray"] = "Citrus"
print(chai_types)

#Nested Dictionary
tea_shop = {
    "chai": {"Masala": "Spicy", "Ginger": "Zesty"},
    "Tea": {"Green": "Mild", "Black": "Strong"}
}
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Ginger"])

#Make a NEw Dictionary by using list
keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)