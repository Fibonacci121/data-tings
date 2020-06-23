import numpy
from numpy import *
import turtle
from random import *

print("""
	"""*15)

turtle.setup(500,500)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()


xcoords = []
ycoords = []

fir_quad = 0
sec_quad = 0
third_quad = 0

#i actually spelled that wrong...
forth_quad = 0
middles = 0

#colors = ['red','blue','green']

#main loop that continuously runs the program a set number of times

runs = 0

for i in range(100000):

	x = randint(-250,250)
	y = randint(-250,250)
	turtle.bgcolor("#abf381")
	turtle.speed(4)

	turtle.delay(7)
	runs += 1


	if x >= 0 and y >= 0 :

		quadA = turtle.Turtle()
		quadB = turtle.Turtle()
		quadC = turtle.Turtle()
		quadD = turtle.Turtle()
		quadA.goto(300,0)
		quadB.goto(-300,0)
		quadC.goto(0,-500)
		quadD.goto(0,500)

		turtle.pencolor("blue")
		turtle.dot()
		fir_quad += 1
		turtle.goto(x,y)
		turtle.write(str(x) + "," + str(y), True, align="center")

	if x < 0 and y >= 0 :

		quadA = turtle.Turtle()
		quadB = turtle.Turtle()
		quadC = turtle.Turtle()
		quadD = turtle.Turtle()
		quadA.goto(300,0)
		quadB.goto(-300,0)
		quadC.goto(0,-500)
		quadD.goto(0,500)

		turtle.pencolor("red")
		turtle.dot()
		sec_quad += 1
		turtle.goto(x,y)
		#turtle.write("Home = ", True, align="center")
		turtle.write(str(x) + "," + str(y), True, align="center")

	if x < 0 and y < 0 :


		quadA = turtle.Turtle()
		quadB = turtle.Turtle()
		quadC = turtle.Turtle()
		quadD = turtle.Turtle()
		
		quadA.goto(300,0)
		quadB.goto(-300,0)
		quadC.goto(0,-500)
		quadD.goto(0,500)

		turtle.pencolor("green")
		turtle.dot()
		third_quad += 1
		turtle.goto(x,y)
		#turtle.write("Home = ", True, align="center")
		turtle.write(str(x) + "," + str(y), True, align="center")

	if x >= 0 and y < 0 :


		quadA = turtle.Turtle()
		quadB = turtle.Turtle()
		quadC = turtle.Turtle()
		quadD = turtle.Turtle()
		quadA.goto(300,0)
		quadB.goto(-300,0)
		quadC.goto(0,-500)
		quadD.goto(0,500)

		turtle.pencolor("black")
		turtle.dot()
		forth_quad += 1
		turtle.goto(x,y)
		#turtle.write("Henwo", 20,20)
		turtle.write(str(x) + "," + str(y) ,True, align="center")
		#turtle.write("Home = ", True, align="center")

	if x == 0 and y == 0 :


		quadA = turtle.Turtle()
		quadB = turtle.Turtle()
		quadC = turtle.Turtle()
		quadD = turtle.Turtle()
		quadA.goto(300,0)
		quadB.goto(-300,0)
		quadC.goto(0,-500)
		quadD.goto(0,500)


		turtle.pencolor("black")
		turtle.dot()
		middles += 1
		turtle.goto(x,y)
		#turtle.write("Home = ", True, align="center")
		turtle.write(str(x) + "," + str(y) ,True, align="center")

#Adding names and points to each quadrant

	quadatext = turtle.Turtle()
	quadbtext = turtle.Turtle()
	quadctext = turtle.Turtle()
	quaddtext = turtle.Turtle()

	quadatext.hideturtle()
	quadbtext.hideturtle()
	quadctext.hideturtle()
	quaddtext.hideturtle()
	#turtle.penup()

	quadatext.goto(125,125)
	quadatext.write("1st quadrant", True, align="center")
	quadbtext.goto(-125,125)
	quadbtext.write("2nd quadrant", True, align="center")
	quadctext.goto(-125,-125)
	quadctext.write("3rd qaudrant", True, align="center")
	quaddtext.goto(125 ,-125)
	quaddtext.write("4th quadrant", True, align="center")

	for i in range(7):

		turtle.right(90)
	
	xcoords.append(str(x))
	ycoords.append(str(y))

	print("x : " + str(x))
	print("y : " + str(y))
	print("------runs = %s-------" %runs)


	turtle.clearscreen()

	
#printing outputs


print("There were " + str(fir_quad) + " points in the 1st quadrant" )
print("There were " + str(sec_quad) + " points in the 2nd quadrant" )
print("There were " + str(third_quad) + " points in the 3rd quadrant" )
print("There were " + str(forth_quad) + " points in the 4th quadrant" )
print("There were " + str(middles) + " points on the + of the coord plane")

turtle.exitonclick()
print()
print()
print()