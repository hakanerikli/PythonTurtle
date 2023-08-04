import turtle

myturtle = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Instructor's Turtle")
FONT = ("Verdana", 50, "normal")

# MyTurtle
myturtle.penup()
myturtle.setpos(0, 200)
myturtle.write("Test", align="center", font=FONT)
myturtle.hideturtle()

# Score Turtle
score_turtle = turtle.Turtle()
score_turtle.color("dark blue")
score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

# Countdown Turtle
countdown_turtle = turtle.Turtle()
countdown_turtle.color("red")
countdown_turtle.write(arg="Time: 0", move=False, align="center", font=FONT)

turtle.mainloop()
