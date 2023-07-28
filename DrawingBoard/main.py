import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()


def turtle_forward():
    turtle_instance.forward(10)

def rotate_angle_right():
    turtle_instance.right(30)

def rotate_angle_left():
    turtle_instance.left(30)

def turtle_clear():
    turtle_instance.clear()

penstate=True
def tpup():
    global penstate
    if penstate:
        turtle_instance.penup()
        penstate^=True
    else:
        turtle_instance.pendown()
        penstate^=True
def treset():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkeypress(fun=turtle_forward, key="Up" )
drawing_board.onkeypress(fun=rotate_angle_left, key="Left" )
drawing_board.onkeypress(fun=rotate_angle_right, key="Right" )
drawing_board.onkeypress(fun=turtle_clear, key="d" )
drawing_board.onkeypress(fun=tpup, key="space" )
drawing_board.onkeypress(fun=treset, key="r" )



turtle.mainloop()