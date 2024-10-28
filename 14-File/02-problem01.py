# Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File 1/0
# using Python.
# I like programming in Python.

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/0\nusing Python.\n")
    f.write("I like programming in Python.")