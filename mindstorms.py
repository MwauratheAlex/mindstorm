import turtle

def draw_square(some_turtle):
	for i in range(4):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("cyan")

	#create turtle brad - Draws square
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed(2)

	for i in range(36):
		draw_square(brad)
		brad.right(10)
		
		

	#create turtle angie - Draws circle
	#angie = turtle.Turtle()
	#angie.shape("arrow")
	#angie.color("blue")
	#angie.circle(100)

	window.exitonclick()

draw_art()

