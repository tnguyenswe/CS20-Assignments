'''
Name: Thomas Nguyen
Date: 1/23/20
Professor: Henry Estrada
Assignment: Final Project
This program is the driver program for the final project.
'''
#
#   Customer program.
#
#   This program constructs a dictionary of accounts keyed by account number
#   from a text file named accounts.dat. This file has one account per
#   line, with the account number, customer name, PIN, and balance,
#   separated by colons. For example, one entry might be:
#
#   10627:Georges Remi:0174:3571.85
#
#   The program then repeatedly allows customers to "log in" with account
#   number and PIN. (three tries). If user presses ENTER when asked for
#   account number, the program ends.
#
#   Once authenticated, the customer can deposit, withdraw, or finish.
#   When the customer finishes, the program writes the dictionary back to the
#   accounts.dat file in the same format as previously described.

from account import Account

#   Global variable: the account dictionary
accounts = {}

#DONE
def create_dictionary():
    """Create dictionary of accounts from a data file that has
    acct number, name, pin, and current balance separated by colon"""
    lines = open('accounts.dat', 'r')
    # lines = infile.readlines()
    new = []
    account = []
    i = 0
    for line in lines:
        line = line.strip()
        int_data = line.split(':')
        new.append(int_data)
        new_object = Account(*new[i])
        account.append(new_object)
        #account.append(Account(*new[i]))
        accounts[account[i].getacctnumber()] = account[i]
        i = i + 1
    # strip leading and trailing spaces, and split on ':'
    # create a new Account object with the given data
    # add it to the accounts dictionary with the account number as a key.
    lines.close()

def write_accounts():
    """Write back the accounts.dat file after customer finishes transaction."""
    key_list = []
    for key in accounts.keys():
        key_list.append(key)
    key_list.sort()
    writing = open('accounts.dat', 'w')
    i=0
    for key in key_list:
        writing.write(str(accounts[key_list[i]]) + '\n')
        i = i + 1
    writing.close()

    # get list of keys for the accounts dictionary
    # sort that list
    # open the accounts.dat file for writing
    # for each key in the key list:
    #    write str(accounts[key]) + '\n' to the file
    # close the file

def input_account_number():
    """Return an account number as a string"""
    result = input('Enter account number (or ENTER to quit): ')
    while(result not in accounts and result != ''):
        print('Invalid account number.')
        result = input('Enter account number (or ENTER to quit): ')
    return result

#DONE
def input_pin():
    """Return a 4-digit PIN as a string"""
    while True:
        pin = input("Enter a 4-digit PIN: ")
        if (len(pin) == 4 and pin.isnumeric()):
            return pin
            break
        else:
            print("Please enter a pin that is exactly 4 digits.")


def login(account_number):
    """Given an account number, give customer three tries to provide
    correct PIN. Return True if valid, False otherwise."""
    tries = 1
    account = accounts[account_number]

    correct_pin = account.getpin()

    pin = input_pin()
    while(tries<3 and pin != correct_pin):
        tries +=1
        pin = input_pin()

    if tries !=3:
        return True
    else:
        return False

    # set number of tries to one
    # retrieve the Account object for the given account_number
    # ask the user to input PIN (use input_pin() function)
    # while there are less than 3 tries and the input PIN doesn't match the
    # account PIN:
    #    add 1 to the number of tries
    #    ask for the PIN again
    # return True if the number of tries is not equal to 3 (good PIN),
    # otherwise return False (bad PIN)

def do_deposit(account):
    while True:
        amount = -1
        amount = float(input("Enter amount to deposit: $"))
        if amount>0:
            account.deposit(amount)
            break
        else:
            print("Amount cannot be negative.")

    """Deposit to the given account (which is an object)."""
    # Repeatedly ask for an amount until you get a non-negative value.
    # Call the account's deposit() method with that amount.

def do_withdrawal(account):
    """Withdraw from the given account (which is an object)."""
    # Repeatedly ask for an amount until you get a value that is valid
    # (non-negative and not more than the balance)
    # Call the account's withdraw() method with that amount.

    while True:
        amount = float(input("Enter amount to withdraw: $"))
        if amount>0 and amount<account.getbalance():
            account.withdraw(amount)
            break
        else:
            print("Amount cannot be negative or greater than balance.")


def do_transactions(account):
    """Ask to Deposit, Withdraw, or Finish; write new account file
    when finished. The account parameter is an Account object."""
    # Prompt for D)eposit, W)ithdraw, or F)inish and convert to uppercase

    action = 'x'
    while action != 'D' and action != 'W' and action != 'F':
        action = input("D)eposit, W)ithdraw, or F)inish: ")
        action = action.upper()

    while action != 'F':
        if action == 'D':
            do_deposit(account)
            print("Your balance is now: $%.2f" % (account.getbalance()))
            action = 'x'
            while action != 'D' and action != 'W' and action != 'F':
                action = input("D)eposit, W)ithdraw, or F)inish: ")
                action = action.upper()
        elif action == 'W':
            do_withdrawal(account)
            print("Your balance is now: $%.2f" % (account.getbalance()))
            action = 'x'
            while action != 'D' and action != 'W' and action != 'F':
                action = input("D)eposit, W)ithdraw, or F)inish: ")
                action = action.upper()

    write_accounts()
    if action == 'F':
        print("Thank you for banking with us, " + account.getname())
        exit()

def show_balance(account):
    """Return a string giving current account balance in proper
    format (2 decimals and dollar sign)"""
    return '$' + format(account.balance, '.2f')

def main():
    create_dictionary()
    account_number = input_account_number()
    while True:
        if account_number != '':
            if login(account_number):
                account = accounts.get(account_number)
                print('Welcome, ', account.name, '! Your current balance is ',
                      show_balance(account), '.', sep='')
                do_transactions(account)
            else:
                print('Sorry, could not validate you as a customer.')

            account_number = input_account_number()

        else:
            break


main()
