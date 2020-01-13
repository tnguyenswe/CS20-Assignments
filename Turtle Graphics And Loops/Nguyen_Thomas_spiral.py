'''
Name: Thomas Nguyen
Date: 1/6/20
Professor: Henry Estrada
Assignment: Turtle Graphics/Loops
This program takes 3 inputs and creates an increasingly-sized shape based on your input.
'''

#Import turtle module
import turtle

#Gets user inputs for sides, lines, and size increase
sides = int(input("How many sides do you want the shape to have?: "))
lines = int(input("How many times do you want to spiral (total number of lines to draw)?: "))
increase = float(input("What percentage of increase do you want to use for each arm of the spiral?: "))

#Converts the increase into percentage
sizeincrease = increase/100

#Initialize the arm to be 10, set pen size to 2.
arm = int(10)
turtle.pensize(2)

#For loop to draw the necessary shapes.
for i in range(lines):
    turtle.forward(arm)
    turtle.right(360/sides)
    arm = arm + (arm*sizeincrease)

#Allows the user to exit upon clicking the turtle screen rather than automatically closing upon finishing the drawing.
turtle.exitonclick()