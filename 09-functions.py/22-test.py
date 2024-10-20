import random

#invoke a function with user input
name = input("Enter your name:\t")
def salam(salam_to):
    print(f"Assalamu Alaikum {salam_to}")

salam(name)

#Function using random
num = 10
def robot(name):
    for number in range(1, 10):
        random_choice = random.choice(range(1, num + 1))
        print(f"Number: {name}, Random Choice: {random_choice}")

robot(name = input("Enter your name:\t"))

#Function using random with iteration value  
def robot(name):
    for number in range(1, 10):
        random_choice = random.choice(range(1, number + 1))
        print(f"Number: {name}, Random Choice: {random_choice}")

robot(name = input("Enter your name:\t"))

#Function using multiple argument
def display_invoice(user_name, amount, due_date):
    print(f"Hello {user_name}!\nyour bill of Tk.{amount:.2f} is due: {due_date}")
display_invoice("Khan", 42.33, "01/10")


# return
def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return f"{first} {last}"
full_name = create_name("ahshanul", "khan")
print(full_name)