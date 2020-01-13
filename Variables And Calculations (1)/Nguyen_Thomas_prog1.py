'''
Name: Thomas Nguyen
Date: 1/5/20
Professor: Henry Estrada
Assignment: Variables and Calculations (1)
This is the first program assignment, it takes the prices of multiple items and calculates the subtotal, tax, and total.
'''

#Initialize i and price to 0.
price=0
i=0
#Gets price input from user.
item1 = float(input("Enter price for item " + "1: "))
item2 = float(input("Enter price for item " + "2: "))
item3 = float(input("Enter price for item " + "3: "))
item4 = float(input("Enter price for item " + "4: "))
item5 = float(input("Enter price for item " + "5: "))

#Calculates the price.
subtotal = item1 + item2 + item3 + item4 + item5

#Calculate the tax.
tax = subtotal*.07
#Calculate the total.
total = tax + subtotal

#Prints the results in format requested.
print("Subtotal: $ %.2f" % (subtotal))
print("Tax: $ %.2f" % (tax))
print("Total: $ %.2f" % (total))