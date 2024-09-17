# year = int(input("Enter a year:\t"))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#               print("Leapyear.")
#         else:
#             print("Not leapyear.")
#     else:
#         print("Not leapyear.")
# else:
#     print("Not leapyear.")   
# 
# year = int(input("Enter a year:\t"))
year = int(input("Enter a year:\t"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not a leap year.")
    else:
        print("Leap year.")
else:
    print("Not a leap year.")         