info = {
    "name": "Md Ahshanul Alam Khan",
    "muslim": True,
    "contact": 1889365698,
    "age": "ever green",
    "address": "khulna"
}
# The pop() method removes the item with the specified key name
info.pop("age")
print(info)

# The popitem() method removes the last inserted item 
info.popitem()
print(info)

# The del keyword removes the item with the specified key name:
del info["contact"]
print(info)

# The del keyword can also delete the dictionary completely
# hi = {
#     "name": "Md Ahshanul Alam Khan",
#     "muslim": True,
#     "contact": 1889365698,
#     "age": "ever green",
#     "address": "khulna"
# }
# del hi
# print(hi)