# Create and print a dictionary
data = {
    "name": "Md Ahshanul Alam Khan",
    "contact": "01889365698",
    "Age": "ever green",
    "address": "khulna"
}
print(data)

# Print the "name" value of the dictionary
print(data["name"])

# Duplicate values will overwrite existing values
data2 = {
    "name": "Md Ahshanul Alam Khan",
    "name": "pranto",
    "contact": "01889365698",
    "Age": "ever green",
    "address": "khulna"
}
print(data2)

# Print the number of items in the dictionary
print(len(data))

# The values in dictionary items can be of any data type
info = {
    "name": "Md Ahshanul Alam Khan",
    "Muslim": True,
    "contact": 1889365698,
    "Age": "ever green",
    "address": "khulna"
}
print(info)

# Print the data type of a dictionary

print(type(info))
