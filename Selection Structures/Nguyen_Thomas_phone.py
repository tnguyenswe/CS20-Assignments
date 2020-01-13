'''
Name: Thomas Nguyen
Date: 1/6/20
Professor: Henry Estrada
Assignment: Selection Structures (Part 3: Phone Plan)
This program calculates the cost of 2 different phone plans given the amount of units, base cost, and base limit.
'''

#Created class named calculations so I could group all my functions together.
class calculations:
    #Defines get_units function according to the assignment.
    def get_units():
        units_used = input("Enter number of units used: ")
        return int(units_used)

    #Defines calculate_cost function in order to return the price of the plan.
    def calculate_cost(num_of_units, base_cost, base_limit, over_base_limit_price):
        price = 0
        units_over = 0
        if(num_of_units>base_limit):
            units_over = num_of_units - base_limit
            price = (base_cost + units_over*over_base_limit_price)
            return price
        else:
            price = base_cost
            return price

    #Defines plan 1's base cost, base limit, and price per unit over the base limit.
    def plan1():
        base_cost = 9.38
        base_limit = 65
        over_base_limit_price = .045
        return base_cost, base_limit, over_base_limit_price

    #Defines plan 2's base cost, base limit, and price per unit over the base limit.
    def plan2():
        base_cost = 8.57
        base_limit = 50
        over_base_limit_price = .052
        return base_cost, base_limit, over_base_limit_price

def main():
    #While loop to check whether the user entered a correct value.
    while True:
         n = calculations.get_units()
         if (n>=0):
            break
         else:
            print("You cannot have negative units.")

    #Saves the base costs, base limits, and price per unit over the base limit of both plans into their own variables.
    a,b,c = calculations.plan1()
    d,e,f = calculations.plan2()

    #Calculates and prints the cost of the first plan according to the requirements.
    plan1 = calculations.calculate_cost(n,a,b,c)
    print("Cost for plan 1: $%.2f" % (round(plan1,2)))

    #Calculates and prints the cost of the second plan according to the requirements.
    plan2 = calculations.calculate_cost(n,d,e,f)
    print("Cost for plan 2: $%.2f" % (round(plan2,2)))

    #Determines which plan is cheaper and tells user which one is cheaper.
    if(round(plan1,2) > (round(plan2,2))):
        print("Plan 2 is cheaper.")
    elif(round(plan2,2) > round(plan1,2)):
        print("Plan 1 is cheaper.")
    else:
        print("They're the same price.") #In the case of floating point numbers, use test case of "69" or "70". This line will be used.

#Calls the main function.
main()