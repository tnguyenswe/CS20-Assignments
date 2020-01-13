'''
Name: Thomas Nguyen
Date: 1/6/20
Professor: Henry Estrada
Assignment: Selection Structures (Part 2: Software Sales)
This program calculates the subtotal, discount, and total of a software product given the quantity purchased and original price.
'''

#Created a class in order to calculate both the discount and price.
class calculations:
    #Calculates the discount amount in decimal.
    def discount(self, quantity):
        if(quantity<10):
            return(1)
        elif(quantity>=10 and quantity<=19):
            return(.9)
        elif(quantity>=20 and quantity<=49):
            return(.8)
        elif(quantity>=50 and quantity<=99):
            return(.75)
        elif(quantity>=100):
            return(.7)

    #Calculates the price including the discount amount.
    def price(self, quantity, price):
        return (self.discount(quantity) * price*quantity)

#Defines the main function.
def main():
    #Gets input from user for price of product as well as quantity of products purchased
    original_price = float(input("Enter price of product: $"))
    quantity = int(input("Enter quantity: "))

    #Creates calculations() object named calculator
    calculator = calculations()

    #Calculates price before discount and prints it according to format
    price_before_discount = original_price*quantity
    print("\nTotal price before discount: $%.2f" % (price_before_discount))

    #Calculates discount amount and prints it according to format
    discount_amount = (price_before_discount - (price_before_discount*calculator.discount(quantity)))
    print("Amount of discount: $%.2f" % (discount_amount))

    #Calculates price after discount and prints it according to format
    price_after_discount = calculator.price(quantity, original_price)
    print("Total price after discount: $%.2f" % (price_after_discount))

main()
