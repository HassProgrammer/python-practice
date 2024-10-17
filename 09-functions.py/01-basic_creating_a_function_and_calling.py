# Creating and calling a Function
def ahshan():
    print("Assalamualaikum everyone")
print(ahshan())

# Arguments
def go(do):
    print(f"{do} happy")

go("i'm")
go("you'r")
go("be")

# Arbitrary Arguments, *args
def tea(*args):
    print(f"Plz, i want a cup of {args[2]}")
tea("Black Tea", "Coffee", "Oolong Tea", "Lemon Tea")

# Keyword Arguments
def tea(option1, option2, option3, option4):
    print(f"Plz, i want a cup of {option4}")
tea(option1 = "Black Tea", option2 = "Coffee", option3 = "Oolong Tea", option4 = "Lemon Tea")

# Arbitrary Keyword Arguments, **kwargs
def tea(**kwargs):
    print(f"Plz, i want a cup of {kwargs["option1"]}")
tea(option1 = "Black Tea", option2 = "Coffee", option3 = "Oolong Tea", option4 = "Lemon Tea")

# Default Parameter Value
def password(open= 123):
    if open == 566 or open == 123:
        print("Open")
    else:
        print("Close")
password()

# Passing a List as an Argument
def starving(food):
   for open_mouth in food:
       print(f"Eating {open_mouth}")

item = ["coffee", "fruits", "rice the Bhat"]
starving(item)

# Return Values
def math(x):
    return 5+x
print(math(2))

# Positional-Only Arguments
def my_function(x, /):
  print(x)

my_function(3)

