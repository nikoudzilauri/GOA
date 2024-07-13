def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return "Error: Input string is not a valid number"

number_str = input("Enter a number as a string: ")
result = string_to_int(number_str)
print(result)
