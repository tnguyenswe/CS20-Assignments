'''
Name: Thomas Nguyen
Date: 1/8/20
Professor: Henry Estrada
Assignment: Strings (Pig Latin)
This program converts any input into pig latin.
I also finished all 3 extra credits for this assignment!
'''

#Sets vowels to include normal vowels and y. Also includes capital versions as it is necessary for extra credit.
vowels = 'a','e','i','o','u','y','A','E','I','O','U','Y'

new_sentence = []

def piglatin(statement):
    #Clears the previous sentence if the function is used more than once.
    new_sentence.clear()
    #Splits the string into individual words and saves it into an array.
    wordarray = statement.split()

    #For statement to go through every single word in the array
    for word in wordarray:
        #Checks to see if first letter is vowel. According to extra credit #2, I'm treating y as a consonant if it's the first letter.
        if(word[0] in vowels and word[0]!='y' and word[0]!='Y'):
            #If the first letter is uppercase, it will always stay uppercase. So for extra credit #1 I do not need to change this.
            new_sentence.append(word + 'way')

        #If first letter isn't vowel, uses this statement.
        else:
            if(word[0].isupper()):

                #Handles 'qu' better for extra credit #3.
                if(word[0]=='Q' and word[1]=='u' or word[0]=='Q' and word[1]=='U'):
                    for letter in word[2:]:
                        if letter in vowels:
                            new_word = (word[word.index(letter):] + word[:word.index(letter)] + 'ay')
                            new_words = new_word.lower()
                            new_sentence.append(new_words.title())
                            break

                else:
                    for letter in word: #Parses every letter in the word
                        if letter in vowels: #Checks if letter is vowel to see where to stop the reordering of letters

                            #I used the slice notation in order to format the new strings.
                            #This means that w[i:] has all items starting through the rest of the array
                            #and w[:i] has all items from the beginning through the stop index -1.

                            #This is for extra credit #1.
                            new_word = (word[word.index(letter):] + word[:word.index(letter)] + 'ay')
                            new_words = new_word.lower()
                            new_sentence.append(new_words.title())
                            break
            else:
                #Handles 'qu' better for extra credit #3.
                if(word[0]=='q' and word[1]=='u' or word[0]=='q' and word[1]=='u'):
                    for letter in word[2:]:
                        if letter in vowels:
                            new_sentence.append(word[word.index(letter):] + word[:word.index(letter)] + 'ay')
                            break

                else:
                    for letter in word:  # Parses every letter in the word
                        if letter in vowels:  # Checks if letter is vowel to see where to stop the reordering of letters

                            # I used the slice notation in order to format the new strings.
                            # This means that w[i:] has all items starting through the rest of the array
                            # and w[:i] has all items from the beginning through the stop index -1.
                            new_sentence.append(word[word.index(letter):] + word[:word.index(letter)] + 'ay')
                            break


    #I used the join function in order to add the spaces in between each word so that the sentence is formatted properly.
    return (" ".join(new_sentence))

def main():
    statement = input("Enter a sentence: ")
    #Quits program if input is a space according to the assignment. Also keeps asking for user input if the input is not enter.
    while True:
        if(statement==''):
            exit()
        else:
            print(piglatin(statement))
            statement = input("Enter another sentence or press enter to quit: ")

main()