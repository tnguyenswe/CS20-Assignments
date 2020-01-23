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
    #Sets all latitudes and longitudes for each city.
    sj_lat = math.radians(float(37.33))
    sj_lon = math.radians(float(-121.9))
    chicago_lat = math.radians(float(41.83))
    chicago_lon = math.radians(float(-87.68))
    washingtondc_lat = math.radians(38.90)
    washington_dc_lon = math.radians(-77.02)

    #Calls the great_circle_distance function and sets the answer into a variable called distance_sj_to_chicago.
    distance_sj_to_chicago = great_circle_distance(sj_lat,sj_lon,chicago_lat,chicago_lon)

    #Converts float value of distance_sj_to_chicago to integer value according to the problem.
    truedistance = int(distance_sj_to_chicago)
    #Calls the km_to_miles function and gets the distance between the 2 cities but in miles.
    distanceinmiles = km_to_miles(distance_sj_to_chicago)
    #Converts float value of distance to integer value according to the problem.
    truedistanceinmiles = int(distanceinmiles)

    #Prints the distances between San Jose and Chicago kilometers and miles.
    print("\nThe distance between San Jose and Chicago in kilometers is: " + str(truedistance) + " km")
    print("The distance between San Jose and Chicago in miles is: " + str(truedistanceinmiles) + " miles")

    #Calls the great_circle_distance function and sets the answer into a variable called distance_chicago_to_dc.
    distance_chicago_to_dc = great_circle_distance(chicago_lat,chicago_lon,washingtondc_lat,washington_dc_lon)

    #Converts float value of distance_chicago_to_dc to integer value according to the problem.
    truedistance = int(distance_chicago_to_dc)
    #Calls the km_to_miles function and gets the distance between the 2 cities but in miles.
    distanceinmiles = km_to_miles(distance_chicago_to_dc)
    #Converts float value of distance to integer value according to the problem.
    truedistanceinmiles = int(distanceinmiles)

   #Prints the distances between Chicago and Washington DC in kilometers and miles.
    print("\nThe distance between Chicago and Washington DC in kilometers is: " + str(truedistance) + " km")
    print("The distance between Chicago and Washington DC in miles is: " + str(truedistanceinmiles) + " miles")

#Calls the main function
main()