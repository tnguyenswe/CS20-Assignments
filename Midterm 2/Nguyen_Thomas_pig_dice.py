'''
Name: Thomas Nguyen
Date: 1/16/20
Professor: Henry Estrada
Assignment: Pig Dice
This program is a game of pig dice, roll the highest number you can without rolling a 1.
'''

#
#   The game of "pig"
#
#   The object of the game is to score as many points as possible.
#   You can either roll a die or keep your current total.
#   If you roll a 1, you lose. If you roll any other number, it is
#   added to your current score.
#

import random


#
#   This function will repeatedly ask you if you want to roll the die
#   or hold (keep your current total). If you enter 'r' or 'R', it will
#   return 'r' (for roll); if you enter 'h' or 'H', it will return 'h' (for
#   hold). If you enter any other string, the function gives an error message
#   and asks you for input again. Hint: use a while loop

def get_roll_or_hold():
    answer = input('R)oll or H)old? ')
    while True:
        if(answer.lower() == 'r' or 'h'):
            return answer
            break
        else:
            print("You printed an invalid input. Please try again.")

#   This function will repeatedly ask you if you want to play again or not
#   If you enter 'y' or 'Y', it will return True; if you enter 'n' or 'N',
#   it will return False. If you enter any other string, the function gives
#   an error message and asks you for input again. Hint: use a while loop.

def play_again():
    answer = input('Play again? (Y/N) > ')
    while True:
        if (answer.lower() == 'y'):
            playing = True
            return playing
            break
        if(answer.lower()=='n'):
            playing = False
            return playing
            break
        else:
            print("Please enter Y for yes or N for no")
            answer = input('Play again? (Y/N) > ')

    # your code goes here


playing = True
print('Welcome to the game of "pig."')

while playing:

    total = 0
    rolling = True


    while rolling:
        response = get_roll_or_hold()
        if response=='r':
            roll = random.randrange(1,7)
            print("You rolled a", roll)
            if roll == 1:
                print("Sorry, you lost this round.")
                rolling = False
            else:
                total += roll
                print("Your total is now", total)
        elif response=='h':
            rolling = False
        else:
            print("Please enter R to roll or H to hold.")
            rolling = True


    # call get_roll_or_hold() and put return value into a variable named response
    # if the response is 'r':
    #   roll the die
    #   print the value of the roll
    #   if the die is 1:
    #     print a message that player lost this round
    #     set rolling to False
    #   else:
    #     add die value to total
    #     print current total
    # else:
    #   set rolling to False

    if response == 'h':
        print("Your total for this round is ", total)
    # print total for the round, appropriately labeled

    print()  # for spacing
    playing = play_again()  # will set playing to True or False

print('Thanks for playing the game.')