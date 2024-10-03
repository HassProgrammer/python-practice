# Q2. Write a program to calculate the electricity bill (accept number of unit from user) according to
# the following criteria :
# First 100 units
# no charge
# Next 100 units
# Rs 5 per unit
# After 200 units
# Rs 10 per unit
# (For example if input unit is 350 than total bill amount is Rs2000)

number_of_unit = int(input("Enter the number of unit:\t"))
if number_of_unit <= 100:
    charge = 0
elif number_of_unit > 100 and number_of_unit <= 200:
    charge = (number_of_unit-200)*5
elif number_of_unit > 200:
    charge = 500 + (number_of_unit - 200)*10
print(f"Amount to pay: Tk.{charge})")