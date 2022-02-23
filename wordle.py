import random
import os
import time
from typing import Counter
from termcolor import colored

def check_list(guess_wrd, word_bank):
    for i in range(0, len(word_bank)):
        word_bank[i] = word_bank[i].rstrip("\n")
        if guess_wrd == word_bank[i]:
            return True
    return False

if __name__ == '__main__':
    # set the game loop variable to 1 and curr_row to 0
    game_loop = 1
    curr_row = 0
    
    # open the word bank file to read
    fp = open("wordbank.txt", 'r')
    wrds = fp.readlines()
    
    # randomly selects a word in the list of words
    wrd = wrds[random.randint(0, len(wrds))]
    
    # strips the newline character
    wrd = wrd.rstrip("\n")
    
    game_rows = ["-----", "-----", "-----", "-----", "-----", "-----"]
    while(game_loop == 1):
        # clears the screen and prints the rows and words
        os.system('clear')
        print(colored("WORDLE", 'cyan', attrs=['underline', 'blink']))
        for i in range(0, 6):
            print(game_rows[i])
        
        # take the input from the user and checks if it is a word in the dictionary
        guess_wrd = input("What is your guess? ")
        check = check_list(guess_wrd, wrds)
        
        # checks if the correct word was guessed
        if (guess_wrd == wrd):
            game_loop = 2
        
        # checks if the current row is 5 and adjusts accordingly
        if (curr_row == 5 and check):
            game_loop = 3
            
        # check if the word length is not five letters
        if (len(guess_wrd) != 5):
            print("That is not a valid length word!")
            time.sleep(1)
        elif (check == False):
            print("That word is not in the dictionary!")
            time.sleep(1)
        else:
            to_append = ["X", "X", "X", "X", "X"]
            for i in range(0, 5):
                if guess_wrd[i] == wrd[i]:
                    to_append[i] = "O"
            for i in range(0, 5):
                if (wrd.__contains__(guess_wrd[i])):
                    for j in range(0, 5):
                        if (wrd[j] == guess_wrd[i] and to_append[i] != "O"):
                            to_append[i] = "M"
            # changes the guessed word to upper case and splits it
            guess_wrd = guess_wrd.upper()
            guess_wrd = list(guess_wrd)
            for i in range (0, 5):
                if (to_append[i] == 'M'):
                    guess_wrd[i] = colored(guess_wrd[i], 'yellow')
                if (to_append[i] == 'O'):
                    guess_wrd[i] = colored(guess_wrd[i], 'green')
            guess_wrd = "".join(guess_wrd)
            to_append = "".join(to_append)
            print("colored word " + guess_wrd)        
            game_rows[curr_row] = guess_wrd
            curr_row += 1
    
    os.system('clear')
    print(colored("WORDLE", 'cyan', attrs=['underline', 'blink']))
    for i in range(0, 6):
        print(game_rows[i])    
    if (game_loop == 2):
        print("Congratulations! You won!")
    if (game_loop == 3):
        print("Better luck next time!")
        print("The word was: " + wrd)
