info = {
    "name": "Md Ahshanul Alam Khan",
    "muslim": True,
    "contact": 1889365698,
    "age": "ever green",
    "address": "khulna"
}
# Change the "name" to 2018:
info["name"] = "Md Ahshanul Alam Khan (pranto)"
print(info)

# Update the "age" by using the update() method
if "age" in info:
    change = info.update({"current age":"ever green ++"})
print(info)

