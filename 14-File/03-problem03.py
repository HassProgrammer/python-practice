# WAF that replaces all occurrences of "Java" with "python" in the above file.
with open("14-File/problem3.txt", "r") as p:
    data = p.read()

data.replace("Java", "Python")