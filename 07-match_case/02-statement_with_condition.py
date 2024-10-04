inp = int(input("Enter The Value of x:\t"))
match inp:
    case 0:
        print("inp is zero")
    case 1:
        print("inp is one")
    case _ if inp!= 90:
        print(f"{inp} is not 90")
    case _ if inp != 80:
        print(f"{inp} is not 80")
    case _:
        print(inp)