This file will contain some practice "write the code questions".


## Simple Code Writing on Paper

1. **Tricky Multiplication**
   - Write a Python program that takes two numbers as input and multiplies them, with a major catch: you cannot use the "*" character in your code.

2. **Conditionals**
   - Write a Python function `is_even(num)` that returns `True` if a number is even and `False` otherwise. Then use this function to write a function that counts the number of even in a list of numbers.

3. **Loops**
   - Write a Python program to print all the numbers from 1 to 100 that are divisible by 5.

4. **Recusrive String Manipulation**
   - Write a recursive Python function that takes a string as input and returns the string reversed.

5. **Lists**
   - Write a Python program that takes a two lists of numbers: a set of scores achieved by some players and a set of "valid" scores. We want to print the sum of all scores that appear in the valid scores list. Example: scores might be [50,75,99,101]. Valid scores might be list(range(50,100)).

7. **File Handling**
   - Write a Python program to read from a file named `input.txt` and count the number of lines in the file that contain a "$" character".


## "???" Code Completion Questions

### **1. Binary Search**
The following function performs binary search on a sorted list but has a missing line. Choose the correct code snippet to replace `???`:

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            ???  # Missing line
        else:
            high = mid - 1
    return -1
```

Options:
- a) `low = mid + 1`
- b) `low = target`
- c) `low = mid`
- d) `low = high`

<details><summary>Correct answer</summary>a</details>

---

### **2. File Handling for Data Analysis**
The following function processes a text file where each line contains a number. It calculates the average of the numbers but has a missing line. Choose the correct code snippet to replace `???`:

```python
def calculate_average(file_path):
    total, count = 0, 0
    with open(file_path, 'r') as file:
        for line in file:
            try:
                num = int(line.strip())
                total += num
                ???  # Missing line
            except ValueError:
                pass
    return total / count
```

Options:
- a) `count += 1`
- b) `count = total // num`
- c) `count += num`
- d) `count = 1`

<details><summary>Correct answer</summary>a</details>


Bonus: any robustness issues with this code?


---

### **3. Analyzing a List of Strings**
The following function identifies the longest string in a list but is missing a critical line. Choose the correct code snippet to replace `???`:

```python
def find_longest_string(strings):
    longest = ""
    for s in strings:
        if len(s) > len(longest):
            ???  # Missing line
    return longest
```

Options:
- a) `longest += s`
- b) `longest = s`
- c) `longest = len(s)`
- d) `longest = len([len(s)])`

<details><summary>Correct answer</summary>b</details>

---

### **4. Selection Sort (with 3-line replacement pattern)**
The following function implements selection sort but is missing lines to perform the swap. Choose the correct snippet to replace `???`:

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the current element with the smallest element
        ???
    return arr
```

Options:
- a) 
```python
temp = arr[j]
arr[j] = arr[min_index]
arr[min_index] = temp
```

- b) 
```python
temp = arr[min_index]
arr[min_index] = arr[j]
arr[j] = temp
```

- c) 
```python
temp = arr[min_index]
arr[min_index] = arr[n - 1]
arr[n - 1] = temp
```

- d) 
```python
temp = arr[i]
arr[i] = arr[min_index]
arr[min_index] = temp
```


<details><summary>Correct answer</summary>d</details>


---

### **5. Binary to Decimal Conversion (using very basic Python)**
The following function converts a binary string to a decimal number but is missing a critical line. Choose the correct snippet to replace `???`:

```python
def binary_to_decimal(binary_str):
    decimal = 0
    power = 0
    for i in range(len(binary_str) - 1, -1, -1):
        if binary_str[i] == '1':
            ???  # Missing line
        power += 1
    return decimal
```

Options:
- a) `decimal += 2 ** power`
- b) `decimal += 1 + power`
- c) `decimal += power * 2`
- d) `decimal += 2 ** i`

<details><summary>Correct answer</summary>a</details>


### **6. While Loop Example**
The following function uses a `while` loop to find the smallest power of 2 greater than or equal to a given number but has a missing line. Choose the correct snippet to replace `???`:

```python
def smallest_power_of_two(n):
    power = 1
    while power < n:
        ???  # Missing line
    return power
```

Options:
- a) `power *= 2`
- b) `power += 2`
- c) `power = power + power`
- d) `power = n // 2`

<details><summary>Correct answer</summary>a</details>

---

### 7. **Green Screen Pixel Replacement**

The following function replaces the green pixels in an image with pixels from a background image. It processes pixel-by-pixel using very basic Python (no modules) but has a missing line. Note that this function constructs a new array to return
in the function -- it does not modify the arguments. Choose the correct snippet to replace `???`:

