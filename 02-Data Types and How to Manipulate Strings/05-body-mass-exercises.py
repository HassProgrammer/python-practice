height = float(input("Enter Your Height:\t"))
weight = int(input("Enter Your Weight:\t"))
bmi = weight / (height * height)
bmi_as_int = int(bmi)
bmi_as_str = str(bmi_as_int)
print("Your BMI calculation is: "+bmi_as_str)