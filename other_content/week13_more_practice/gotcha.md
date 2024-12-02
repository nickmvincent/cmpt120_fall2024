# GOTCHAS

Reminders of GOTCHAs, organized into **TESTABLE** and **UNTESTABLE** categories:

Stuff in TESTABLE category -- try to feel super confident about this!

---

### **TESTABLE Gotchas**

```python

# Negative indexing retrieves elements from the end
s = "hello"
print(s[-1])  # 'o'

# Attempting to modify a string directly
s = "hello"
s[0] = "H"  # TypeError: 'str' object does not support item assignment

# Tricky uses of `in`
print("ello" in "hello")  # True
print("H" in "hello")  # False (case-sensitive)

# String methods do not modify in place
s = "  Hello "
print(s.strip().upper())  # 'HELLO'
print(s)  # Original remains: '  Hello '

# Slicing creates a new list, not a reference
lst = [1, 2, 3]
sublist = lst[:]
sublist[0] = 99
print(lst)  # [1, 2, 3]

# Modifying a list through aliases
lst1 = [1, 2, 3]
lst2 = lst1
lst2[0] = 99
print(lst1)  # [99, 2, 3]

# Negative indexing and slicing
lst = [1, 2, 3, 4]
print(lst[-2:])  # [3, 4]
print(lst[-2:-1])  # [3]

# Range with negative steps
print(list(range(5, 0, -1)))  # [5, 4, 3, 2, 1]

# Non-empty objects evaluate as True
if " ":
    print("This runs!")  # "This runs!"

# Zero or empty objects evaluate as False
print(bool([]))  # False
print(bool(0))  # False

# Functions without a return statement return None
def func():
    pass

print(func())  # None

# Division and integer division
print(4 / 2)  # 2.0
print(5 // 2)  # 2

# Overwriting built-in names
list = [1, 2, 3]
print(list(range(3)))  # TypeError: 'list' object is not callable

# Importing a module doesn't bring functions into scope
import math
print(sqrt(4))  # NameError: name 'sqrt' is not defined

# Concatenating strings and integers
print("Age: " + 21)  # TypeError: can only concatenate str (not "int") to str

# IndexError when accessing an out-of-range index
lst = [1, 2, 3]
print(lst[5])  # IndexError: list index out of range

# Negative slicing steps
lst = [1, 2, 3, 4, 5]
print(lst[-1:-3:-1])  # [5, 4]

# Unintended return behavior in loops
def check(lst):
    for i in lst:
        if i % 2 == 0:
            return True
    return False

print(check([1, 3, 5]))  # False

# Multiple return paths in a function
def example(x):
    if x > 0:
        return x
    # Implicitly returns None if x <= 0

print(example(-1))  # None
```

---

### **UNTESTABLE Gotchas**

```python
# Slicing beyond string length does not raise an error
print(s[0:10])  # 'hello'

# Reversing strings with slicing steps
print(s[::-1])  # 'olleh'

# Multiplying lists with shared references
lst = [[0]] * 3
lst[0][0] = 1
print(lst)  # [[1], [1], [1]] (not [[1], [0], [0]])

# Empty range from reversed indices
print(list(range(5, 0)))  # []

# Step argument in range
print(list(range(0, 10, 0)))  # ValueError: step must not be zero

# Short-circuit evaluation
x = 0
if x and 1 / x:
    print("Won't run")  # Avoids ZeroDivisionError

# Modifying lists during iteration
lst = [1, 2, 3]
for i in lst:
    lst.remove(i)
print(lst)  # [2]

# Mutable default arguments
# POPULAR ON INTERVIEWS (or at least it used to be)
def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(append_to_list(1))  # [1]
print(append_to_list(2))  # [1, 2]

# Floating-point precision errors
print(0.1 + 0.2)  # 0.30000000000000004

# Loop variable persistence
for i in range(3):
    pass
print(i)  # 2

# Chained comparisons
print(1 < 2 < 3)  # True (evaluates as 1 < 2 and 2 < 3)

# Modulo with negatives
print(-7 % 3)  # 2 (remainder has same sign as divisor)

# Exponentiation precedence
print(-2**2)  # -4, equivalent to -(2**2)

# Chaining assignments
x = y = [1, 2, 3]
x.append(4)
print(y)  # [1, 2, 3, 4]
```

---