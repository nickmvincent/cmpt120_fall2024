import turtle
import random

# # Create a turtle object named pet
pen = turtle.Turtle()

# # Set the turtle's speed to the fastest
pen.speed(0)

# ---
# FILL ME IN HERE
# ---

def draw_rect(pen, color_for_rect, units_for_rect_width):
    # this function should draw a rectangle of the given color
    # pen should be the object instantiated as turtle.Turtle()
    # color "blue"
    pen.color(color_for_rect)
    for _ in range(4):
        pen.forward(units_for_rect_width)
        pen.left(90)

def get_rand_rgb():
    random_r = random.choice(range(0,256))
    random_g = random.choice(range(0,256))
    random_b = random.choice(range(0,256))
    return [random_r, random_g, random_b]

def draw_random_lines(num_lines):
    for _ in range(num_lines):
        random_r, random_g, random_b = get_rand_rgb()
        pen.color(random_r, random_g, random_b)
        pen.penup()
        pen.goto(random.randint(-200, 200), random.randint(-200, 200))
        pen.pendown()
        pen.setheading(random.randint(0, 360))
        pen.forward(random.randint(50, 200))

turtle.colormode(255)


# This loop draws 20 random colored rectangles

def draw_n_rectangles(n):
    for _ in range(n):
        random_x_coordinate = random.choice(range(-300, 300))
        random_y_coordinate = random.choice(range(-300, 300))
        # NMVG edited this to use a function on Oct 31...
        random_r, random_g, random_b = get_rand_rgb()
        # rand_color = random.choice(['red', 'green', 'blue'])
        pen.penup()
        pen.goto(random_x_coordinate, random_y_coordinate)
        pen.pendown()
        draw_rect(pen, [random_r, random_g, random_b], 150)


draw_n_rectangles(20)
draw_random_lines(10)



# ---
pen.hideturtle()

turtle.done()