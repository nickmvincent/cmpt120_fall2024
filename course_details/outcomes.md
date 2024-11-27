##  Week 1 Learning Outcomes 

1. Know that CS is problem solving
2. Understand problem solving by subdividing tasks into subtasks
3. Able to explain the main characteristics of an algorithm
4. Understand plagiarism for programming and this course
5. Know what pseudocode is
6. Able to write Python comments
7. Know what information is in a program header block (i.e. initial comments with author, date and purpose)
8. Able to output a "Hello World" using print()
9. Able to contrast programming languages with natural languages
10. Able to work with IDLE and an IDE
11. Able to submit code in a .zip or .py file

##  Week 2 Learning Outcomes 

1. Able to design/plan an algorithm, e.g. using comments or pseudocode
2. Able to apply some common problem solving strategies, such as breaking down the problem into smaller pieces
3. Able to obtain input into Python from the terminal to a variable 
4. Able to receive input from terminal without saving it to a variable
5. Know how to assign a value to a variable
6. Able to output a string variable in a print statement
7. Able to concatenate two strings
8. Know the constraints and conventions on variable naming
9. Know that there are different types of data, although String is the focus for now
10. Able to create a list of strings and assign it to a variable
11. Able to use the random.choice() function on a list (including import)
12. Knows what the . after a module name does
13. Understands that modules contain functions (light treatment)
14. Know to put import statements at the top of the program, after header
15. Knows how to use if/elif statements with ==
16. Knows how to use the else clause
17. Understands the meaning of logical operators and, or
18. Knows about comparison operators and how to use in a conditional statement
19. Understands what a Boolean expression is
20. Understands the basics in combining Boolean expressions using `and` and `or`
21. Is able to print a Boolean expression
22. Knows some of the characteristics of good software: usable, pleasing to read, minimizes duplication, robust to errors
23. Knows to include a short description of the program in the header
24. Able to test a program for the desired outcome, interactively
25. Able to test a program (lightly) for unexpected cases, interactively
26. Knows how to test smaller pieces of code by commenting out blocks
27. Knows the interpreter's role in catching errors

##  Week 3 Learning Outcomes 
1. Can apply the strip, lower, and upper String methods appropriately
2. Can identify the String data type
3. Able to interactively test methods and inspect variables (using REPL in IDLE, IDE, online tool, etc.)
4. Able to use the **in** keyword for both (1) string in a list and (2) character(s) in a string.
5. Can create a list using variables (e.g. from user inputs)
6. Can use a for to loop over elements of a list
7. Understands the `range(...)` function and what it represents
8. Knows the concept of the index variable in for i in range(...)
9. Understands the Integer type
10. Able to convert an Integer to a String
11. Knows that concatenation is only applicable between 2 strings, not Int and String
12. Is able to design and implement nested conditionals
13. Understands the concept of robustness with respect to code
14. Can identify whether an error is a syntax error or a semantic error
15. Understands the concept of method chaining (applying to an object and sending output from one method to the method to its right, using the . operator)

##  Week 4 Learning Outcomes 
1. Can use the range function with arguments that are variables (not only numbers)
2. Knows that a loop is a way to reduce duplication of code
3. Able to use integers and floats and manipulate them in variables
4. Knows how to initialize a variable of type Integer
5. Can apply the accumulator pattern (including initialization) and += shortcut
6. Able to get the length of a list
7. Able to convert strings to integer type (esp. user input)
8. Knows that division of integers converts type to float
9. Able to perform arithmetic operations on numbers
10. Can use the accumulator pattern with other arithmetic operators
11. Can print floats to a given number of decimal places

##  Week 5 Learning Outcomes 

1. Able to open and read lines from a text file
2. Able to split a string into a list
3. Able to access a specific element(s) of a list using indexing/slicing
4. Able to access a specific character(s) in a string using indexing/slicing
5. Able to perform comparisons between numbers, taking into account order of operators (operator precedence)
6. Able to perform comparisons (e.g. !=, &lt;,>) with strings
7. Can interpret code with nested conditionals with comparison operators (e.g. !=, &lt;,>=) and numbers
8. Able to find the common elements between 2 lists
9. Able to understand and use a nested for loop
10. Able to apply operator precedence to evaluate expressions
11. Able to concatenate lists
12. Able to apply accumulation pattern for strings and lists (previously was numbers)
13. Able to calculate the maximum or minimum
14. Able to coordinate between 2 or more lists using a common  index

##  Week 7 Learning outcomes 

- know `len`, know that strings are immutable, use loops by index
- Know what a bit represents in a computer
- Convert a given number of bytes (or kb, mb) to bits
- Convert binary <> decimal
- Understand the goal of hexadecimal
- Know that binary numbers convert to hexadecimal by grouping of 4 bits
- Know the purpose of ASCII
- Know relationship of Unicode to ASCII
- Know how to store RGB numbers (3 byte aka 24 bits aka 6 hexadecimal digits)

##  Week 8 Learning outcomes 

