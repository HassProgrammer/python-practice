def calculate_BMI(run):
    while run == "Start".lower():
        print("*- Welcome to BMI test.\n")
        height = float(input("Enter your height:\t"))
        weight = int(input("Enter your weight:\t"))
        bmi = weight / (height * height)

        if bmi < 18.5:
            print(f"Your BMI is {bmi}, you are underweight.")
        elif bmi < 25:
            print(f"Your BMI is {bmi}, you are normal weight.")
        elif bmi < 30:
            print(f"Your BMI is {bmi}, you are slightly overweight.")
        elif bmi < 35:
            print(f"Your BMI is {bmi}, you are obes.")
        else:
            print(f"Your BMI is {bmi}, you are clinically obes.")  

        exit_or_not =  input("do you want to exit:: ").lower()
        for d in exit_or_not:
            if d == 'y' or 'n':
                if exit_or_not == 'y':
                    print("Thank you for choosing us!!")
                    exit()
                elif exit_or_not == 'n':
                        calculate_BMI(run)
                        
            else:
                print("You have to choose between Y/N")
                    


        
 