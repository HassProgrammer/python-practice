username = "admin"

def func():
    username = "root"
    print(username)

print(username)
func()

x = 99
def add(y):
    z = x+y
    return z
print(add(1))

#Global keyword
u = 99
def func2():
    global u
    u = 55
func2()
print(u)


def f1():
    # x = 92
    def f2():
        print (x)
    f2()
f1()
