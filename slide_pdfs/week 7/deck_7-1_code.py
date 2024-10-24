values = [3, 5, 2, 8, 6]
maximum = values[0]
for value in values:
    if value > maximum:
        maximum = value
print(maximum)  # 8

values = [3, 5, 2, 8, 6]
maximum = values[0]
index_of_max = 0
for i in range(len(values)):
    value = values[i]
    if value > maximum:
        maximum = value
        index_of_max = i
print(maximum, i)

max([1,2,3])

def max_number_for_bits(n_bits):
    return 2**n_bits - 1

# Example usage:
n_bits = 4
print(f"The maximum number that can be stored with {n_bits} bits is {max_number_for_bits(n_bits)}")

binary_str = "1101"
decimal = 0
length = len(binary_str)

for i in range(length):
    bit = binary_str[i]
    if bit == '1':
        decimal += 2 ** (length - i - 1)

print(f"The decimal representation of binary {binary_str} is {decimal}")


def binary_to_decimal(binary_str):
    return int(binary_str, 2)

# Example usage:
binary_str = "1101"
print(f"The decimal representation of binary {binary_str} is {binary_to_decimal(binary_str)}")

print("Lets find the most popular coffee shop")

survey_responses = [
    "tims", "sbux", "ren", "tims", "sbux", "blenz",
    "blenz", "ren", "blenz"
]
options = ["tims", "sbux", "ren", "blenz"]

list_of_counting_vars = len(options) * [0]

for response in survey_responses:
    for i in range(len(options)):
        if options[i] == response:
            list_of_counting_vars[i] += 1

for i in range(len(options)):
    print(options[i], list_of_counting_vars[i])

dec = ["65", "66", "67"]
chars = ["A", "B", "C"]

characters_as_dec = ["65", "65", "65", "67", "67", "67"]

for i in range(len(characters_as_dec)):
    for j in range(len(dec)):
        if characters_as_dec[i] == dec[j]:
            print(chars[j])

