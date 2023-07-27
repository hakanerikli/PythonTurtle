import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Python Turtle")

# drawing a square
'''
turtle_instance = turtle.Turtle()
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

# drawing a star
turtle_instance = turtle.Turtle()
for i in range(5):
    turtle_instance.left(72)
    turtle_instance.forward(200)
    turtle_instance.right(144)
    turtle_instance.forward(200)

# polygone drawing
'''
turtle_instance = turtle.Turtle()
num_sides = 5
angle = 360.0/ num_sides
side_length = 100
for i in range(num_sides):
    turtle_instance.right(angle*2)
    turtle_instance.forward(side_length)
'''

turtle.done()