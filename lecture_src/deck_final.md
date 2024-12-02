

# The Big Review Deck


<div style="display:flex; justify-content: center;">
<img src="/images/priscilla-du-preez-Vm0nC-VKFTc-unsplash.jpg" style="max-width:200px"/>
</div>

From Priscilla Du Preez @ https://unsplash.com/photos/scenery-of-bridge-in-front-of-silhouette-of-mountain-Vm0nC-VKFTc





---


# Week 1: Introduction to CS and Problem Solving

<div class="grid grid-cols-2 gap-4">
<div>

- Know that CS is problem-solving
- Problem solving by subdividing tasks
- Characteristics of an algorithm
- Plagiarism rules for programming
- What is pseudocode?
- Write Python comments, program header block info
- Output "Hello World" using print()
- Programming languages vs. natural languages
- Use IDLE and an IDE
- Submit code as .zip or .py file

</div>
<div>

```python
# Problem Solving Example: Basic Algorithm & Hello World
def greet():
    """Program header block: Author, Date, Purpose."""
    print("Hello, World!")  # Simple print statement

# Algorithm breakdown using function
greet()
```

</div></div>


---

# Week 2: Basics of Python Programming

<div class="grid grid-cols-2 gap-4">
<div>

- Design/plan algorithms using pseudocode/comments
- Input from terminal to a variable or without saving
- Assign a value to a variable
- Output a string variable, string concatenation
- Variable naming rules
- Data types introduction (focus on String)
- Lists and random.choice() (including imports)
- Purpose of modules, imports at top
- If/elif/else, logical operators (`and`, `or`)
- Comparison operators in conditional statements
- Boolean expressions, testing programs interactively
- Characteristics of good software
- Interpreter’s role in error catching

</div>

<div>

```python
# Variables, Input, Output, and Conditionals
name = input("Enter your name: ")  # Obtain user input
age = int(input("Enter your age: "))  # Type conversion from string to int

if age >= 18:
    print(f"Welcome, {name}. You are eligible!")  # Use of formatted string
else:
    print(f"Sorry, {name}. You are not eligible.")  # Conditional branching
```

</div> </div>

---

# Week 3: Strings, Lists, and Conditionals

<div class="grid grid-cols-2 gap-4">
<div>

- String methods: `strip()`, `lower()`, `upper()`
- Identify String data type
- Test methods using REPL
- Use `in` keyword with strings and lists
- Create a list from variables/user inputs
- Loop over list elements with `for`
- Understand `range()` function and index variable
- Integer type and conversion to String
- Concatenation rules, nested conditionals
- Error types: syntax vs. semantic
- Method chaining with `.`

</div>
<div>

```python
# String Methods and Looping Over Lists
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(fruit.lower())  # Using string methods to manipulate list elements

# Check if a character is in a string
if "a" in "banana":
    print("Found 'a' in banana")
```

</div></div>

---

# Week 4: Loops and Arithmetic

<div class="grid grid-cols-2 gap-4">
<div>- U
se `range()` with variables
- Loop to reduce code duplication
- Integers, floats, initialization
- Accumulator pattern, `+=` shortcut
- Get list length, convert input to Integer
- Division types, arithmetic operations
- Print floats to given decimals

</div>
<div>

```python
# Accumulator Pattern and Loop with Range
total = 0
for i in range(1, 6):  # Loop from 1 to 5
    total += i  # Accumulate the sum

print(f"Sum of numbers from 1 to 5 is: {total}")

# Basic arithmetic operations
div_result = 10 / 3  # Division (float)
print(f"Division result: {div_result:.2f}")  # Print to 2 decimal places
```
</div></div>

---

# Week 5: File I/O, Lists, and Comparisons

<div class="grid grid-cols-2 gap-4">
<div>

- Read lines from text files
- String splitting, list indexing/slicing
- Compare numbers and strings
- operator precedence (light treatment)
- Nested conditionals, nested loops
- find comment elements between lists
- List concatenation, accumulation pattern for strings/lists
- Calculate max/min, coordination between lists by index

</div>
<div>

```python
# Reading a File and Splitting Lines into Lists
with open("example.txt", "r") as file:
    for line in file:
        words = line.strip().split()  # Split line into words
        print(words)  # List of words
```
</div></div>

---

# Week 7: Bits, Bytes, and Data Representation

<div class="grid grid-cols-2 gap-4">
<div>

