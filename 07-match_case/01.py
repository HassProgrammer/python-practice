inp = int(input("Enter The Value of x:\t"))
match inp:
    case 0:
        print("inp is zero")
    case 1:
        print("inp is one")
    case _:
        print(inp)