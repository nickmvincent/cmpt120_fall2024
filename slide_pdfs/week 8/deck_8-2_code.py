def function_name(parameters):
    # code block
    return True

def greet(name):
    return f"Hello, {name}!"

def foo1(a,b):
  return a+b

def foo2(n):
  return n % 2 == 0

def foo3(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

def add_two_nums(a,b):
  return a+b

def is_even(n):
  return n % 2 == 0

def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

i = 0
while i < 5:
    print(i)
    i += 1

while not user_input:
    user_input = input("Enter something: ")

for i in range(5):
    if i == 2:
        continue
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

inputs = ["hello", "", "world", "", "python"]
for item in inputs:
    if item == "":
        continue
    print(item)

for i in range(10):
    if i == 5:
        break
    print(i)

while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    if user_input == 'q':
        break
    print(f"You entered: {user_input}")

numbers = [3, 5, 7, 8, 10, 12]
for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break

def binary_to_decimal(binary_str):
    """Convert a binary string to a decimal number."""
    decimal = 0
    for digit in binary_str:
        decimal = decimal * 2 + int(digit)
    return decimal

def decimal_to_ascii(decimal):
    """Convert a decimal number to its ASCII character."""
    return chr(decimal)

def process_binary_input():
    """Process binary input and handle conversion to decimal and ASCII."""
    while True:
        binary_input = input("Enter an 8-bit binary number (or 'exit' to quit): ")
        
        if binary_input.lower() == 'exit':
            print("Exiting...")
            break
        
        # Ensure input is 8 bits and binary
        if len(binary_input) != 8 or not all(bit in '01' for bit in binary_input):
            print("Invalid input! Please enter an 8-bit binary number.")
            continue

        # Convert binary to decimal
        decimal_value = binary_to_decimal(binary_input)
        
        # Convert decimal to ASCII
        ascii_char = decimal_to_ascii(decimal_value)
        
        print(f"Binary: {binary_input} -> Decimal: {decimal_value} -> ASCII: {ascii_char}")

# Call the function to start the loop
process_binary_input()

# Get ASCII code from character
print(ord('A'))  # Output: 65
print(ord('!'))  # Output: 33

# Get character from ASCII code
print(chr(65))   # Output: A
print(chr(33))   # Output: !

# String of ASCII characters
print(''.join(chr(i) for i in range(65, 91)))  # A-Z

def binary_to_decimal(binary_str):
    """Convert a binary string to a decimal number."""
    decimal = 0
    for digit in binary_str:
        decimal = decimal * 2 + int(digit)
    return decimal

binary_to_decimal("01001000")
chr(72)

dec = ["65", "66", "67"]
chars = ["A", "B", "C"]
characters_as_dec = ["65", "65", "65", "67", "67", "67"]
for i in range(len(characters_as_dec)):
    for j in range(len(dec)):
        if characters_as_dec[i] == dec[j]:
            print(chars[j])

