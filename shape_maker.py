import turtle


# Initializing the turtle
t = turtle.Turtle()


def draw(num_sides):

    color_choice = input("What color do you want your shape to be? ")
    print(f"You chose to have a {color_choice} shape with {num_sides} sides.")
    t.fillcolor(color_choice)
    t.begin_fill()

    for i in range(num_sides):
        t.forward(50)
        t.left(360 / num_sides)
    t.end_fill()

    t.hideturtle()
    t.screen.mainloop()


def main():
    run = True
    num_sides = input("How many sides do you want your shape to have? ")

    while run:
        if num_sides.isdigit():
            run = False
            draw(int(num_sides))
        
        else:
            num_sides = input("Invalid input. Please enter a valid number for the sides. ")  
            draw(int(num_sides))


if __name__ == "__main__":
    main()