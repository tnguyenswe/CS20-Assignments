'''class Account:
  def __init__(self, acct_number, name, pin, balance):
    self.acct_number = acct_number
    self.name = name
    self.pin = pin
    self.balance = balance

  def __str__(self):
    return ("Account ID: " + str(self.acct_number) + " : Name: " + str(self.name) + " : Pin: " + str(
      self.pin) + " : Balance: " +
            str(self.balance))

  def deposit(self, amount):
    if amount > 0:
      self.balance = self.balance + amount
      return self.balance
    else:
      return self.balance

  def withdraw(self, amount):
    if amount > 0 and amount < self.balance:
      self.balance
      self.balance - amount
      return self.balance
    else:
      return self.balance

  def getbalance(self):
    return self.balance

  def getname(self):
    return self.name

  def getacctnumber(self):
    return self.acct_number'''
from account1 import Account

accounts = {}

lines = open('/Users/tobeysdw/Downloads/accounts.dat', 'r')
#lines = infile.readlines()
new = []
account = []
i=0
for line in lines:
  line = line.strip()
  int_data = line.split(':')
  new.append(int_data)
  account.append(Account(*new[i]))
  accounts[account[i].getacctnumber()] = account[i]
  i = i + 1
  # add it to the accounts dictionary with the account number as a key.


print(accounts)

key_list = []
for key in accounts.keys():
  key_list.append(key)

print(key_list)
key_list.sort()