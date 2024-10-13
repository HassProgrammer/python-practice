number = int(input("Enter a number:\t"))
def odd_even(number):
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")
odd_even(number)