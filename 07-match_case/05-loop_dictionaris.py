info = {
    "name": "Md Ahshanul Alam Khan",
    "muslim": True,
    "contact": 1889365698,
    "age": "ever green",
    "address": "khulna"
}

# Print all key names in the dictionary, one by one
if "name" in info:
    print(info)
    
for x in info:
    print(info[x])

# You can also use the values() method to return values of a dictionary
for x in info.values():
    print(x)

# You can use the keys() method to return the keys of a dictionary
for x in info.keys():
    print(x)

# Loop through both keys and values, by using the items() method
for x, y in info.items():
    print(x, y)