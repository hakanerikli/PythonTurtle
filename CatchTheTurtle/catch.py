import turtle,random
def randomCoords():
    x= (random.random())*400
    y= (random.random())*400
    print(x,y)
    return x,y

scorePoint=0

'''def caption(ypos,score):
    turtle.hideturtle()
    turtle.setpos(0, ypos)
    score= "Score: "+score
    turtle.write(score, move=False, align='center', font=FONT)
    turtle.showturtle()'''

def caption(score,time):
    scoreTurtle.hideturtle()
    timeTurtle.hideturtle()
    scoreTurtle.clear()
    timeTurtle.clear()
    scoreTurtle.penup()
    timeTurtle.penup()

    scoreTurtle.setpos(0,350)

    global scorePoint
    if scorePoint != score:
        score= "Score: "+score
        scoreTurtle.write(score, move=False, align='center', font=FONT)

    timeTurtle.setpos(0, 300)
    timeTurtle.write(time, move=False, align='center', font=FONT)

coords= randomCoords()
gameStatus=0


turtle1 = turtle.Turtle()
turtle1.penup()
screen = turtle1.screen
scoreTurtle = turtle.Turtle()
scoreScreen = scoreTurtle.screen
timeTurtle = turtle.Turtle()
timeScreen = timeTurtle.screen

print(coords)

screen.onclick(lambda x,y: countdown(10))
screen.bgcolor("light green")
screen.title("Python Turtle Hakan")

image = "turtle.gif"
screen.addshape(image)
turtle1.shape(image)
turtle1.penup()
FONT = ('Arial', 20, 'normal')
caption("0",0)
turtle1.goto(0,0)

canvas = screen.getcanvas()





def countdown(time):
    def getMouseClickCoor(x, y):
        tpos = turtle1.pos()
        clickpos = (x, y)
        diffx = tpos[0] - clickpos[0]
        diffy = tpos[1] - clickpos[1]
        if (diffx < 30 and diffx > -30) and (diffy < 50 and diffy > -50):
            print(x, y, "Yeeyy")
            turtle1.goto(randomCoords())
            global scorePoint
            scorePoint += 1
        else:
            print(diffx, diffy, ":((")
    screen.onclick(None)
    screen.onscreenclick(lambda x, y: getMouseClickCoor(x, y))
    timeTurtle.clear()
    global scorePoint

    if time > 0:
        caption(str(scorePoint),str(time))
        screen.ontimer(lambda: countdown(time -1), 1000)
    else:
        caption(str(scorePoint),"Game Over")
        screen.onclick(lambda x, y: countdown(10))
        scorePoint=0




screen.mainloop()