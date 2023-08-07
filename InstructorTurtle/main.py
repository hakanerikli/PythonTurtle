import math
import turtle

myturtle = turtle.Turtle()
screen = turtle.Screen()
myturtle.hideturtle()
# screen.setup(500,500)
screen.bgcolor("light blue")
screen.title("Instructor's Turtle")
FONT = ("Verdana", 12, "normal")
grid_size = 15


# MyTurtle
myturtle.hideturtle()
myturtle.penup()
# myturtle.setpos(0, 200)
# myturtle.write("Test", align="center", font=FONT)



score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
score_turtle.hideturtle()
countdown_turtle.hideturtle()

# Score Turtle
def score_turtle_setup():
    score_turtle.color("dark blue")
    score_turtle.penup()
    score_turtle.setpos(0, turtle.window_height() * 0.45)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

# Countdown Turtle
def countdown_turtle_setup():
        countdown_turtle.color("red")
        countdown_turtle.penup()
        countdown_turtle.setpos(0, turtle.window_height() * 0.42)
        countdown_turtle.write(arg="Time: 0", move=False, align="center", font=FONT)

def make_turtle(x, y):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.color("green")
        t.shape("turtle")
        t.shapesize(3,3)
        t.goto(x,y)

for i in range(20):
        turtle.hideturtle()
        sc_y=turtle.window_height()
        sc_y_start= (-sc_y/2 + sc_y*0.2) + (sc_y/5)*(i//5)
        sc_x=turtle.window_width()
        sc_x_start= (sc_x/2-sc_x/10) - (sc_x/5)*(i%5)
        make_turtle(sc_x_start, sc_y_start)

score_turtle_setup()
countdown_turtle_setup()



turtle.mainloop()
