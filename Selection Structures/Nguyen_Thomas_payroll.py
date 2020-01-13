'''
Name: Thomas Nguyen
Date: 1/6/20
Professor: Henry Estrada
Assignment: Selection Structures (Part 1: Payroll)
This program calculates the total wages of an employee given the amount of hours (includes overtime as well).
'''

#Defines the wages function.
def wages(hours, rate):
    if(hours>40):
        pay = 0
        overtime_hours = 0
        overtime_hours = hours - 40
        pay = (hours*rate + (overtime_hours*(rate*.5)))
        return(pay)
    else:
        return(hours*rate)

#Defines the main function.
def main():
    #Gets input from user rate of pay as well as hours worked for the week.
    hours = float(input("Enter how many hours you worked this week: "))
    rate = float(input("Enter your rate of pay: "))

    #Saves the wages into a variable.
    real_wages = wages(hours, rate)

    #Round the wages so that the calculation is more precise.
    rounded_wages = round(real_wages,2)

    #Prints the pay according to the format.
    print("Your pay for the week is: $%.2f" % (rounded_wages))

#Calls the main function.
main()