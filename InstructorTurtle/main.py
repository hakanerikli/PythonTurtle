import math
import turtle
from random import random

myturtle = turtle.Turtle()
screen = turtle.Screen()
myturtle.hideturtle()
# screen.setup(500,500)
screen.bgcolor("light blue")
screen.title("Instructor's Turtle")
FONT = ("Verdana", 12, "normal")
grid_size = 10

# turtle list
turtle_list = []

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
        # t.hideturtle()
        t.penup()
        t.color("green")
        t.shape("turtle")
        t.shapesize(2,2)
        t.goto(x*grid_size,y*grid_size)
        turtle_list.append(t)

x_coordinates = [-20, -10, 0, 10,20]
y_coordinates = [20,10,0,-10]
def setup_turtles():
        for x in x_coordinates:
                for y in y_coordinates:
                        make_turtle(x,y)


# for i in range(20):
#         # turtle.hideturtle()
#         sc_y=turtle.window_height()
#         sc_y_start= (-sc_y/2 + sc_y*0.15) + (sc_y/5)*(i//5)
#         sc_x=turtle.window_width()
#         sc_x_start= (sc_x/2-sc_x/10) - (sc_x*0.2)*(i%5)
#         make_turtle(sc_x_start, sc_y_start)

def hide_turtles():
        for t in turtle_list:
                t.hideturtle()

turtle.tracer(0)
score_turtle_setup()
countdown_turtle_setup()
setup_turtles()
hide_turtles()
turtle.tracer(1)

random


turtle.mainloop()
