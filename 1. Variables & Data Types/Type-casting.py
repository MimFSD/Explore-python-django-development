# Implicit Type Conversion
a = 5          # Integer
b = 2.0        # Float
c = a + b      # Implicitly converts integer to float
print(c)       # Output: 7.0

# Explicit Type Conversion
# Convert float to integer
num_float = 7.9
num_int = int(num_float)  # Converts float to integer
print(num_int)  # Output: 7

# Convert integer to string
num_str = str(num_int)  # Converts integer to string
print(num_str)  # Output: "7"

# Convert string to boolean
str_val = "Hello"
bool_val = bool(str_val)  # Converts non-empty string to True
print(bool_val)  # Output: True

# Convert string to list
str_val = "hello"
list_val = list(str_val)  # Converts string to list of characters
print(list_val)  # Output: ['h', 'e', 'l', 'l', 'o']
