'''
Name: Thomas Nguyen
Date: 1/6/20
Professor: Henry Estrada
Assignment: Variables and Calculations (2)
This program takes the latitude and day of the year and calculates the minutes of sunshine for the day.
'''
#Import math module
import math

#Gets input from user
latitude = float(input("Enter latitude in degrees: "))
day = float(input("Enter day of year (1-365): "))
#Calculates the latitude in radians instead of degrees.
latitudeinradians = math.radians(latitude)

#Calculates p - I broke it up into different variables for easier readability.
insideoftan = math.tan(.00860*(day-186))
insideofarctan = math.atan(0.9671396*insideoftan)
insideofcos = math.cos(0.2163108+ (2*insideofarctan))
p = math.asin(0.39795*insideofcos)

#Calculates d
numerator = math.sin(.01454)+math.sin(latitudeinradians)*math.sin(p)
denominator = math.cos(latitudeinradians)*math.cos(p)
d = 24 - (7.63944*math.acos(numerator/denominator))

#Prints the amount of minutes in daylight. Multiply d by 60 because d is in hours, not minutes.
print("There are about %.3f" % (d*60) + " minutes of daylight." )
