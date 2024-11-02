import random as go

def headOrTail():
    user = input("Press y for flip or n for exit:\t").lower()
    if user == "n":
        print("\n..............🪙................\n")
        print("🤝 Thank you for being with us!")
        exit() 
    elif user == "y":
        flip = go.randint(0,1)
        if flip == 1:
            print("\n..............🪙................\n")
            print ("🪙 Heads")
        else:
            print("\n..............🪙................\n")
            print("🪙 Tails")
        headOrTail()

