print("Welcome to the bank 💰")
print("*******************************")

def show_balance(balance):
    print(f"\nYour balance is tk.{balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited:\t"))
    if amount < 0:
        print("\nHey! Poor people, that's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn:\t"))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0.")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("_______Our Services__________")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(input("What you would like to do?\nEnter your choice (1-4):->\t"))

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance += deposit()  
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            print("Exiting the program. Thank you, have a nice day!")
            is_running = False  
        else:
            print('That is not a valid choice!')
print("\nThank you have a nice day")
if __name__ == '__main__':
    main()
