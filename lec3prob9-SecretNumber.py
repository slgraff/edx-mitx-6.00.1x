# lec3prob9 - Secret Number
# Use bisection search to guess the value of a number from 0 to 100

low = 0
high = 100
userInput = ""

# bisect low and high to get a starting point
myGuess = (low + high)/2

print "Please think of a number between 0 and 100!"

# Loop through presenting guesses to user until correct
while str(userInput) != "c":
    
    # Present myGuess to the user
    print "Is your secret number " + str(myGuess) +"?"

    # Ask user to enter if guess is correct, too high, or too low
    print "Enter 'h' to indicate the guess is too high. ",
    print "Enter 'l' to indicate the guess is too low. ",
    print "Enter 'c' to indicate I guessed correctly. ",
    userInput = raw_input ()
    
    if str(userInput) == "h":
        high = myGuess
        myGuess = (low + high)/2
    elif str(userInput) == "l":
        low = myGuess
        myGuess = (low + high)/2
    elif str(userInput) == "c":
        break
    else:
        print "Sorry, I did not understand your input."

print "Game over. Your secret number was: " + str(myGuess)