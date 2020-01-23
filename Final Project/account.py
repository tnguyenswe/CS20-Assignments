'''
Name: Thomas Nguyen
Date: 1/23/20
Professor: Henry Estrada
Assignment: Final Project
This program is the account class for the final project.
'''
class Account:
    def __init__(self, acct_number, name, pin, balance):
        self.acct_number = acct_number
        self.name = name
        self.pin = pin
        self.balance = float(balance)

    def __str__(self):
        return (str(self.acct_number) + ":" + str(self.name) + ":" + str(self.pin) + ":" +
                str(self.balance))

    def deposit(self, amount):
        if amount>0:
            self.balance = self.balance + amount
            return self.balance
        else:
            return self.balance


    def withdraw(self, amount):
        if amount>0 and amount<self.balance:
            self.balance = self.balance - amount
            return self.balance
        else:
            return self.balance

    def getbalance(self):
        return self.balance

    def getname(self):
        return self.name

    def getacctnumber(self):
        return self.acct_number

    def getpin(self):
        return self.pin