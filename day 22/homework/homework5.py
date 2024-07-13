global_var = "I am a global variable"

# Function that uses a local variable
def local_variable_demo():
    local_var = "I am a local variable"
    print("Inside the function:")
    print("Global variable:", global_var)
    print("Local variable:", local_var)

# Call the function
local_variable_demo()


print("\nOutside the function:")
print("Global variable:", global_var)

