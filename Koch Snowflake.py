import turtle
t = turtle.Turtle()
t.color("cyan")
turtle.Screen().bgcolor("white")
t.fillcolor("cyan")

def koch_curve(order, length):
    global t
    if order == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(order - 1, length)
        t.left(60)
        koch_curve( order - 1, length)
        t.right(120)
        koch_curve(order - 1, length)
        t.left(60)
        koch_curve( order - 1, length)

def koch_snowflake( order, length):
    global t
    for _ in range(3):
        koch_curve(order, length)
        t.right(120)


t.speed(0)
t.penup()
t.goto(-150, 100)  # Move to a starting position
t.pendown()
t.begin_fill()
koch_snowflake( 4, 300)  # Calling the function
t.end_fill()

'''t.right(30)
t.color("white")
#347
koch_curve(4, 347)
t.left(180)
koch_curve(4, 347)
'''
turtle.mainloop()