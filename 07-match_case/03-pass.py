pass_change = True
new_pass = input("* Enter new password:\t")
re_pass = input("* Rewrite new password:\t")

match pass_change == True:
    case _ if new_pass == re_pass:
        print(f"- Your new password is {re_pass}")
        exit()  
    case _ :
        print("Try again")
         
new_pass = input("* Enter new password:\t")
re_pass = input("* Rewrite new password:\t")
match pass_change:
    case _ if new_pass == re_pass:
        print(f"- Your new password is {re_pass}")
    case _ :
        print("- Time is up!, party is over\n Hasta la Vista Baby!")
        exit()

    