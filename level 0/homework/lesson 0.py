from turtle import *

#we want to paint a house


width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door 


forward(70)
left(90)
forward(120)  # height of the door
right(90)
forward(60)
right(90)
forward(120)


penup()
goto(200, 200)

pendown()

forward(20)
right(150)
forward(200)
left(120)
forward(200)


exitonclick()