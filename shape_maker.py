import turtle

# Initializing the turtle
t = turtle.Turtle()


def main():
    #    while True:

    try:
        num_sides = int(
            input("How many sides do you want your shape to have? "))
        #break
    except ValueError:
        print("Invalid input. Please enter a valid number for the sides.")

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
    


if __name__ == "__main__":
    main()