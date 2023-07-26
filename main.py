import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("green")
drawing_board.title("Python Turtle")

#create a square
turtle_instance = turtle.Turtle()
'''
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)
turtle_instance.left(90)
turtle_instance.forward(100)'''
'''for i in range(4):
    turtle_instance.left(90)
    turtle_instance.forward(100)
'''

#drawing a star
for i in range(5):
    turtle_instance.left(72)
    turtle_instance.forward(100)
    turtle_instance.right(144)
    turtle_instance.forward(100)

turtle.done()