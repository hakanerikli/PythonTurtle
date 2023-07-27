# shrinking square
import turtle
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("orange")
turtle_screen.title("Turtle Python")
turtle_instance = turtle.Turtle()
# turtle_instance.color("blue")

def shrinkingSquare(size, num):
    for i in range(num):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size -=10



shrinkingSquare(200,12)

turtle.done()