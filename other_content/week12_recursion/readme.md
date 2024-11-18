# Readme for Week 12 Recursion

This folder includes some interactive content we'll work through together during Week 12!

We'll spend some time trying to code key recursive functions. Then, we'll live code them together.

## Exercise 1: Review tree drawing

Take a look at `draw_tree.py`


## Exercise 2: Recursive Factorial

Write a recursive function that returns the factorial of a number.

The factorial of n is equal to n times the factorial of n-1.

For instance 3! = 3 * 2 * 1

and 4! = 4 * 3 * 2 * 1 = 4 * 3!

Important: the factorial of 0 is equal to 1.

Start with a single parameter function definition:

`def factorial(num):`


<details>
<summary>Hint 1: Base Case</summary>
The base case will be based on the definition that factorial(0) = 1.
</details>

<details>
<summary>Hint 2: Recursive Case</summary>

In order to move towards the base case, consider decrementing the variable being passed by argument by 1

(e.g., somewhere in your code call, `factorial(num-1)`

</details>


## Exercise 3: Sums with recursion

Write a recursive function in Python, recursive_sum, that calculates the sum of all integers from 1 up to a given positive integer n.

Start with a single parameter function definition:

`def recursive_sum(num):`
 
Example: 
`recursive_sum(5)  # Output: 15 (1 + 2 + 3 + 4 + 5)`

<details>
<summary>Hint 1: Base Case</summary> The base case occurs when `n` is 0. The sum of all integers up to 0 is simply 0. </details>

<details>
<summary>Hint 2: Recursive Case</summary> If `n` is greater than 0, return `n` plus the result of `recursive_sum(n - 1)`. </details>


<details>
<summary>Solution</summary>

```python
def recursive_sum(n: int) -> int:
    if n == 0:  # Base case
        return 0
    else:
        return n + recursive_sum(n - 1)  # Recursive case

# Example usage:
print(recursive_sum(5))  # Output: 15
```
</details>



## Exercise 4: Reverse a string

Write a recursive function in Python, recursive_reverse, that reverses a given string.

Start with a single parameter function definition:

`def recursive_reverse(s):`

Example: `recursive_reverse("hello")  # Output: "olleh"`

<details>
<summary>Hint 1: Base Case</summary> The base case is an empty string or a single-character string, which is its own reverse. </details>

<details>
<summary>Hint 2: Recursive Case</summary> Return the last character of the string concatenated with the reverse of the rest of the string. </details>

<details>
<summary>Hint 3</summary> To get the "rest of the string", we can use `s[:-1]`</details>

<details>
<summary>Solution</summary>

```python
def recursive_reverse(s: str) -> str:
    if len(s) <= 1:  # Base case
        return s
    else:
        return s[-1] + recursive_reverse(s[:-1])  # Recursive case

# Example usage:
print(recursive_reverse("hello"))  # Output: "olleh"
```
</details>

## Exercise 5: Palindrome checker

Write a recursive function in Python, is_palindrome, that checks if a given string is a palindrome (reads the same forward and backward).


Start with a single parameter function definition:

`def is_palindrome(s):`


Examples:
`is_palindrome("racecar")  # Output: True`
`is_palindrome("hello")    # Output: False`


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


<details>
<summary>Solution</summary>

```python
def is_palindrome(s: str) -> bool:
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