- `len()` function, string immutability, loops by index
- Bits and bytes, converting bytes to bits
- Binary to decimal, hexadecimal goals
- ASCII and Unicode overview
- RGB storage in hexadecimal
- Important numbers: 1 byte = 8 bits, 8-bit per character for 8-bit character set, 6 hexadecimal digits in an RBG number, therefore 24 bits, because 6 digits x 4 bits per digit
- Different numbering systems (base-2, base-10, base-16) require different number of "symbols"

</div>

<div>

```
# Convert Bytes to Bits and Decimal to Binary
bytes_value = 4
bits_value = bytes_value * 8  # Convert bytes to bits
print(f"{bytes_value} bytes is {bits_value} bits")

# FF0001 -- what is this?
# 00FF00 -- what is this?
```

</div></div>

---

# Week 8: Turtle Graphics and Functions

<div class="grid grid-cols-2 gap-4">
<div>

- Use Turtle package for drawing (specific methods that are "testable" to be described in class)
- Read Turtle code and understand the purpose
- Create and call functions (with/without parameters)
- Loop variable as function argument
- Turtle coloring using RGB values
- Variable scope (function vs. global)

</div>
<div>

```python
# Turtle Graphics Drawing a Square
import turtle

def draw_square(size):
    pen = turtle.Turtle()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)

draw_square(100)  # Draw a square with side length of 100
turtle.done()
```
</div></div>

---

# Week 9: Functions and While Loops

<div class="grid grid-cols-2 gap-4">
<div>

- Define and use functions, `return` vs `print()`
- Effect of `return` in loops, handling `None`
- Identify appropriate use of `while` vs `for`
- Sentinel and multiple control variables in `while`
- Use `while` for input validation

</div>
<div>

```python
# Function that Returns a Value and While Loop for Validation
def double_number(num):
    return num * 2

valid_input = False
while not valid_input:
    user_input = input("Enter a positive number: ")
    if user_input.isdigit() and int(user_input) > 0:
        valid_input = True
        result = double_number(int(user_input))
        print(f"Double of {user_input} is {result}")
    else:
        print("Invalid input, please enter a positive number.")
```
</div></div>

---

# Week 10: Modules and Image Processing

<div class="grid grid-cols-2 gap-4">
<div>

- Create and use custom modules
- Module shortnames and relationship of modules to filesystem
- RGB colors and pixel manipulation
- Access/modify 2D/3D lists for images
- Using course-specific `cmpt120images` module for images
- Return Boolean expressions directly

</div>
<div>

```python
# Custom Module Import and RGB Color Manipulation
import cmpt120images

image = cmpt120images.loadImage("example.png")
height = len(image)
width = len(image[0])

for y in range(height):
    for x in range(width):
        # Invert the RGB colors of the pixel
        r, g, b = image[y][x]
        image[y][x] = (255 - r, 255 - g, 255 - b)

cmpt120images.saveImage(image, "inverted_example.png")
```
</div></div>

---

# Week 11: Lists, Aliases, and Recursion

<div class="grid grid-cols-2 gap-4">
<div>

- Alias vs. copy of lists
- Function parameter and argument as aliases
- List modification inside functions
- Basic recursion, draw recursive patterns
- 3 characteristics of recursive function
- Write factorial, sum of list, reverse string using recursion
- Check if a string is a palindrome (recursive/iterative)

</div>
<div>

```python
# Recursive Function to Calculate Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5 is: {factorial(5)}")
```
</div></div>

---

# Week 12: Search Algorithms

<div class="grid grid-cols-2 gap-4">
<div>

- Review recursion
- Write linear search functions (Boolean/index/indices)
- Recognize and code recursive binary search

</div>
<div>

```python
# Binary Search Implementation
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

numbers = [1, 3, 5, 7, 9, 11]
index = binary_search(numbers, 7)
print(f"Element found at index: {index}" if index != -1 else "Element not found")
```
</div></div>

---

# Week 13: Sorting and Complexity

<div class="grid grid-cols-2 gap-4">
<div>

- Swap list elements, selection sort
- Intermediate steps of selection sort
- Measure runtime with `time`
- Apply algorithms on data from a file
- Characteristics of a good algorithm
- Big O notation and complexity examples. 7 reference functions.
- Merge Sort approach and complexity
- Critical operations, best/worst case scenarios
- Analyze binary search and merge two lists

</div>
<div>

```python
# Selection Sort Implementation
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

data = [64, 25, 12, 22, 11]
selection_sort(data)
print(f"Sorted array: {data}")
```
</div></div>