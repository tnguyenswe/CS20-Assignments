'''
Name: Thomas Nguyen
Date: 1/6/20
Professor: Henry Estrada
Assignment: Functions (Part 3: Spherical Distance)
This program takes the latitude and longitude of 2 cities and calculates the distance between them, both in kilometers and miles.
'''

#Imports the math module
import math

#Sets r to be 6371 (radius of Earth in kilometers).
r=6371

#Defines the great_circle_distance function to calculate the distance between the cities.
def great_circle_distance(lat1, lon1, lat2, lon2):
    theta = math.acos(math.sin(lat1) * math.sin(lat2) + (math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1 - lon2))))
    d = r*theta
    return(d)

#Defines the kilometers to miles function.
def km_to_miles(k):
    return(k*.621371)

#Defines the main function.
def main():
    #Gets the latitude and longitudes of both cities from the user.
    lat1 = math.radians(float(input("Enter the latitude of the first city: ")))
    lon1 = math.radians(float(input("Enter the longitude of the first city: ")))
    lat2 = math.radians(float(input("Enter the latitude of the second city: ")))
    lon2 = math.radians(float(input("Enter the longitude of the second city: ")))

    #Calls the great_circle_distance function and sets the answer into a variable called distance.
    distance = great_circle_distance(lat1,lon1,lat2,lon2)
    #Converts float value of distance to integer value according to the problem.
    truedistance = int(distance)

    #Calls the km_to_miles function and gets the distance between the 2 cities but in miles.
    distanceinmiles = km_to_miles(distance)
    #Converts float value of distance to integer value according to the problem.
    truedistanceinmiles = int(distanceinmiles)

    #Prints the distances between the cities in kilometers and miles.
    print("\nThe distance between the 2 cities in kilometers is: " + str(truedistance) + " km")
    print("The distance between the 2 cities in miles is: " + str(truedistanceinmiles) + " miles")

#Calls the main function
main()