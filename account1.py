class Account:
    def __init__(self, acct_number, name, pin, balance):
        self.acct_number = acct_number
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        return ("Account ID: " + str(self.acct_number) + " : Name: " + str(self.name) + " : Pin: " + str(self.pin) + " : Balance: " +
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