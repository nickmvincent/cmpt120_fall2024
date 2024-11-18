
# Week 12 Recursion

This folder includes some interactive content we'll work through together during Week 12!

We'll spend some time trying to code key recursive functions and live code them together.

This deck has the SAME content as the readme file in `other_content/week12_recursion`. I will recommend you open that file during lecture, and I'll project this just for slightly better lecture viewing experience.


---

## Exercise 1: Review tree drawing

First, take a look at `draw_tree.py` in this directory. We're going to talk through how and way this code works. You should copy and paste this into a file on your local machine. Trying running it, then try modifying the *initial function call* so that the tree:

1. Has even more branches
2. Has fewer branches
3. Hits the base case immediately

---


## Exercise 2: Recursive Factorial

Probem: Write a recursive function that returns the factorial of a number. The factorial of n is equal to n times the factorial of n-1.

Start with a single parameter function definition: `def factorial(n):`

Examples:
- 0! = 0 (important: the factorial of 0 is equal to 1.)
- 1! = 1
- 2! = 2 * 1= 2 * 1!
- 3! = 3 * 2 * 1 = 3 * 2!
- so, `factorial(4) # -> 24`

<details>
<summary>Hint 1: Base Case</summary>

The base case will be based on the definition that factorial(0) = 1. If occurs when `n` is 0.

</details>

<details>
<summary>Hint 2: Recursive Case</summary>

In order to move towards the base case, consider decrementing the variable being passed by argument (`n`) by 1.

(e.g., somewhere in your code call, `factorial(n-1)`)
</details>

---

<details>
<summary> Solution</summary>

```python
def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

# Example usage:
print(factorial(5))  # Output: 120
```
</details>


--- 

## Exercise 3: Sums with recursion

### Exercise 3a: Summing all integers from 1 to n
Write a recursive function in Python, recursive_sum, that calculates the sum of all integers from 1 up to a given positive integer n.

Start with a single parameter function definition:`def recursive_sum(n):`

Examples: 
- `recursive_sum(4)  # Output: 9 (1 + 2 + 3 + 4)`
- `recursive_sum(5)  # Output: 15 (1 + 2 + 3 + 4 + 5)`

<details>
<summary>Hint 1: Base Case</summary> The base case occurs when `n` is 0. The sum of all integers up to 0 is simply 0. </details>

<details>
<summary>Hint 2: Recursive Case</summary>

If `n` is greater than 0, return `n` plus the result of `recursive_sum(n - 1)`.
</details>

---

<details>
<summary>Solution</summary>

```python
def recursive_sum(n):
    if n == 0:  # Base case
        return 0
    else:
        return n + recursive_sum(n - 1)  # Recursive case

# Example usage:
print(recursive_sum(5))  # Output: 15
```
</details>


---

### Exercise 3b: Summing all integers in a list
Problem: Write a recursive function in Python, recursive_sum_list, that calculates the sum of all integers in a given list.

Start with a single parameter function definition: `def recursive_sum_list(numbers):`

Examples:
- `recursive_sum_list([1, 2, 3, 4]) # Output: 10`
- `recursive_sum_list([5, 7, 3]) # Output: 15`

<details> <summary>Hint 1: Base Case</summary> The base case occurs when the list is empty. The sum of an empty list is simply 0. </details> <details>

<summary>Hint 2: Recursive Case</summary> If the list is not empty, return the first element of the list plus the result of `recursive_sum_list` called on the rest of the list. </details>

<details>

<summary>Hint 3: List Indexing</summary>

To get the first element of the list, use `numbers[0]`. The get the "rest of the list", use `numbers[1:]`.

</details>

---

<details>
<summary>Solution</summary>

```python
def recursive_sum_list(numbers):
    if not numbers:  # Base case
        return 0
    else:
        return numbers[0] + recursive_sum_list(numbers[1:])  # Recursive case

# Example usage:
print(recursive_sum_list([1, 2, 3, 4]))  # Output: 10
```

