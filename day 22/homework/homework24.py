def gcd(a, b):
    value = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            value = i
    return value

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

result = gcd(num1, num2)

print(f"The greatest common divisor of {num1} and {num2} is: {result}")