- Able to use the Turtle package to create drawings (see methods below)
- Able to read and understand basic Turtle code to visualize its output
- Able to create a function 
- Able to create a function with parameters
- Able to call a function previously created in the program
- Able to call a function from a loop and use the loop variable as argument
- Able to color the turtle using turtle color names
- Able to color the turtle using color coded with RGB values as a 3-tuple with values for (red,green,blue)
- Able to identify the scope of a variable, especially in relation to function scope

```python
# turtle methods
import turtle
pen = turtle.Turtle()
pen.forward(10)
pen.stamp()
pen.right(180)
pen.left(90)
pen.penup()
pen.pendown()
pen.goto(10,-10)
pen.color("blue")
turtle.colormode(255)
mycolor = (255,0,120)
pen.color(mycolor)

# defining a function
def myfunction(a,b):
    # do things with a and b
    # possibly use `return` statement

myfunction(45,20)

for i in range(...):
      myfunction(i*2,i)
```

##  Week 9 Learning outcomes 

- Functions!
  - Able to create and use functions that return values ()
  - Knows how to call a function so that the value returned from a function is received
  - Knows that print() is different than return in a function
  - Knows the effect that a return has if executed inside a loop (inside a function)
  - Identifies cases when the value None is produced when calling a function
- While Loops!
  - Able to identify when a while loop would be appropriate compared to a for loop
  - Able to create a valid while loop with a sentinel (control variable) 
  - Able to create a valid while loop with multiple control variables
  - Able to use a while loop to validate user input

```python

def multiplier_100(a):
  return (a*100)

receive = multiplier_100(5)

i = 0
while i <10:
    i+=1
    # do something with i
```

##  Week 10 Learning outcomes 

You should know:

- Modules!
  - How to create and use a module containing one's own defined functions
  - How to import and access the contents of packages and modules
  - How to import a module with a short name

- Image process and 2D list / 3D list manipulation:
  - How pixel colors are represented by RGB values 
  - How to pass global variables into local scope
  - That you can to directly return a Boolean expression in a function without using if statement in the function (e.g. `return x > 10`)
  - How to access and modify a 2D image in the form of a list of lists (with 0s and 1s)
  - How to access and modify a 3d image in the form of a list of lists (with 3-item RGB lists)
  - How to manipulate 2 dimensional lists, process a row, process a column, process a specific element
  - How to read, show and save images using the 3Dlist representing an image as provided in the cmpt120images module 
  - How to extract and/or change the color as RGB and/or individual color components of a pixel using a 3DList representing an image as provided in the cmpt120images module

```
def my_func(a,b):
  return a < b

if  my_less_than(2,30):
     ..............

my_3d_list[0][10][4]

import cmpt120images
import my_custom_module
```

##  Week 11 Learning outcomes 

- Alias vs. copy, lists and functions, mutability of lists
  - Knows what a list alias is, versus a copy
  - Knows the implication of sending a list as an argument to a function (i.e. argument and parameter become aliases)
  - Knows how to modify a list in place using append() 
  - Knows the effect of modifying a list inside a function when the list is sent as parameter, even if it is not returned
- Starting on recursion
  - Knows the basic elements of a recursive function
  - Able to analyze a recursively drawn tree in Turtle
  - Able to write a simple recursive function that does not return any value, e.g. to draw concentric circles
  - Understands the difference between executing a line of code before a recursive call vs. after a recursive call
  - Is able to apply the 3 laws of recursion to write or analyze a basic recursive fruitful function
  - Able to write a factorial function recursively
  - Able to write code that can produce the sum of a list using recursion
  - Able to write code that can reverse a string using recursion 
  - Able to write a recursive or iterative function to check if a string is a palindrome

```
mylist = [1,2,3]
mylistalias = mylist
mylist.append(4)
# mylist and mylistalias now have 4 elements

def changes_list(alist):
  alist[0] = 1

origlist = ["a","b","c"]
changes_list(origlist)
# origlist is now changed
```

##  Week 12 Learning outcomes 

(Spend more time on recursion learning outcomes this week)

- Search!
  - Able to write a linear search function with various return types (Boolean using for/while, index of unique found element, indices of all found elements)
  - Able to recognize a binary search and produce code for it
  - Able to produce the code for a recursive binary search

Code snippets are getting longer. See lecture slides.

##  Week 13 Learning outcomes 


- Swap different elements in a list
- Identify and write the code for a selection sort
- Describe intermediate steps of a selection sort
- Use the datetime or time module to compute the running time of code
- Apply learned search and sort algorithms on a dataset from a file
- Use range() with multiple parameters to iterate over a sublist, or to iterate backwards over a list
- List 10 characteristics of a good algorithm/code
- Understand in what case(s) time complexity is important to consider
- Give 7 examples of reference functions commonly used with Big O notation and compare them
- Describe the general approach and functioning of Merge Sort

- List 3 examples of critical operations
- Identify the number of critical operations in terms of an input size n, given a piece of iterative code
- Calculate the time complexity in big O notation for a piece of iterative code
- Give best/worst case scenarios (order and description of scenario) for Linear Search and Selection Sort
- Identify a piece of code that is O(logn)
- Analyze the time complexity of binary search and compare its use over linear search
- Give the complexity of Merge Sort
- Write code to merge two ordered lists

