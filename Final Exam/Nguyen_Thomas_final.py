'''
Name: Thomas Nguyen
Date: 1/23/20
Professor: Henry Estrada
Assignment: Final
This program utilizes a class to show acceleration and braking of a car.
'''

#Defines Car class with acceleration, braking, and getting speed functions.
class Car:
    def __init__(self, year, model):
        self.year = year
        self.make = "make"
        self.model = model
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def get_speed(self):
        return self.speed


def main():
    #Initializes car object
    car = Car(2017, "Civic")
    #Prints accelerating car 5 times.
    print("car is accelerating:")
    i=0
    while i<5:
        car.accelerate()
        print("Current speed:", car.get_speed())
        i += 1
    #Prints braking car 5 times.
    print("car is braking:")
    i=0
    while i<5:
        car.brake()
        print("Current speed:",car.get_speed())
        i += 1

main()