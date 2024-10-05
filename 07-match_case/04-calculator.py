num1 = int(input("Enter First Number:\t"))
operator = input("+, -, *, /, % :\t")
num2 = float(input("Enter Second Number:\t"))

match operator:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2
    case "%":
        result = num1 % num2

print(f"The result is {result}")