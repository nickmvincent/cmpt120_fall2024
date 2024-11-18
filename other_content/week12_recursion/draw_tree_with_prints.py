import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Recursive Tree")

# Set up the turtle
tree_turtle = turtle.Turtle()
# tree_turtle.shape("turtle")
tree_turtle.speed("fastest")  # Speed up the drawing

# Recursive function to draw a fractal tree with visualization of recursion stack
def draw_tree(turtle, branch_length, angle, depth=0):
    indent = "  " * depth  # Increase indentation for each recursion level
    print(f"{indent}draw_tree(depth={depth}, branch_length={branch_length})")

    if branch_length > 5:  # Base case: stop when the branch is too short
        # Draw the main branch
        turtle.forward(branch_length)
        
        # Right branch
        turtle.right(angle)
        print(f"{indent}  Right branch at depth={depth + 1}")
        draw_tree(turtle, branch_length - 15, angle, depth + 1)
        
        # Left branch
        turtle.left(2 * angle)
        print(f"{indent}  Left branch at depth={depth + 1}")
        draw_tree(turtle, branch_length - 15, angle, depth + 1)
        
        # Reset position and angle for next branch
        turtle.right(angle)
        turtle.backward(branch_length)

    print(f"{indent}Returning from depth={depth}")

# Initial position
tree_turtle.left(90)  # Point the turtle upwards
tree_turtle.penup()
tree_turtle.goto(0, -200)  # Move to starting position
tree_turtle.pendown()

# Draw the tree
draw_tree(tree_turtle, branch_length=40, angle=20)

# Finish up
turtle.done()
