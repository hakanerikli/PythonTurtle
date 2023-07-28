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

drawing_board.listen()
drawing_board.onkeypress(fun=turtle_forward, key="Up" )
drawing_board.onkeypress(fun=rotate_angle_left, key="Left" )
drawing_board.onkeypress(fun=rotate_angle_right, key="Right" )
drawing_board.onkey(fun=turtle_clear, key="d" )


turtle.mainloop()