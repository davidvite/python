
import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("blue")

	brad = turtle.Turtle()
	turtle.shape("turtle")
	turtle.speed(9)
	turtle.color("red","green")
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)

	window.exitonclick()
draw_square()