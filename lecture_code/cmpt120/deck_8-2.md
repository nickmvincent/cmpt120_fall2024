---
# You can also start simply with 'default'
theme: seriph
# random image from a curated Unsplash collection by Anthony
background: images/kseniia-rastvorova-U2AwijfUNS4-unsplash.jpg
title: Week 8
info: |
  Slides for Week 8 of CMPT 120, Fall 2024, Section D300, Nicholas Vincent
# apply unocss classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
# take snapshot for each slide in the overview
overviewSnapshots: true
---

# Welcome to Week 8

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space to start <carbon:arrow-right class="inline"/>
  </span>
  <span> Photo by <a href="https://unsplash.com/@hixenia?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Kseniia Rastvorova</a> on <a href="https://unsplash.com/photos/trees-near-mountain-U2AwijfUNS4?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
  </span>
</div>

---

## Agenda for Today

- Announcements
- Quick comments on midterm
- `def`, `while`, `continue`, `break`, bits and bytes, oh my!

---
title: Announcements
---

## Announcements

- Putting more course content on GitHub going forward (readings, slides, due dates)
- Assignment 4 extension (now *due* Oct 30)
- Midterm marks and grading details: as soon as possible!

---
title: Python Functions with `def`
---

# Python Functions with `def`

- **`def`**: Used to define a function in Python

Syntax:

```python
def function_name(parameters):
    # code block
    return value
```

Example:

```python
def greet(name):
    return f"Hello, {name}!"
```

- Functions:
  - Encapsulate code for reuse
  - Can accept parameters
  - Can return values (or `None` if no return statement)

---

## Three more examples

- Ex1:
  ```python
  def foo1(a,b):
    return a+b
  ```

- Ex2:
  ```python
  def foo2(n):
    return n % 2 == 0
  ```

- Ex3:
  ```python
  def foo3(n)
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result
  ```

---

## Better names


```python
def add_two_nums(a,b):
  return a+b
```

```python
def is_even(n):
  return n % 2 == 0
```

```python
def factorial(n)
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result
```

---
title: Python `while` Loop
---

# Python `while` Loop

- **`while` loop**: Repeats a block of code as long as a condition is `True`
- Syntax:
  ```python
  while condition:
      # code block
  ```
- Example:
  ```python
  i = 0
  while i < 5:
      print(i)
      i += 1
  ```


---

---
title: Why Use a `while` Loop?
---

# Why Use a `while` Loop (or not!)?

- **Flexible Condition**:
  - Use `while` when the number of iterations is unknown.
  - Example: Waiting for user input or external event.
  
- **Infinite Loops**:
  - Easier to create loops that run indefinitely until a condition is met.

- **Dynamic Conditions**:
  - When the loop condition is more complex than simple iteration (e.g., event-based, real-time updates).

- **Example**:
  ```python
  while not user_input:
      user_input = input("Enter something: ")
  ```

- When to Avoid:
  - Avoid while loops when you can define a specific range or collection to iterate over.

--- 

---
title: Python `continue`
---

# Python `continue`

- **`continue`**: Skips the rest of the code inside the loop for the current iteration and moves to the next iteration.

- **Use Case**:
  - When you want to skip certain iterations based on a condition.
  
- **Syntax**:
  ```python
  while condition:
      if some_check:
          continue
      # remaining code for other iterations
  ```

--- 

- **Example**:
  ```python
  for i in range(5):
      if i == 2:
          continue
      print(i)
  ```
  
  - Output: `0, 1, 3, 4` (skips `2`)

- **Key Point**: 
  - Useful for skipping specific cases without stopping the loop.
  - Sometime if you "found what you're looking for" you can continue

---

---
title: More Practical Examples of `continue`
---

# More Practical Examples of `continue`

- **Skip Even Numbers**:
  ```python
  for i in range(10):
      if i % 2 == 0:
          continue
      print(i)
  ```
  
  - Output: `1, 3, 5, 7, 9` (skips even numbers)

- **Skip Blank Input**:
  ```python
  inputs = ["hello", "", "world", "", "python"]
  for item in inputs:
      if item == "":
          continue
      print(item)
  ```

  - Output: `hello, world, python` (skips empty strings)

- **Key Takeaway**:
  - `continue` helps ignore unwanted cases, allowing the loop to focus on relevant data.


---

---
title: Python `break`
---

# Python `break`

- **`break`**: Immediately exits the loop, stopping further iterations.

- **Use Case**:
  - When you need to stop the loop based on a condition.

- **Syntax**:
  ```python
  while condition:
      if some_check:
          break
      # remaining code
  ```

