def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Example usage:
print(factorial(5))  # Output: 120

def recursive_sum(n):
    if n == 0:  # Base case
        return 0
    else:
        return n + recursive_sum(n - 1)  # Recursive case

# Example usage:
print(recursive_sum(5))  # Output: 15

def recursive_sum_list(numbers):
    if not numbers:  # Base case
        return 0
    else:
        return numbers[0] + recursive_sum_list(numbers[1:])  # Recursive case

# Example usage:
print(recursive_sum_list([1, 2, 3, 4]))  # Output: 10

def recursive_reverse(s):
    if len(s) <= 1:  # Base case
        return s
    else:
        return s[-1] + recursive_reverse(s[:-1])  # Recursive case

# Example usage:
print(recursive_reverse("hello"))  # Output: "olleh"

def is_palindrome(s):
    if len(s) <= 1:  # Base case
        return True
    elif s[0] == s[-1]:  # Recursive case
        return is_palindrome(s[1:-1])
    else:
        return False

# Example usage:
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False

def nested_sum(data):
    total = 0
    for item in data:
        if isinstance(item, int):  # Base case
            total += item
        elif isinstance(item, list):  # Recursive case
            total += nested_sum(item)
    return total

# Example usage:
print(nested_sum([1, 2, [3, 4], 5]))          # Output: 15
print(nested_sum([[1, 2, [3]], 4, [5, [6]]])) # Output: 21
print(nested_sum([1, [2, [3, [4, [5]]]]]))    # Output: 15

def count_vowels(s):
    vowels = "aeiouAEIOU"
    if not s:  # Base case: empty string
        return 0
    elif s[0] in vowels:  # Check if first character is a vowel
        return 1 + count_vowels(s[1:])
    else:
        return count_vowels(s[1:])  # Recursive case: continue with next character

# Example usage:
print(count_vowels("hello"))            # Output: 2
print(count_vowels("Recursion is fun!"))  # Output: 6
print(count_vowels("xyz"))              # Output: 0

