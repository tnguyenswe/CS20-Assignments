'''
Name: Thomas Nguyen
Date: 1/6/20
Professor: Henry Estrada
Assignment: Lists and Files (Part 1: Planetary Density)
This program takes a txt file and calculates the min, max, average, and median densities of the planets.
'''

#Define function to calculate minimum density.
def min_density(list):
    #Creates empty list to store values of the original list as a duplicate.
    min_list = []
    for i in range(len(list)):
        min_list.append(list[i])

    #Used the sort method so the list is sorted in ascending order and returns the first index.
    min_list.sort()
    return min_list[0]

#Define function to calculate maximum density.
def max_density(list):
    # Creates empty list to store values of the original list as a duplicate.
    max_list = []
    for i in range(len(list)):
        max_list.append(list[i])

    #Used the sort method so the list is sorted in ascending order and returns the last index.
    max_list.sort()
    return max_list[len(list)-1]

#Define function to calculate average density.
def avg_density(list):
    # Creates empty list to store values of the original list as a duplicate.
    avg_density = []
    #Initialized total variable to sum up all the list values in order to calculate the average.
    total = 0
    for i in range(len(list)):
        avg_density.append(list[i])

    #Sums up all the values inside the avg_density list and returns the average.
    for i in range(len(avg_density)):
        total += (avg_density[i])
    return total/len(avg_density)

#Define function to fine median density.
def med_density(list):
    # Creates empty list to store values of the original list as a duplicate.
    med_density = []
    for i in range(len(list)):
        med_density.append(list[i])

    #Used the sort method in order to make sure the median is properly calculated.
    med_density.sort()

    #Saves the length of the med_density list inside a variable.
    length = len(med_density)

    #Saves the median index in such a way that allows for easy computation if the list has an odd amount of values.
    index = (length-1)//2

    #If statement to check whether the list has an odd or even amount of values and returns median accordingly.
    if(length%2):
        return med_density[index]
    else:
        return (med_density[index] + med_density[index+1])/2

#Defines main function
def main():
    '''Saves the information of the density.txt file as variable f. You will need to change the directory of the density.txt file accordingly.
    instead of open("/Users/tobeysdw/Downloads...." you can find your folder path on Windows by right clicking the file and clicking on
    properties, and change it accordingly. On Mac, you right click on the file and press Get Info to find the file path.'''
    f = open("/Users/tobeysdw/Downloads/density.txt", "r")

    #Initializes empty list to store the data from the density.txt file and add the values into a list.
    density = []
    #For loop in order to add all the data from density.txt to the density list.
    for aline in f:
        int_data = aline.split()
        density.append(float(int_data[1]))

    #Prints the min, max, avg, and median densities. I formatted the average density so that it only rounds to 2 decimal places.
    print("The minimum density is: " + str(min_density(density)) + " grams per cubic centimeter")
    print("The maximum density is: " + str(max_density(density)) + " grams per cubic centimeter")
    print("The average density is: %.2f" % avg_density(density) + " grams per cubic centimeter")
    print("The median density is: " + str(med_density(density)) + " grams per cubic centimeter")

main()