- **Example**:
  ```python
  for i in range(10):
      if i == 5:
          break
      print(i)
  ```

  - Output: `0, 1, 2, 3, 4` (loop stops at `i == 5`)

- **Key Point**:
  - `break` is useful when you want to exit a loop early based on a condition.

---
title: Practical Examples of `break`
---

# Practical Examples of `break`

- **Stop on User Input**:
  ```python
  while True:
      user_input = input("Enter a number (or 'q' to quit): ")
      if user_input == 'q':
          break
      print(f"You entered: {user_input}")
  ```
  
  - The loop stops when the user enters `q`.

- **Find First Match in a List**:
  ```python
  numbers = [3, 5, 7, 8, 10, 12]
  for num in numbers:
      if num % 2 == 0:
          print(f"First even number found: {num}")
          break
  ```

  - The loop stops after finding the first even number (`8`).

- **Key Takeaway**:
  - `break


---

Let's put it all together and transition back to bits and bytes!

---


```python
def binary_to_decimal(binary_str):
    """Convert a binary string to a decimal number."""
    decimal = 0
    for digit in binary_str:
        decimal = decimal * 2 + int(digit)
    return decimal

def decimal_to_ascii(decimal):
    """Convert a decimal number to its ASCII character."""
    return chr(decimal)

```

---

```python
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
```

---

Important things from bits and bytes

---

---
title: How to Read Binary Code
---

# How to Read Binary Code

<div class="text-center text-2xl mb-6">
  Converting Binary to Decimal
</div>

<div class="grid grid-cols-2 gap-4">
  
  - **Binary Representation**:
    - Binary is a base-2 system (only `0` and `1`).
    - Each binary digit (bit) represents a power of 2.

  - **Example**:
    ```python
    Binary: 1011
    1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0 = 11
    ```

</div>

---

<div class="text-center text-2xl mb-6">
  Step-by-Step Guide
</div>

- **Start from the rightmost bit**:
  - Assign powers of 2 (starting from 2^0).
  
- **Multiply each bit** by its corresponding power of 2.
  
- **Sum the results** to get the decimal number.

<div class="mt-4">
  - Binary: `1011`
  - Decimal: `11`
</div>


---
title: Reading Binary Code
layout: center
---

# Reading Binary

<style>
  table {
    font-size: 1.2em;
  }
  th, td {
    padding: 8px 16px;
    text-align: center;
  }
</style>

| Power of 2 | 2⁷  | 2⁶  | 2⁵  | 2⁴  | 2³  | 2²  | 2¹  | 2⁰  |
|------------|-----|-----|-----|-----|-----|-----|-----|-----|
| Value      | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| Binary     | 1   | 0   | 1   | 1   | 0   | 1   | 0   | 1   |

Total: 128 + 0 + 32 + 16 + 0 + 4 + 0 + 1 = 181

---

<div class="text-center text-xl mt-8">
  Binary `1011` equals Decimal `11`
</div>

<div class="text-center text-2xl mt-4">
  Powers of 2 are key to understanding binary!
</div>


---
title: ASCII
---

ASCII is a table that maps decimal numbers to characters

---
layout: center
---

# ASCII Table (American Standard Code for Information Interchange)

<style>
  table {
    font-size: 1.1em;
  }
  th, td {
    padding: 6px 12px;
    text-align: center;
  }
</style>

| Character | Binary      | Decimal | Hexadecimal | Description     |
|-----------|------------|---------|-------------|-----------------|
| `A`       | 0100 0001  | 65      | 0x41        | Uppercase A    |
| `a`       | 0110 0001  | 97      | 0x61        | Lowercase a    |
| `0`       | 0011 0000  | 48      | 0x30        | Number zero    |
| ` `       | 0010 0000  | 32      | 0x20        | Space          |
| `!`       | 0010 0001  | 33      | 0x21        | Exclamation    |
| `\n`      | 0000 1010  | 10      | 0x0A        | New line       |

<div class="text-sm mt-4">
Note: ASCII uses 7 bits, allowing for 128 characters (0-127).<br>
Extended ASCII uses 8 bits, allowing for 256 characters (0-255).
</div>


--- 
title: Unicode
---

- Unicode is a superset of ASCII. 
- A is a super of B means A includes B, but also other stuff.
- ASCII (American Standard Code for Information Interchange) defines 128 characters, including English letters, digits, and control characters, using 7 bits per character. 
- Unicode, on the other hand, was designed to encompass more characters from more writing systems worldwide, using up to 32 bits per character. The first 128 characters in Unicode are identical to ASCII, ensuring backward compatibility.

---

---