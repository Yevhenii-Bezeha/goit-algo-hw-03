import turtle

def draw_koch_segment(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)
        t.right(120)
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)

def draw_snowflake(t, length, level):
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)

    # Prompt user for recursion level
    try:
        level = int(input("Enter recursion level (e.g., 3): "))
        if level < 0:
            print("Recursion level must be a non-negative integer.")
            return
    except ValueError:
        print("Please enter an integer.")
        return

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    draw_snowflake(t, 400, level)

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()
