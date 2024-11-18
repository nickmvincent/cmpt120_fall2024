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

##  Week 12 Learning outcomes 

- More recursion
  - Able to write code that can produce the sum of a list using recursion
  - Able to write code that can reverse a string using recursion 
  - Able to write a recursive or iterative function to check if a string is a palindrome

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

