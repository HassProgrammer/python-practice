class A:
    varA = "Welcome to class A"
class B:
    varB = "Welcome to class B"
class C(A,B):
    varC = "Welcome To class C"

c = C()
print(c.varC)
print(c.varB)
print(c.varA)