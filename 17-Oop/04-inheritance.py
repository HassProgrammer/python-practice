print("Calling without inheritance")
class Phone:
    def call(self):
        print("you can call")
    def message(self):
        print("You can message")

class Samsung:
    def call(self):
        print("you can call")
    def message(self):
        print("You can message")
    def photo(self):
        print("You can take photo")

system = Phone()
system.call()
system.message()   

print("\n--------------------------------")
print("\nCalling with inheritance")


class Phone:
    def call(self):
        print("you can call")
    def message(self):
        print("You can message")

class Samsung(Phone):
    # def call(self):
    #     print("you can call")
    # def message(self):
    #     print("You can message")
    def photo(self):
        print("Taking photo")

samsung_call = Samsung()

samsung_call.call()
samsung_call.message()
samsung_call.photo()
