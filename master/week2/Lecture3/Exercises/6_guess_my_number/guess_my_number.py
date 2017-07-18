high  = 100
low   = 0
guess = 50

print("Please think of a new between 0 and 100!")

while high > low:
    print("Is your secret number {}?".format(guess))

    feedback = input("Enter 'h' to indicate the guess is too high. " + \
        "Enter 'l' to indicate the guess is too low. " + \
        "Enter 'c' to indicate I guessed correctly. ")

    if feedback == 'l':
        low   = guess
        guess = (low + high) // 2
    elif feedback == 'h':
        high  = guess
        guess = (low + high) // 2
    elif feedback == 'c':
        break
    else:
        print("Sorry, I did not understand your input.")

print ("Game over.  Your secret number was: {}".format(guess))
