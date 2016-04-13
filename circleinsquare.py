import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.left(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	# create brad -Draw squares
	brad=turtle.Turtle()
	brad.shape("turtle")
	brad.speed(8)
	brad.color("green")
	for i in range(1,37):
		brad.left(10)
		draw_square(brad)



	window.exitonclick()
draw_art()