import turtle

def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.left(90)

def draw_triangles(some_turtle):
	for i in range(1,4):
		some_turtle.forward(100)
		some_turtle.left(120)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	# create brad -Draw squares
	brad=turtle.Turtle()
	brad.shape("turtle")
	brad.speed(8)
	brad.color("green")
	brad.left(40)
	draw_square(brad)
	#  create david - draw cicle
	david= turtle.Turtle()
	david.shape("turtle")
	david.speed(9)
	david.color("orange")
	david.circle(80)
	#create pedro - draw triangles
	pedro=turtle.Turtle()
	pedro.shape("turtle")
	pedro.speed(8)
	pedro.color("white")
	pedro.left(40)
	draw_triangles(pedro)


	window.exitonclick()
draw_art()
