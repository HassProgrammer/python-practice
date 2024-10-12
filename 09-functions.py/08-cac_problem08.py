# 8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format
# key: value.

def print_normal(name, power):
    print(f"Name: {name}, Power: {power}")

print_normal(name="Hulk", power="Smash")
# print_normal(name="Hulk")

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(name="Hulk", power="Smash", enemy="Thanos")