# Get the value of the "age" key:
info = {
    "name": "Md Ahshanul Alam Khan",
    "muslim": True,
    "contact": 1889365698,
    "age": "ever green",
    "address": "khulna"
}
get = info["age"]
print(get)

# Get a list of the keys
get = info.keys()
print(get)

# Add a new item to the original dictionary, and see that the keys list gets updated as well
info2 = {
    "name": "Md Ahshanul Alam Khan",
    "muslim": True,
    "contact": 1889365698,
    "age": "ever green",
    "address": "khulna"
}
k  = info2.keys()
print(k)

info2["home town"] = "khulna"
print(k)
print(info2)

# Get a list of the values
v = info2.values()
print(v)

# Get a list of the key:value pairs
pairs = info2.items()
print(pairs)

# Check if "model" is present in the dictionary:
if "home town" in info2:
    print(info2["name"])

