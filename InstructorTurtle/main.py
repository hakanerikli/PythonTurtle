import turtle
import random
import time

myturtle = turtle.Turtle()
screen = turtle.Screen()
myturtle.hideturtle()
# screen.setup(500,500)
screen.bgcolor("light blue")
screen.title("Instructor's Turtle")
FONT = ("Verdana", 12, "normal")
grid_size = 10
score = 0
game_over = True
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
    def handle_click(x, y):
        t.hideturtle()
        global score
        global game_over
        score += 1
        print(x, y)


    t.onclick(handle_click)
    t.penup()
    t.color("green")
    t.shape("turtle")
    t.shapesize(2, 2)
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)


x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [20, 10, 0, -10]


def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)


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


def show_turtles_randomly():
    random.choice(turtle_list).showturtle()


def countdown(tg):
    hide_turtles()
    global score, game_over
    while tg:
        mins, secs = divmod(tg, 60)
        timer = '{:02d}'.format(secs)
        print(timer)
        show_turtles_randomly()
        time.sleep(0.5)
        tg -= 1
        time_score(timer,score)
        hide_turtles()
        game_over = False
    else:
        time_score("Time is over",score)
        myturtle.write("Press Space to Start new game!", move=False, align="center", font=FONT)
        game_over = True

def time_score(time, score):
    turtle.tracer(0)
    text = "Score: " + str(score)
    score_turtle.clear()
    score_turtle.write(text, move=False, align="center", font=FONT)
    countdown_turtle.clear()
    countdown_turtle.write(time, move=False, align="center", font=FONT)
    turtle.tracer(1)


def start_turtle():
    myturtle.clear()
    score_turtle.clear()
    countdown_turtle.clear()
    global score, game_over
    tg = 10
    turtle.tracer(0)
    score_turtle_setup()
    countdown_turtle_setup()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    turtle.tracer(1)
    countdown(tg)
    score = 0
    game_over = False




# start_turtle()
if game_over == True:
    turtle.onkeypress(start_turtle, "space")
myturtle.write("Press Space to Start new game!", move=False, align="center", font=FONT)
turtle.listen()

turtle.mainloop()