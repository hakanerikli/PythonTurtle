import turtle
statusList=("Not Started", "Started", "Game Over")
gameStatus=0
turtle = turtle.Turtle()
#turtle.hideturtle()
screen = turtle.screen
screen.onclick(lambda x,y: countdown(10))
screen.bgcolor("light green")
screen.title("Python Turtle Hakan")



image = "turtle.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
FONT = ('Arial', 20, 'normal')
turtle.setpos(0,250)
turtle.write("Click Screen", align='center' ,font=FONT)

canvas = screen.getcanvas()
screen.onscreenclick(lambda x,y: getMouseClickCoor(x,y))
def getMouseClickCoor(x,y):
    global gameStatus
    if gameStatus!= 1:
        gameStatus = 1
        countdown(10)

    tpos= turtle.pos()
    clickpos= (x,y)
    diffx = tpos[0]-clickpos[0]
    diffy= tpos[1]-clickpos[1]
    if (diffx < 50 and diffx >-50 ) and (diffy<50 and diffy>-50):
        print(x,y, "Yeeyy")
    else:
        print(diffx, diffy, ":((")

def countdown(time):
    screen.onclick(None)
    turtle.clear()

    if time > 0:
        turtle.write(time, align='center', font=FONT)
        screen.ontimer(lambda: countdown(time -1), 1000)
    else:
        turtle.write(statusList[2], align='center', font=FONT)
        screen.onclick(lambda x, y: countdown(10))
        global gameStatus
        gameStatus = 2






screen.mainloop()