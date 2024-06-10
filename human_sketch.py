import turtle

def draw_circle(t, radius):
    t.circle(radius)

def draw_line(t, start, end):
    t.penup()
    t.goto(start)
    t.pendown()
    t.goto(end)

def draw_human():
    screen = turtle.Screen()
    screen.title("Human Sketch")

    t = turtle.Turtle()
    t.speed(2)

    # Draw head
    t.penup()
    t.goto(0, -50)
    t.pendown()
    draw_circle(t, 50)

    # Draw body
    draw_line(t, (0, -50), (0, -200))

    # Draw left arm
    draw_line(t, (0, -100), (-50, -150))

    # Draw right arm
    draw_line(t, (0, -100), (50, -150))

    # Draw left leg
    draw_line(t, (0, -200), (-50, -300))

    # Draw right leg
    draw_line(t, (0, -200), (50, -300))

    # Hide turtle
    t.hideturtle()

    screen.mainloop()

if __name__ == "__main__":
    draw_human()
