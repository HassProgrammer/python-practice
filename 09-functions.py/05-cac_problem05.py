# 5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.
def user(name = "User"):
    return "Hi " + name + "!"
print(user())
print(user("Khan"))