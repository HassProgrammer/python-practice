import re
number = input("Enter Your Phone Number:\t")
model = re.compile(r"(\d\d\d)(\d\d\d\d\d\d\d\d)")
mo = model.search(number)
if mo.group(1) == "017":
    print(f"Gramin Phone Number: {mo.group(0)}")
elif mo.group(1) == "019":
    print(f"Banglalink Number: {mo.group(0)}")
elif mo.group(1) == "015":
    print(f"Telitalk Number: {mo.group(0)}")
elif mo.group(1) == "018":
    print(f"Robi Number: {mo.group(0)}")
elif mo.group(1) == "011":
    print(f"Citycell Number: {mo.group(0)}")
elif mo.group(1) == "016":
    print(f"Airtel Number: {mo.group(0)}")
else:
    print("International Number / Unknown.")