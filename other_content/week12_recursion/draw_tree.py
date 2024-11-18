import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Recursive Tree")

# Set up the turtle
tree_turtle = turtle.Turtle()
#tree_turtle.shape("turtle")
tree_turtle.speed("fastest")  # Speed up the drawing

# Recursive function to draw a fractal tree
def draw_tree(turtle, branch_length, angle):
    if branch_length > 5:  # Base case: stop when the branch is too short
        # Draw the main branch
        turtle.forward(branch_length)
        
        # Right branch
        turtle.right(angle)
        draw_tree(turtle, branch_length - 15, angle)
        
        # Left branch
        turtle.left(2 * angle)
        draw_tree(turtle, branch_length - 15, angle)
        
        # Reset position and angle for next branch
        turtle.right(angle)
        turtle.backward(branch_length)

# Initial position
tree_turtle.left(90)  # Point the turtle upwards
tree_turtle.penup()
tree_turtle.goto(0, -200)  # Move to starting position
tree_turtle.pendown()

# Draw the tree
draw_tree(tree_turtle, branch_length=100, angle=20)

# Finish up
turtle.done()
