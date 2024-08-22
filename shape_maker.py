import turtle
import random
import math

# Initialize the turtle
t = turtle.Turtle()
screen = turtle.Screen()

def draw(num_sides):
    color_choice = input("What color do you want your shape to be? ")
    print(f"You chose to have a {color_choice} shape with {num_sides} sides.")
    
    # Set turtle color and begin filling the shape
    t.fillcolor(color_choice)
    
    # Get screen width and height
    screen_width = screen.window_width() // 2
    screen_height = screen.window_height() // 2
    
    # Set side length for the polygon
    side_length = 50
    
    # Calculate the radius of the bounding circle (from center to a vertex)
    shape_radius = side_length / (2 * math.sin(math.pi / num_sides))
    
    # Randomize position but ensure shape stays within the screen
    x_pos = random.randint(-screen_width + int(shape_radius), screen_width - int(shape_radius))
    y_pos = random.randint(-screen_height + int(shape_radius), screen_height - int(shape_radius))
    
    # Move turtle to the random position
    t.penup()
    t.goto(x_pos, y_pos)
    t.pendown()

    t.begin_fill()
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360 / num_sides)
    t.end_fill()
    
    # Write the message
    t.penup()
    t.setpos(-screen_width + 20, -screen_height + 20)  # Adjust to display text in the bottom left
    t.pendown()
    t.write(f"A {color_choice} shape with {num_sides} sides.", font=("Arial", 16, "normal"))
    
    t.hideturtle()
    screen.mainloop()

def main():
    run = True
    num_sides = input("How many sides do you want your shape to have? ")

    while run:
        if num_sides.isdigit():
            run = False
            draw(int(num_sides))
        else:
            num_sides = input("Invalid input. Please enter a valid number for the sides.")  
            draw(int(num_sides))

if __name__ == "__main__":
    main()