'''
Name: Thomas Nguyen
Date: 1/6/20
Professor: Henry Estrada
Assignment: Lists and Files (Part 2: Driver's License Exam)
This program takes a txt file and grades whether or not a student passed an exam.
'''

#Sets the answers to the test according to the key given in the assignment.
license_answers = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']

#Defines the main function.
def main():
    #Opens the text file of the student's answers and saves it in variable f.
    f = open("/Users/tobeysdw/Downloads/incorrect_answers.txt", "r")

    #Creates empty list in order to store the student's answers from the txt file.
    student_answers = []

    #Appends all the data from the txt file to the student_answers list.
    for i in f:
        char_data = i.splitlines()
        student_answers.append(char_data[0])

    #Initializes correct to 0 as a counter to see how many questions the student answered correctly.
    correct = 0
    #Initializes an empty list in order to get the numbers of as well as how many questions the student missed.
    incorrect = []

    #For loop in order to determine correct and incorrect answers.
    for i in range(len(license_answers)):
        if(license_answers[i] == student_answers[i]):
            correct +=1
        else:
            incorrect.append(i+1)
            correct = correct

    #If else statement that prints different outputs based on how many questions the student got correct.
    if(correct>14):
        print("You passed! The total number of correctly answered questions is: " + str(correct))
        print("\nYou passed! The total number of incorrectly answered questions is: " + str(len(incorrect)))
        if len(incorrect)>0:
            print("\nHere are all the incorrect questions: ")

            wrong = ''
            for i in incorrect:
                wrong = wrong + str(i) + ', '
            print(wrong[0:-2])
    else:
        print("You failed, the total number of correctly answered questions is: " + str(correct))
        print("\nYou failed, the total number of incorrectly answered questions is: " + str(len(incorrect)))
        print("\nHere are all the incorrect questions: ", end='')

        wrong = ''
        for i in incorrect:
            wrong = wrong + str(i) + ', '
        print(wrong[0:-2])
main()