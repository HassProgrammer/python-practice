import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?:\t")) 
nr_symbols = int(input(f"How many symbols would you like?:\t"))
nr_numbers = int(input(f"How many numbers would you like?:\t"))

easy_or_hard = input("For easy pass press (E) For hard pass press (H):\t").lower()


if easy_or_hard == "e":
    # easy pass
    password = ""
    for char in range(1, nr_letters + 1):
        random_char = random.choice(letters)
        password = password + random_char

    for char in range(1, nr_symbols + 1):
        random_char = random.choice(symbols)
        password = password + random_char

    for char in range(1, nr_numbers + 1):
        random_char = random.choice(numbers)
        password = password + random_char

    print(f"Your password is: {password}")
if easy_or_hard == "h":
    # Hard password
    password_list = []
    for char in range(1, nr_letters + 1):
        
        password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
        password_list.append(random.choice(symbols))

    for char in range(1, nr_numbers + 1):
        password_list.append(random.choice(numbers))
        

    # print(f"Your password is: {password_list}")
    random.shuffle(password_list)
    # print(password_list)

    password = ""
    for char in password_list:
        password  = password + char
    print(f"Your password is: {password}")
else:
    print("Invalid Keyword You must have to press (E) for easy password\nor (H) for hard password\nYou can type (E) or (H) one any case, they are not Case sensitivity.\t\nTry again! ")






