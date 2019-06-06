#! /usr/bin/env python3
'''
    Rochelle Gardner
    13 May 2019
    Hangman

        Write a hagman game that randomly generates a word 
    and prompts the user to guess on eletter at a time, as 
    shown in the sample run. Each letter in the word is 
    displayed as an asterisk. When the user makes a correct 
    guess, the actual letter is then displayed. When the 
    user finishes a word, display the number of misses and 
    ask the user whether to continue playing. Create a list 
    to store the words.
'''

import random
import sys
import string


easyWords = ['plan', 'mole', 'nest', 'half', 'list',
            'risk', 'draw', 'side', 'lost', 'fate',
            'cool', 'shed', 'drop', 'wolf', 'stir',
            'cane', 'take', 'boom', 'rest', 'rank',
            'wild', 'lily', 'toll', 'hair', 'drop']

normWords = ['dress', 'fever', 'irony', 'cause', 'drain',
            'uncle', 'budge', 'doubt', 'aloof', 'refer',
            'youth', 'evoke', 'paint', 'swipe', 'total',
            'amuse', 'stain', 'glass', 'fleet', 'grief',
            'drift', 'brink', 'board', 'gaffe', 'opera']

medWords = ['jacket', 'rotate', 'morsel', 'depart', 'extort', 
            'repeat', 'dilute', 'finish', 'freeze', 'ensure', 
            'scrape', 'sphere', 'trance', 'patent', 'redeem', 
            'refund', 'rescue', 'census', 'thread', 'damage', 
            'viable', 'absent', 'rabbit', 'silver', 'salmon']

hardWords = ['species', 'sustain', 'minimum', 'loyalty', 'pursuit', 
            'missile', 'concern', 'benefit', 'meeting', 'cunning',
            'overeat', 'clothes', 'citizen', 'overall', 'speaker',
            'provoke', 'include', 'improve', 'offense', 'passage', 
            'gravity', 'anxiety', 'default', 'protest', 'receipt']

expertWords = ['stereotype', 'atmosphere', 'competence', 'enegagement', 'negligence', 
            'vegetarian', 'assignment', 'dependence', 'withdrawal', 'attraction', 
            'helicopter', 'admiration', 'absorption', 'accountant', 'chimpanzee', 
            'resolution', 'decorative', 'depression', 'mainstream', 'generation', 
            'dictionary', 'nomination', 'appearance', 'insistence', 'earthquake']


def guessWord(word):
    guesses = 0
    letter = []
    guess_word = []

    for i in word:
        guess_word.append('*')

    while True:
        print("Pick your letter in word ", end='')
        for element in guess_word:
            sys.stdout.write(str(element))
        guess = input("\n--->").lower()

        if ((not guess.isalpha()) and (len(guess) == 1)):
            print("It must be a letter...")
        elif (guess in letter and (len(guess) == 1)):
            print("You have already guessed that one...")
        elif ((guess not in letter) and (len(guess) == 1)):
            letter.append(guess)
            if guess in word:
                print("Your guess was right!")
                for i in range(0, len(word)):
                    if word[i] == guess:
                        guess_word[i] = guess

                if not '*' in guess_word:
                    print("\nYou win! It took you ", guesses, " guesses for", end=' ')
                    for element in guess_word:
                        sys.stdout.write(str(element))
                    again = input("\nDo you want to play again? y or n")
                    if again.lower() == 'y':
                        break
                    elif again.lower() == 'n':
                        print("Goodbye")
                        exit()

            else:
                print("That letter isn't in the word...")
                guesses += 1
        elif len(guess) > 1:
            print("You can only guess one letter at a time...")
        else:
            print("There was an unexpected error...")
            exit()

def wordChoice(choice):
    if (choice == 1):
        print("You picked easy?")
        wordNum = random.randint(0,24)
        word = easyWords[wordNum]
        guessWord(word)

    elif (choice == 2):
        print("Reasonable to start with normal words.")
        wordNum = random.randint(0,24)
        word = normWords[wordNum]
        guessWord(word)
        
    elif (choice == 3):
        print("Stepping it up with medium words?")
        wordNum = random.randint(0,24)
        word = medWords[wordNum]
        guessWord(word)
        
    elif (choice == 4):
        print("Ooh look at me, I know hard words.")
        wordNum = random.randint(0,24)
        word = hardWords[wordNum]
        guessWord(word)
        
    elif (choice == 5):
        print("You're not an expert...")
        wordNum = random.randint(0,24)
        word = expertWords[wordNum]
        guessWord(word)
        

def main():
    while True:
        print("\nWelcome to Hangman. Pick a level: ")
        print("\n1. Easy")
        print("2. Normal")
        print("3. Medium")
        print("4. Hard")
        print("5. Expert")
        print("0. Exit")
        choice = input("\n---> ")
        try:
            choice = int(choice)
            if (choice > 0 and choice < 6):
                wordChoice(choice)
            elif choice == 0:
                print("Goodbye")
                exit()
            else:
                print("Please pick one")
        except ValueError:
            print("Please enter a whole number as a choice...")

main()