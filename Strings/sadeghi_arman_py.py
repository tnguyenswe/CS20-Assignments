
vowel = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']


def pig_latin(word):
    word.clear()

    if word[0].isupper():
        if word[0] in vowel:
            word[0].upper()
            return word + "way"
        else:
            for letter in word:
                if letter in vowel:
                    # print(letter)
                    word1 = word[0:word.index(letter)].lower()
                    word = word[word.index(letter)].upper() + word[word.index(letter)+1:] + word1
                    return word + "ay"
                    break
    else:
        if word[0] in vowel:
            return word + "way"
        else:
            for letter in word:
                if letter in vowel:
                    # print(letter)
                    word1 = word[0:word.index(letter)]
                    word = word[word.index(letter):] + word1
                    return word + "ay"
                    break


def main():
    sentence = input("Enter a sentence to convert to Pig Latin: ")
    # pig_latin(sentence)
    latin_word = ''  # create an empty string to store words in
    while True:  # as long as the given string is not blank
        while sentence != '':
            position = sentence.find(' ')  # find the space (returns -1 if not found)
            # print(position)

            if position < 0:  # if white space not found
                position = len(sentence)
                # latin_word = pig_latin(sentence)
                latin_word = latin_word + pig_latin(sentence) + ' '  # add the remainder to latin_word
                break
            else:
                word = sentence[:position]  # slice the sentence from the beginning to the position of the space
                # latin_word = pig_latin(word)
                latin_word = latin_word + pig_latin(word) + ' '  # add remainder to latin_word
                sentence = sentence[position + 1:]  # skip the space in oder to find next word
                # print(latin_word)


        latin_word = latin_word.rstrip()  # strip the last space
        print(latin_word)
        sentence = input("Enter another sentence to convert into pig latin, press 'enter' to quit: ")




main()