</details>

---

## Exercise 4: Reverse a string

Write a recursive function in Python, recursive_reverse, that reverses a given string. Start with a single parameter function definition: `def recursive_reverse(s):`

Example:
- `recursive_reverse("hello")  # Output: "olleh"`
- `recursive_reverse("abc")  # Output: "cba"`

<details>
<summary>Hint 1: Base Case</summary> The base case is an empty string or a single-character string, which is its own reverse.
</details>

<details>
<summary>Hint 2: Recursive Case</summary> Return the last character of the string concatenated with the reverse of the rest of the string.
</details>


<details>
<summary>Hint 3: String Indexing</summary>.

To get the last character of the string, we can use `s[-1]`. To get the "rest of the string", we can use `s[:-1]`.

</details>

---

<details>
<summary>Solution</summary>

```python
def recursive_reverse(s):
    if len(s) <= 1:  # Base case
        return s
    else:
        return s[-1] + recursive_reverse(s[:-1])  # Recursive case

# Example usage:
print(recursive_reverse("hello"))  # Output: "olleh"
```
</details>

---

## Exercise 5: Palindrome checker

Write a recursive function in Python, is_palindrome, that checks if a given string is a palindrome (reads the same forward and backward). Start with a single parameter function definition: `def is_palindrome(s):`


Examples:
- `is_palindrome("racecar")  # Output: True`
- `is_palindrome("hello")    # Output: False`


<details>
<summary>Hint 1: Base Case</summary>
The base case is when the string is empty or has a length of 1; both cases are palindromes by definition.
</details>

<details>
<summary>Hint 2: Recursive Case</summary> If the first and last characters are the same, check if the substring between them is a palindrome by calling `is_palindrome` recursively.
</details>

<details>
<summary>Hint 3: String Indexing</summary>
To check the substring between the first and last character, you can use the indexing approach `s[1:-1]` </details>


---

<details>
<summary>Solution</summary>

```python
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
```
</details>


---

## Exercise 6: Challenge!

"Nested List Sum"

Problem: Write a recursive function in Python, nested_sum, that calculates the sum of all integers in a list. However, this time, some elements of the list might be nested lists themselves. The function should recursively process these nested lists to calculate the total sum.

You can use `isinstance(item, int)` to check an item is an integer and `isinstance(item, list)` to check if an item is a list.

Start with a single parameter function definition: def nested_sum(data):

Examples:
- nested_sum([1, 2, [3, 4], 5]) # Output: 15
- nested_sum([[1, 2, [3]], 4, [5, [6]]]) # Output: 21
- nested_sum([1, [2, [3, [4, [5]]]]]) # Output: 15

<details> <summary>Hint 1: Base Case</summary> The base case is when the current item is an integer, in which case you can return the integer itself. </details>

<details> <summary>Hint 2: Recursive Case</summary> If the current item is a list, loop through each element in the list and recursively apply `nested_sum` on each element, summing the results. </details>


---

<details><summary>Solution</summary>

```python
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
```

</details>


---

## Exercise 7: Count Vowels in a String

Problem: Write a recursive function, count_vowels, that counts the number of vowels (a, e, i, o, u) in a given string. The function should be case-insensitive, so both uppercase and lowercase vowels are counted.

Start with a single parameter function definition: `def count_vowels(s):`

Examples:
- `count_vowels("hello") # Output: 2`
- `count_vowels("Recursion is fun!") # Output: 6`
- `count_vowels("xyz") # Output: 0`

<details> <summary>Hint 1: Base Case</summary> The base case occurs when the string is empty. If it is, return 0 because there are no vowels in an empty string. </details>

<details> <summary>Hint 2: Recursive Case</summary> Check if the first character of the string is a vowel. If it is, add 1 to the count, and then call the function recursively on the rest of the string. </details>

---

<details> <summary>Solution</summary>

```python
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
```

</details>