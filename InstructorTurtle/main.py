import turtle

myturtle= turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("light blue")
screen.title("Instructor's Turtle")

FONT = ("Verdana", 50, "normal")
myturtle.setpos(0,200)
myturtle.write("Test", align="center",font=FONT)

turtle.mainloop()