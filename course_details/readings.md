# CMPT 120 Readings Guide

For pre-midterm readings and learning outcomes, see Canvas Learning Outcomes / Readings entries and the pre-midterm slide deck.

## Week 7

During Week 7, you read from Runestone:
- [9.6](https://runestone.academy/ns/books/published/thinkcspy/Strings/Length.html), - [9.7](https://runestone.academy/ns/books/published/thinkcspy/Strings/StringsareImmutable.html)
- [9.11](https://runestone.academy/ns/books/published/thinkcspy/Strings/TraversalandtheforLoopByIndex.html)
- Chapter 1 from Gaddis, Introduction to Computers and Programming

After these readings and corresponding lectures, you should feel comfortable with the following topics:

- Knows what a bit represents in a computer
- Convert a given number of bytes (or kb, mb) to bits
- Convert binary <> decimal
- Understand the goal of hexadecimal
- Know that binary numbers convert to hexadecimal by grouping of 4 bits
- Know the purpose of ASCII
- Know relationship of Unicode to ASCII
- Know how to store RGB numbers (3 byte aka 24 bits aka 6 hexadecimal digits)


## Week 8

During week 8, you should read

- Runestone Chapter 4
  - Read [4.1](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/intro-HelloLittleTurtles.html), [4.2](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/OurFirstTurtleProgram.html), [4.3](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/InstancesAHerdofTurtles.html), [4.6](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/IterationSimplifiesourTurtleProgram.html), [4.7](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/TherangeFunction.html), [4.8](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/AFewMoreturtleMethodsandObservations.html), and [4.9](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/SummaryofTurtleMethods.html).
  - You can go quickly through these readings: we will cover the content directly in lecture.
  - In 4.4. and 4.5, you've already seen the for loop. revisit them if you want to review.
- Start Runestone Chapter 6
  - Read [6.1](https://runestone.academy/runestone/books/published/thinkcspy/Functions/functions.html), 6.2, and 6.4 and [6.11](https://runestone.academy/ns/books/published/thinkcspy/Functions/ATurtleBarChart.html). You can skip 6.3 for now (though if you are considering software engineering, you want to just read it now!)
- Read about while loops from Chapter 8
  - Read [8.3](https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/ThewhileStatement.html) and [8.8](https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/SentinelValuesAndValidation.html)
  - Option video suggestion: watch the second half of this [video](https://www.youtube.com/watch?v=6iF8Xb7Z3wQ)


After doing these readings, you should feel comfortable:
- Able to use the Turtle package to create drawings (see methods below)
- Able to read and understand basic Turtle code to visualize its output
- Able to create a function 
- Able to create a function with parameters
- Able to call a function previously created in the program
- Able to call a function from a loop and use the loop variable as argument
- Able to color the turtle using turtle color names
- Able to color the turtle using color coded with RGB values as a 3-tuple with values for (red,green,blue)
- Able to identify the scope of a variable, especially in relation to function scope

You should be comfortable with the following code snippets:

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


## Week 9

During Week 9, you should read the rest of Chapter 6. Then, we'll read about Image Processing

- Finishing Runestone Chapter 6
  - [6.6](https://runestone.academy/ns/books/published/thinkcspy/Functions/Functionscancallotherfunctions.html) and [6.7](https://runestone.academy/ns/books/published/thinkcspy/Functions/FlowofExecutionSummary.html)
- Snippet from Runestone Chapter 8 and 10
  - Read [8.11](https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/2DimensionalIterationImageProcessing.html), which is on the longer side, for intro to the theory of image processing. Then also read the very quick [10.24](https://runestone.academy/ns/books/published/thinkcspy/Lists/NestedLists.html) for review on nested lists. Also visit [10.8](https://runestone.academy/ns/books/published/thinkcspy/Lists/ListsareMutable.html) for a reminder about how "mutate" (i.e. change) lists
- Runestone chapter 5 on modules
  - Read [5.1](https://runestone.academy/ns/books/published/thinkcspy/PythonModules/modules.html) for explanation on Python modules. Continue reading the rest of chapter 5. We'll review the "need-to-know" modules in class.


After this week's readings and the lectures that follow, you should feel comfortable with:

- Able to create and use functions that return values ()
- Knows how to call a function so that the value returned from a function is received
- Knows that print() is different than return in a function
- Knows the effect that a return has if executed inside a loop (inside a function)
- Identifies cases when the value None is produced when calling a function


- Able to identify when a while loop would be appropriate compared to a for loop
- Able to create a valid while loop with a sentinel (control variable) 
- Able to create a valid while loop with multiple control variables
- Able to use a while loop to validate user input

You should understand the following code snippets:

```python

def multiplier_100(a):
  return (a*100)

receive = multiplier_100(5)


i = 0
while i <10:
    i+=1
    # do something with i
```


## Week 10

During Week 10, please read:

- Selected readings from Runestone Chapter 10:
  - [10.10](https://runestone.academy/runestone/books/published/thinkcspy/Lists/ObjectsandReferences.html)
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


After this week's readings and the lectures that follow, you should feel comfortable with:

- Able to create and use a module containing one's own defined functions
- Knows how pixel colors are represented by RGB values 
- Knows how to pass global variables into local scope
- Knows to directly return the Boolean value evaluated from a Boolean expression in a function without using if statement in the function,  and call the function and use the returned Boolean value.
- Able to access and modify a 2D image in the form of a list of lists, containing RGB values in the form of a list
- Able to manipulate 2 dimensional lists, process a row, process a column, process a specific element
- Knows how to import and access the contents of packages and modules
- Knows how to import a module with a short name
- Able to read, show and save images using the 3Dlist representing an image as provided in the cmpt120images module 
- Able to extract and/or change the color as RGB and/or individual color components of a pixel using a 3DList representing an image  as provided in the cmpt120images module



## Week 11

During Week 11, please read

- [16.2](https://runestone.academy/ns/books/published/thinkcspy/IntroRecursion/CalculatingtheSumofaListofNumbers.html) for an example of using recursion
- [16.4](https://runestone.academy/ns/books/published/thinkcspy/IntroRecursion/ConvertinganIntegertoaStringinAnyBase.html) for another example of recursion with strings

We'll also go back to Chapter 6 and read:
- [6.2](https://runestone.academy/ns/books/published/pythonds/SortSearch/searching.html)
- [6.3](https://runestone.academy/ns/books/published/pythonds/SortSearch/TheSequentialSearch.html)
- [6.4](https://runestone.academy/ns/books/published/pythonds/SortSearch/TheBinarySearch.html)


## Week 12

During Week 12, please read:

- [6.6](https://runestone.academy/ns/books/published/pythonds/SortSearch/sorting.html)
- [6.8](https://runestone.academy/ns/books/published/pythonds/SortSearch/TheSelectionSort.html)
- [6.11](https://runestone.academy/ns/books/published/pythonds/SortSearch/TheMergeSort.html)

Now we'll once again go back in Chapter numbers a bit to get some of the theory of motivation for algorithm analysis
- [3.2](https://runestone.academy/ns/books/published/pythonds/AlgorithmAnalysis/WhatIsAlgorithmAnalysis.html)
- [3.3](https://runestone.academy/ns/books/published/pythonds/AlgorithmAnalysis/BigONotation.html)


