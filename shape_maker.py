import turtle
import random
import math

# Initialize the turtle
t = turtle.Turtle()
screen = turtle.Screen()

def draw(num_sides):
    # Ask the user for the background color and set it
    background_color = input("What color do you want the background to be? ")
    screen.bgcolor(background_color)

    # Ask the user for the color and size of the shape
    color_choice = input("What color do you want your shape to be? ")
    print(f"You chose to have a {color_choice} shape with {num_sides} sides.")

    # Ask the user for size on a scale from 1 to 5
    while True:
        size_choice = input("On a scale from 1-5, how big would you like your shape to be? ")
        if size_choice.isdigit() and 1 <= int(size_choice) <= 5:
            size_choice = int(size_choice)
            break
        else:
            print("Please enter a valid size between 1 and 5.")

    # Set turtle color and begin filling the shape
    t.fillcolor(color_choice)

    # Get screen width and height
    screen_width = screen.window_width() // 2
    screen_height = screen.window_height() // 2

    # Set a larger base side length and scale it by the user's choice
    base_side_length = 50  # Increased base side length for larger shapes
    side_length = base_side_length * size_choice  # Scale based on user's input

    # Calculate the radius of the bounding circle (from center to a vertex)
    shape_radius = side_length / (2 * math.sin(math.pi / num_sides))

    # Randomize position but ensure shape stays within the screen
    x_pos = random.randint(-screen_width + int(shape_radius), screen_width - int(shape_radius))
    y_pos = random.randint(-screen_height + int(shape_radius), screen_height - int(shape_radius))

    # Move turtle to the random position
    t.penup()
    t.goto(x_pos, y_pos)
    t.pendown()

    # Draw the shape
    t.begin_fill()
    for i in range(num_sides):
        t.forward(side_length)
        t.left(360 / num_sides)
    t.end_fill()

    # Move the turtle to write the message below the shape
    t.penup()
    text_y_pos = y_pos - (shape_radius + 40)  # Increased offset to position the text below the larger shape
    text_y_pos = max(text_y_pos, -screen_height + 60)  # Ensure text stays within screen bounds
    t.goto(-screen_width + 40, text_y_pos)
    t.pendown()

    # Write the message with larger font
    t.write(f"A {color_choice} shape with {num_sides} sides and size {size_choice}.", font=("Arial", 18, "normal"))

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