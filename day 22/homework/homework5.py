global_var = "I am a global variable"

# Function that uses a local variable
def local_variable_demo():
    local_var = "I am a local variable"
    print("Inside the function:")
    print("Global variable:", global_var)
    print("Local variable:", local_var)

# Call the function
local_variable_demo()

# Accessing global variable outside the function
print("\nOutside the function:")
print("Global variable:", global_var)

# Trying to access local variable outside the function (will result in an error)
# print("Local variable outside the function:", local_var)
