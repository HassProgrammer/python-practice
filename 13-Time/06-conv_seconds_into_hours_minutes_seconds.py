import math as m
seconds = int(input("Enter Seconds:->\t"))

hours = m.floor(seconds/3600)
# print(hours)
# #120000
hours1 = seconds%3600
minute = m.floor(hours1/60)

rem_seconds = hours1%60 

print(f"{hours} Hours : {minute} Minutes : {rem_seconds} Seconds") 