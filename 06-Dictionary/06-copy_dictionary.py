info = {
    "name": "Md Ahshanul Alam Khan",
    "muslim": True,
    "contact": 1889365698,
    "age": "ever green",
    "address": "khulna"
}
# Make a copy of a dictionary with the copy() method
my_dict = info.copy() 
print(my_dict)

# Make a copy of a dictionary without the copy() method
myDict = info
print(my_dict)

# Make a copy of a dictionary with the dict() function
mydict = dict(info)
print(mydict)