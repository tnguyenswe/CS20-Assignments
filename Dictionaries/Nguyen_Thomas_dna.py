'''
Name: Thomas Nguyen
Date: 1/14/20
Professor: Henry Estrada
Assignment: Dictionaries
This program takes a triple and corresponds it with the given sequence.
'''

#Saves all of the triples and their given abbreviations
nucleotides = {'TTT': 'Phe', 'TCT': 'Ser', 'TGT': 'Cys', 'TAT': 'Tyr',
 'TTC': 'Phe', 'TCC': 'Ser', 'TGC': 'Cys', 'TAC': 'Tyr',
 'TTG': 'Leu', 'TCG': 'Ser','TGG': 'Trp', 'TAG': '***',
 'TTA': 'Leu', 'TCA': 'Ser', 'TGA': '***','TAA': '***',
 'CTT': 'Leu', 'CCT': 'Pro', 'CGT': 'Arg', 'CAT': 'His',
 'CTC': 'Leu', 'CCC': 'Pro', 'CGC': 'Arg', 'CAC': 'His',
 'CTG': 'Leu', 'CCG': 'Pro', 'CGG': 'Arg', 'CAG': 'Gln',
 'CTA': 'Leu', 'CCA': 'Pro', 'CGA': 'Arg', 'CAA': 'Gln',
 'GTT': 'Val', 'GCT': 'Ala', 'GGT': 'Gly', 'GAT': 'Asp',
 'GTC': 'Val','GCC': 'Ala', 'GGC': 'Gly', 'GAC': 'Asp',
 'GTG': 'Val', 'GCG': 'Ala','GGG': 'Gly', 'GAG': 'Glu',
 'GTA': 'Val', 'GCA': 'Ala', 'GGA': 'Gly','GAA': 'Glu',
 'ATT': 'Ile', 'ACT': 'Thr', 'AGT': 'Ser', 'AAT': 'Asn',
 'ATC': 'Ile', 'ACC': 'Thr', 'AGC': 'Ser', 'AAC': 'Asn',
 'ATG': 'Met', 'ACG': 'Thr', 'AGG': 'Arg', 'AAG': 'Lys',
 'ATA': 'Ile', 'ACA': 'Thr', 'AGA': 'Arg', 'AAA': 'Lys'}

#Defines clean sequence function in order to process the string.
def clean_sequence(string):
    #Creates new list in order to contain the new strings in intervals of 3.
    new = []
    n=3
    for i in range(0, len(string.upper()), n):
        new.append(string.upper()[i:i+n])

    #Creates matching_sequence to store the corresponding sequence to the triple given.
    matching_sequence = []
    for i in range(len(new)):
        #If else statement to determine whether the triple has a given sequence.
        if new[i] not in nucleotides:
            print(new[i] + " invalid sequence")
        else:
            matching_sequence.append(nucleotides[new[i]])
            print(new[i] + " "  + "".join(nucleotides[new[i]]))


def main():
    #While true statement to either ask for user input until given right information or quit program.
    while True:
        string = input("Enter a nucleotide sequence or just press ENTER to quit: ")
        string = string.replace(" ", '')
        string = string.replace(",", '')

        if len(string)%3==0:
            break
        elif string=="":
            exit()
        else:
            print("Error: You must give complete triples.")

    #Calls the clean_sequence function
    clean_sequence(string)

#Calls the main function.
main()