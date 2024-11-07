# CMPT 120 Readings Guide

For pre-midterm readings and learning outcomes, see Canvas Learning Outcomes / Readings entries and the pre-midterm slide deck.

## Week 7

Readings:

- [9.6](https://runestone.academy/ns/books/published/thinkcspy/Strings/Length.html) (covers `len`)
- [9.7](https://runestone.academy/ns/books/published/thinkcspy/Strings/StringsareImmutable.html) (covers immutability of strings)
- [9.11](https://runestone.academy/ns/books/published/thinkcspy/Strings/TraversalandtheforLoopByIndex.html) (covers loops by index)
- Chapter 1 from Gaddis, Introduction to Computers and Programming (bits and bytes)

Learning outcomes:

- know `len`, know that strings are immutable, use loops by index
- Know what a bit represents in a computer
- Convert a given number of bytes (or kb, mb) to bits
- Convert binary <> decimal
- Understand the goal of hexadecimal
- Know that binary numbers convert to hexadecimal by grouping of 4 bits
- Know the purpose of ASCII
- Know relationship of Unicode to ASCII
- Know how to store RGB numbers (3 byte aka 24 bits aka 6 hexadecimal digits)


## Week 8

These may extend into Week 9 (the Week 9 reading list is much shorter).

### Week 8 Readings:

- From Runestone Chapter 4, which covers the `turtle` module and drawing images in Python
  - [4.1](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/intro-HelloLittleTurtles.html)
  - [4.2](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/OurFirstTurtleProgram.html)
  - [4.3](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/InstancesAHerdofTurtles.html)
  - [4.6](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/IterationSimplifiesourTurtleProgram.html)
  - [4.7](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/TherangeFunction.html)
  - [4.8](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/AFewMoreturtleMethodsandObservations.html), and [4.9](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/SummaryofTurtleMethods.html).
  - You can go quickly through these readings: we will cover the content directly in lecture.
  - In 4.4. and 4.5, you've already seen the for loop. revisit them if you want to review.
- Start Runestone Chapter 6, which covers functions
  - [6.1](https://runestone.academy/runestone/books/published/thinkcspy/Functions/functions.html)
  - [6.2](https://runestone.academy/ns/books/published/thinkcspy/Functions/Functionsthatreturnvalues.html)
  - [6.4](https://runestone.academy/ns/books/published/thinkcspy/Functions/Variablesandparametersarelocal.html)
  - [6.11](https://runestone.academy/ns/books/published/thinkcspy/Functions/ATurtleBarChart.html) (connects functions back to turtle))
  - You can skip 6.3 for now (though if you are considering software engineering, you want to just read it now!)
- Read about while loops from Chapter 8
  - Read [8.3](https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/ThewhileStatement.html) and [8.8](https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/SentinelValuesAndValidation.html)
  - Optional video suggestion: watch the second half of this [video](https://www.youtube.com/watch?v=6iF8Xb7Z3wQ)


### Week 8 Learning outcomes:

- Able to use the Turtle package to create drawings (see methods below)
- Able to read and understand basic Turtle code to visualize its output
- Able to create a function 
- Able to create a function with parameters
- Able to call a function previously created in the program
- Able to call a function from a loop and use the loop variable as argument
- Able to color the turtle using turtle color names
- Able to color the turtle using color coded with RGB values as a 3-tuple with values for (red,green,blue)
- Able to identify the scope of a variable, especially in relation to function scope

### Week 8 Code Snippets

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

## Week 9 (Oct 28)

### Week 9 Readings

- Finishing Runestone Chapter 6
  - [6.6](https://runestone.academy/ns/books/published/thinkcspy/Functions/Functionscancallotherfunctions.html) and [6.7](https://runestone.academy/ns/books/published/thinkcspy/Functions/FlowofExecutionSummary.html)
- Snippet from Runestone Chapter 8 and 10
  - Read [8.11](https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/2DimensionalIterationImageProcessing.html), which is on the longer side, for intro to the theory of image processing. Then also read the very quick [10.24](https://runestone.academy/ns/books/published/thinkcspy/Lists/NestedLists.html) for review on nested lists. Also visit [10.8](https://runestone.academy/ns/books/published/thinkcspy/Lists/ListsareMutable.html) for a reminder about how "mutate" (i.e. change) lists
- Runestone chapter 5 on modules
  - Read [5.1](https://runestone.academy/ns/books/published/thinkcspy/PythonModules/modules.html) for explanation on Python modules. Note: We'll review the "need-to-know" modules in class.


### Week 9 Learning Outcomes:

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

### Week 9 Code Snippets

```python

def multiplier_100(a):
  return (a*100)

receive = multiplier_100(5)


i = 0
while i <10:
    i+=1
    # do something with i
```

## Week 10 (Nov 4)

### Week 10 Readings

- From Chapter 5 (generally, about Python Modules):
  - [5.1](https://runestone.academy/ns/books/published/thinkcspy/PythonModules/modules.html). Modules and Getting Help
  - [5.2](https://runestone.academy/ns/books/published/thinkcspy/PythonModules/MoreAboutUsingModules.html). More about using modules.
  - [5.3](https://runestone.academy/ns/books/published/thinkcspy/PythonModules/Themathmodule.html). The Math Module.
  - [5.5](https://runestone.academy/ns/books/published/thinkcspy/PythonModules/CreatingModules.html). Creating modules.
- From Chapter 8 (Image Processing):
  - [8.11](https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/2DimensionalIterationImageProcessing.html). Two-Dimensional Iteration: Image Processing
- From Chapter 10:
  - [10.8](https://runestone.academy/ns/books/published/thinkcspy/Lists/ListsareMutable.html). Lists are mutable.
  - [10.24](https://runestone.academy/ns/books/published/thinkcspy/Lists/NestedLists.html). Nested lists.

### Week 10 Learning Outcomes

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


### Week 10 Code Snippets

```
def my_func(a,b):
  return a < b

if  my_less_than(2,30):
     ..............

my_3d_list[0][10][4]

import cmpt120images
import my_custom_module
```


## Week 11 (Nov 11)

### Week 11 Readings
- Selected readings from Runestone Chapter 10:
  - [10.10](https://runestone.academy/runestone/books/published/thinkcspy/Lists/ObjectsandReferences.html). Objects and references.
  - [10.11](https://runestone.academy/runestone/books/published/thinkcspy/Lists/Aliasing.html)
  - [10.16](https://runestone.academy/runestone/books/published/thinkcspy/Lists/AppendversusConcatenate.html)
  - [10.19](https://runestone.academy/runestone/books/published/thinkcspy/Lists/UsingListsasParameters.html)
  - [10.22](https://runestone.academy/runestone/books/published/thinkcspy/Lists/FunctionsthatProduceLists.html)
- Selected readings from Runestone Chapter 16 on Recursion (We'll cover a lot in class!)
  - [16.1](https://runestone.academy/runestone/books/published/thinkcspy/IntroRecursion/WhatIsRecursion.html)
  - [16.3](https://runestone.academy/runestone/books/published/thinkcspy/IntroRecursion/TheThreeLawsofRecursion.html)
  - [16.5](https://runestone.academy/runestone/books/published/thinkcspy/IntroRecursion/intro-VisualizingRecursion.html)
  - [16.6](https://runestone.academy/runestone/books/published/thinkcspy/IntroRecursion/SierpinskiTriangle.html)

Optional readings (suggested to help with future CMPT courses):
- [10.12](https://runestone.academy/runestone/books/published/thinkcspy/Lists/CloningLists.html)
- [10.13](https://runestone.academy/runestone/books/published/thinkcspy/Lists/RepetitionandReferences.html)


### Week 11 Learning Outcomes

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

### Week 11 Code Snippets

```


mylist = [1,2,3]
mylistalias = mylist
mylist.append(4)
# mylist and mylistalias now have 4 elements

---
def changes_list(alist):
  alist[0] = 1

origlist = ["a","b","c"]
changes_list(origlist)
# origlist is now changed

---
```



## Week 12 (Nov 18)

### Week 12 Readings

- [16.2](https://runestone.academy/ns/books/published/thinkcspy/IntroRecursion/CalculatingtheSumofaListofNumbers.html) for an example of using recursion
- [16.4](https://runestone.academy/ns/books/published/thinkcspy/IntroRecursion/ConvertinganIntegertoaStringinAnyBase.html) for another example of recursion with strings

We'll also go back to Chapter 6 and read:

- [6.2](https://runestone.academy/ns/books/published/pythonds/SortSearch/searching.html)
- [6.3](https://runestone.academy/ns/books/published/pythonds/SortSearch/TheSequentialSearch.html)
- [6.4](https://runestone.academy/ns/books/published/pythonds/SortSearch/TheBinarySearch.html)




### Week 12 Learning Outcomes

- More recursion
  - Able to write code that can produce the sum of a list using recursion
  - Able to write code that can reverse a string using recursion 
  - Able to write a recursive or iterative function to check if a string is a palindrome

- Search!
  - Able to write a linear search function with various return types (Boolean using for/while, index of unique found element, indices of all found elements)
  - Able to recognize a binary search and produce code for it
  - Able to produce the code for a recursive binary search

Code snippets are getting longer. See lecture slides.

## Week 13

### Week 13 Readings

- [6.6](https://runestone.academy/ns/books/published/pythonds/SortSearch/sorting.html)
- [6.8](https://runestone.academy/ns/books/published/pythonds/SortSearch/TheSelectionSort.html)
- [6.11](https://runestone.academy/ns/books/published/pythonds/SortSearch/TheMergeSort.html)

Now we'll once again go back in Chapter numbers a bit to get some of the theory of motivation for algorithm analysis
- [3.2](https://runestone.academy/ns/books/published/pythonds/AlgorithmAnalysis/WhatIsAlgorithmAnalysis.html)
- [3.3](https://runestone.academy/ns/books/published/pythonds/AlgorithmAnalysis/BigONotation.html)


### Week 13 Learning Outcomes


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

That's it! We did hit a lot of learning outcomes. We'll review them all in the final week.

