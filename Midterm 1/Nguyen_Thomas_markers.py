'''
Name: Thomas Nguyen
Date: 1/6/20
Professor: Henry Estrada
Assignment: Midterm 1
This program determines the cost of a purchase of markers based on quantity of markers bought.
'''

#Gets input from user.
markersbought = int(input("How many markers are you buying? "))

#Determines number of packages of markers.
packages = markersbought//5
print("Number of packages: " + str(packages))
#Determines number of separate markers.
markers = markersbought%5
print("Number of separate markers: " + str(markers))

#Calculates the marker cost, package cost, and add them to find the subtotal.
markercost = markers*(.90)
packagecost = packages*(4.20)
subtotal = markercost + packagecost

#Prints subtotal in format specified
print("Subtotal: $%.2f" % (subtotal))
#Prints tax in format specified
tax = subtotal*.075
print("Tax: $%.2f" % (tax))
#Prints shipping in format specified
shipping = subtotal*.04
print("Shipping: $%.2f" % (shipping))
#Prints total in format specified
total = subtotal + tax + shipping
print("Total: $%.2f" % (total))