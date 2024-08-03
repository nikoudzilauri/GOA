num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
operation = input("Enter the operation (+, -, *, /): ")


if operation == '+':
    result = num1 + num2 + num3
elif operation == '-':
    result = num1 - num2 - num3
elif operation == '*':
    result = num1 * num2 * num3
elif operation == '/':
    if num2 != 0 and num3 != 0:
        result = num1 / num2 / num3
    else:
        result = "Division by zero error"
else:
    result = "Invalid operation"


print("The result is:", result)
