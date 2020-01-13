'''
Name: Thomas Nguyen
Date: 1/5/20
Professor: Henry Estrada
Assignment: Variable And Calculations (2)
This program calculates the monthly payment of a loan given the principal, annual rate of interest, and number of years of the loan.
'''
#Import power function from math module
from math import pow

#Gets input from user for necessary information.
p = int(input("Enter amount of loan: $"))
annual_rate = float(input("Enter annual interest rate as a percent: "))
years = int(input("Enter number of years for the loan: "))

#Calculates all the variables according to the formula.
annual_rate_percent = annual_rate/100
monthly_rate = float(annual_rate_percent/12)
r = float(monthly_rate)
n = int(years*12)
ratio = (1+r)
subformula = ratio**n

#Calculates the payment formula.
payment = p*(r*subformula)/(subformula-1)

#Print the monthly payment formatted according to the requirements.
print("Your monthly payment is $%.2f" % (payment))