```python
def replace_green_screen(foreground, background):
    result = []
    for i in range(len(foreground)):
        row = []
        for j in range(len(foreground[i])):
            pixel = foreground[i][j]
            if pixel[1] > 200 and pixel[0] < 100 and pixel[2] < 100:  # Check for green pixel
                ???  # Missing line
            else:
                row.append(pixel)
        result.append(row)
    return result
```

**Foreground and Background** are 2D lists of pixels (e.g., `pixel = (R, G, B)`), where each pixel is a list of three integers (red, green, blue) ranging from 0 to 255.

Options:
- a) `row.append(background[i][j])`
- b) `row.append(foreground[i][j])`
- c) `row.append((0, 0, 0))`
- d) `row.append((255, 0, 0))`

<details><summary>Correct answer</summary>a</details>



## Challenging code writing questions

### **1. Data Analysis**

Write a function average_above_threshold(lst, threshold) that takes a list of integers and a threshold value. It should calculate the average of all numbers in the list that are greater than the threshold. Return 0 if there are no such numbers. Do not use `max()`.

Example Input:

average_above_threshold([10, 20, 30, 40], 15)

Example Output:

30


### **2. Counting Substrings**
Write a function `count_substrings(s, substring)` that counts how many times a substring appears in a given string. You cannot use any built-in string functions like `count`.

**Example Input:**
```python
count_substrings("ababab", "ab")
```

**Example Output:**
```
3
```

<details>
<summary> Example answer</summary>
def count_substrings(s, substring):
    count = 0
    for i in range(len(s) - len(substring) + 1):
        if s[i:i + len(substring)] == substring:
            count += 1
    return count

# Example usage
print(count_substrings("ababab", "ab"))  # Output: 3

</details>

---

### **3. Random Number Guessing Game**
Write a function `guess_the_number()` that generates a random number between 1 and 100. The user must guess the number, and the program provides feedback ("too high", "too low") until the user guesses correctly.

**Example Interaction:**
```
Computer: Guess the number between 1 and 100!
User: 50
Computer: Too high.
User: 25
Computer: Too low.
User: 30
Computer: Correct!
```

<details>
<summary> Example answer</summary>

```python
import random

def guess_the_number():
    target = random.randint(1, 100)
    guess = 0
    while guess != target:
        guess = int(input("Enter your guess: "))
        if guess < target:
            print("Too low.")
        elif guess > target:
            print("Too high.")
        else:
            print("Correct!")

# Example usage
# guess_the_number()
```

</details>

---

### **3. Removing Duplicates**
Write a function `remove_duplicates(lst)` that removes duplicates from a list without using any advanced built-ins or list comprehensions.

**Example Input:**
```python
remove_duplicates([1, 2, 2, 3, 4, 4, 5])
```

**Example Output:**
```
[1, 2, 3, 4, 5]
```

<details>
<summary> Example answer</summary>

```python
def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

# Example usage
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
```

</details>

---

### **4. Prime Number Check**
Write a function `is_prime(n)` that checks whether a given integer `n` is a prime number. You cannot use any advanced built-ins or modules.

**Example Input:**
```python
is_prime(29)
```

**Example Output:**
```
True
```

<details>

```python
<summary> Example answer</summary>
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(29))  # Output: True
```

</details>


---

### **5. Count Vowels**
Write a function `count_vowels(s)` that counts how many vowels are present in a string. Do not use any string methods like `count` or `re`.

**Example Input:**
```python
count_vowels("hello world")
```

**Example Output:**
```
3
```

<details>

```python

<summary> Example answer</summary>
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage
print(count_vowels("hello world"))  # Output: 3

```

</details>

Bonus: recursive?

---

### **7. Simple Histogram**
Write a function `simple_histogram(lst)` that takes a list of integers and prints a histogram, where each number in the list represents the height of a bar. Each bar should be made of `*`.

**Example Input:**
```python
simple_histogram([3, 5, 1])
```

**Example Output:**
```
***
*****
*
```

<details>

```python


<summary> Example answer</summary>
def simple_histogram(lst):
    for num in lst:
        print('*' * num)

# Example usage
simple_histogram([3, 5, 1])
# Output:
# ***
# *****
# *

```python

</details>

---

### **8. Reverse an Integer**
Write a function `reverse_integer(n)` that reverses the digits of an integer without converting it to a string (large challenge!)

**Example Input:**
```python
reverse_integer(12345)
```

**Example Output:**
```
54321
```

<details>

```python

<summary> Example answer</summary>
def reverse_integer(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num

# Example usage
print(reverse_integer(12345))  # Output: 54321

```python

</details>

---
