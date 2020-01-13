'''
Name: Thomas Nguyen
Date: 1/6/20
Professor: Henry Estrada
Assignment: Functions (Part 2: Distances in Two Dimensions)
This program takes the x and y-coordinates of 2 points and calculates the Pythagorean and block distances between them.
'''

#Define the Pythagorean distance function
def distance(x1,x2,y1,y2):
    return (((x1-x2)**2)+((y1-y2)**2))**(1/2)

#Define the block distance function
def block_distance(x1,x2,y1,y2):
    return (abs(x1-x2)+abs(y1-y2))

def main():
    #Gets the x and y-coordinates of the points
    x1 = int(input("Enter the x-coordinate of the first point: "))
    y1 = int(input("Enter the y-coordinate of the first point: "))
    x2 = int(input("Enter the x-coordinate of the second point: "))
    y2 = int(input("Enter the y-coordinate of the second point: "))


    #Prints the Pythagorean and city block distance between the points.
    print("\nThe Pythagorean distance between the points is: %.2f" % (distance(x1,x2,y1,y2)))
    print("The city block distance between the points is: %.2f" % (block_distance(x1,x2,y1,y2)))

#Call the main function
main()