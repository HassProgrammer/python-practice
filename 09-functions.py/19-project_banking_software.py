print("Welcome to the bank 💰")
print("*******************************")

def show_balance():
    print(f"\nYour balance is tk.{balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited:\t"))

    if amount < 0:
        print("\nHey! poor people, That's not a valid amount")
        return 0
    else:
        return amount


def withdraw():
    pass

balance = 0
is_running = True

while is_running == True:
    print("_______Our Services__________")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("What you would like to do?\nEnter your choice (1-4):->\t"))

    if choice == 1:
        show_balance()
    elif choice == 2:
       balance = balance + deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        # print("You selected Option 4.")
        is_running == False
    else:
        print('That is not a valid choice!')
print("Thank you have a nice day")