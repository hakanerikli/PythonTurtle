import turtle
import random
import math

scorePoint = 0
gameStatus = 0

turtle1 = turtle.Turtle()
turtle1.penup()
screen = turtle1.screen
scoreTurtle = turtle.Turtle()
scoreScreen = scoreTurtle.screen
timeTurtle = turtle.Turtle()
timeScreen = timeTurtle.screen
scoreTurtle.hideturtle()
timeTurtle.hideturtle()
scoreTurtle.penup()
timeTurtle.penup()
scoreTurtle.setpos(0, 350)
timeTurtle.setpos(0, 300)

screen.bgcolor("light green")
screen.title("Python Turtle Hakan")
screen.onclick(lambda x, y: countdown(10))

image = "turtle.gif"
screen.addshape(image)
turtle1.shape(image)
turtle1.penup()
FONT = ('Arial', 20, 'normal')


def caption(score, time):
    scoreTurtle.clear()
    timeTurtle.clear()

    global scorePoint
    if scorePoint != score:
        score = "Score: " + score
        scoreTurtle.write(score, move=False, align='center', font=FONT)

    timeTurtle.write(time, move=False, align='center', font=FONT)


def randomcoords():
    x = random.randint(-350,350)
    y = random.randint(-350,350)
    turtle1.hideturtle()
    turtle1.goto(x, y)
    turtle1.showturtle()


caption("0", "Click to Start")


def countdown(time):
    global scorePoint
    turtle1.clear()

    def get_mouse_click_coor(x, y):
        tpos = turtle1.pos()
        clickpos = (x, y)
        diffx = tpos[0] - clickpos[0]
        diffy = tpos[1] - clickpos[1]
        if (15 > diffx > -15) and (25 > diffy > -25):
            print(x, y, "Yeeyy")
            randomcoords()
            global scorePoint
            scorePoint += 1
        else:
            print(diffx, diffy, ":((")
            randomcoords()

    screen.onclick(None)
    screen.onscreenclick(lambda x, y: get_mouse_click_coor(x, y))
    timeTurtle.clear()

    if time > 0:
        caption(str(scorePoint), str(math.floor(time)))
        randomcoords()
        screen.ontimer(lambda: countdown(time - 0.5), 500)
    else:
        caption(str(scorePoint), "Game Over")
        screen.onclick(lambda x, y: countdown(10))
        scorePoint = 0
        turtle1.hideturtle()
        turtle1.setpos(0,0)
        turtle1.write("Click to Start", move=False, align='center', font=FONT)


screen.mainloop()
