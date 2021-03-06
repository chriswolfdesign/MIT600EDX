# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    for letter in secretWord:

        # If even a single letter is missing, return False
        if letter not in lettersGuessed:
            return False

    # If no letter is missing, return True
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter
        else:
            word += "_ "

    return word

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    alphabet = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        alphabet.remove(letter)

    return "".join(alphabet)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.®

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".\
        format(len(secretWord)))
    print("------------")

    guesses = 8
    lettersGuessed = []

    # Delibrate infinite loop to keep game going
    while(True):
        print("You have {} guesses left.".format(guesses))

        print("Available letters: {}".format(getAvailableLetters\
            (lettersGuessed)))

        guess = input("Please guess a letter: ").lower()

        # If user accidentally repeats a letter
        if guess in lettersGuessed:
            print("Oops!  You've already guessed that letter: {}".\
                format(getGuessedWord(secretWord, lettersGuessed)))

        # If the user guessed a letter that is in the word
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print("Good guess: {}".format(getGuessedWord(secretWord, \
                lettersGuessed)))

        # If the user guessed a letter that is not in the word
        else:
            lettersGuessed.append(guess)
            guesses -= 1
            print("Oops! That letter is not in my word: {}".\
                format(getGuessedWord(secretWord, lettersGuessed)))

        print("------------")

        # If the user has won the game
        if getGuessedWord(secretWord, lettersGuessed) == secretWord:
            print("Congratulations, you won!")
            break

        # If the user has lost the game
        if guesses == 0:
            print("Sorry, you ran out of guesses.  The word was {}.".format\
                (secretWord))
            break

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

if __name__ == "__main__":
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
