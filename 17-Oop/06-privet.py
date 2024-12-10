class Account:
    def __init__(self, acc_id, acc_pass):
        self.acc_id = acc_id
        self.acc_pass = acc_pass
    

acc1 = Account("1234", "abcd120")
print(f"Account id: {acc1.acc_pass}\nAccount password: {acc1.acc_id}")

# Privet

class Account2:
    def __init__(self, acc_id, acc_pass):
        self.acc_id = acc_id
        self.__acc_pass = acc_pass
    def reset_pass(self):
        print(self.__acc_pass)
    

acc1 = Account2("1234", "abcd120")
print(acc1.reset_pass())
print(f"Account id: {acc1.acc_pass}\nAccount password: {acc1.__acc_id}")

class Person:
    __name = "anonymous"
    def __hello():
        print("Hello person")

p1 = Person()
print(p1.__hello)
        