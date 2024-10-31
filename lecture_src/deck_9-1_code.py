def my_math_function(a, b):
    return a * 2 + b * 3

def greet(name):
    message = f"Hello, {name}!"
    return message

def power(base, exponent=2):
    return base ** exponent

# Try to get this code to run by ONLY ADDING things

# give this a default argument
def f1(x):
    return x * 2

# takes multiple arguments: pass then below
def f2(a, b):
    return a + b

# f3 takes no arguments
def f3():  # No arguments
    return "Hello!"

def f4(value):  # Single argument
    if value > 0:
        return "Positive"
    else:
        return "Non-positive"


successes = []
try:
    r1 = f1()
    successes.append("f1 works")
except Exception as e:
    print(e)

try:
    r2 = f2()
    successes.append("f2 works")

except Exception as e:
    print(e)

try:
    r3 = f3("a")
    successes.append("f3 works")

except Exception as e:
    print(e)

try:
    r4 = f4()
    successes.append("f4 works")

except Exception as e:
    print(e)

for success in successes:
    print(success)


import turtle

# Create a turtle object named pen
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed

# Draw a triangle with stamps at each vertex
for i in range(3):
    pen.forward(50)
    pen.stamp()
    pen.left(120)

# Re-position pen for the next part of the drawing
pen.penup()
pen.goto(100, -100)
pen.pendown()

# Draw a square with blue color
pen.color("blue")
for _ in range(4):
    pen.forward(100)
    pen.right(90)

# Starter kit 5-line snippet for turtle art
import turtle as t
import random
def main():
    t.forward(100)
main()

import random

def draw_random_lines(num_lines):
    for _ in range(num_lines):
        t.color(random.random(), random.random(), random.random())
        t.penup()
        t.goto(random.randint(-200, 200), random.randint(-200, 200))
        t.pendown()
        t.setheading(random.randint(0, 360))
        t.forward(random.randint(50, 200))

# Use RGB colors for more variety
turtle.colormode(255)
mycolor = (255, 0, 120)
pen.color(mycolor)
for _ in range(4):
    pen.forward(100)
    pen.right(90)

# Hide the turtle at the end
pen.hideturtle()
turtle.done()

