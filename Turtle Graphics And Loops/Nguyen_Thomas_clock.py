'''
Name: Thomas Nguyen
Date: 1/6/20
Professor: Henry Estrada
Assignment: Turtle Graphics/Loops
This program creates a clock that is based on realtime.
'''

#Imports turtle and datetime modules.
import turtle
import datetime

#Makes the turtle go back to the center and sets the values for the squares to be drawn for the hour markers and center.
turtle.penup()
turtle.home()
turtle.shape('square')
turtle.stamp()
degree = 30

#For loop to mark the hours on the clock
for i in range(12):
    turtle.penup()
    turtle.forward(150)
    turtle.stamp()
    turtle.home()
    turtle.right(degree)
    degree = degree + 30

#Draws the circle.
turtle.hideturtle()
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.circle(150)

#Sets hour to realtime and calculates the angle of the hand.
hour = datetime.datetime.now().hour%12
minute = datetime.datetime.now().minute

hour_angle = (hour*30 + minute*.5)
minute_angle = (minute*6)

#Draws the hour hand.
turtle.penup()
turtle.goto(0,0)
turtle.setheading(90)
turtle.right(hour_angle)
turtle.pendown()
turtle.forward(100)

#Draws the minute hand
turtle.penup()
turtle.goto(0,0)
turtle.setheading(90)
turtle.right(minute_angle)
turtle.pendown()
turtle.forward(120)

#Allows the user to exit upon clicking the turtle screen rather than automatically closing upon finishing the drawing.
turtle.exitonclick()

