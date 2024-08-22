import turtle
import random

# Initializing the turtle
t = turtle.Turtle()
screen = turtle.Screen()

def draw(num_sides):
    color_choice = input("What color do you want your shape to be? ")
    print(f"You chose to have a {color_choice} shape with {num_sides} sides.")

    # Set turtle color and begin filling the shape
    t.fillcolor(color_choice)

    # Randomize position for the shape
    x_pos = random.randint(-200, 200)
    y_pos = random.randint(-200, 200)

    # Move turtle to the random position
    t.penup()
    t.goto(x_pos, y_pos)
    t.pendown()

    t.begin_fill()
    for i in range(num_sides):
        t.forward(50)
        t.left(360 / num_sides)
    t.end_fill()

    # Write the message
    t.penup()
    t.setpos(-100, -200)  # Adjust position to display text below the screen
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