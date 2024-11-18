
from random import randint #For generating random numbers

def greet():
    """
    Greets a new user to the game

    Args:
        (None)
    Returns:
        (None, it executes a print function but doesn't actually return anything meaningful)
    """
    print("Hello, welcome to my 'What are the Odds?' game \n Answer the questions to play!")

#Calls the greet function to display the welcome message
greet()

#Flag to track whether to restart the game
flag = False

#Main Game Loop
while True:
    #Prompts the user for a number
    number = input("What are the odds you give me an A?: ")

    #Attempts to convert the input to an integer
    try:
        number = int(number)

    #Inform the user of invalid input and restart the loop
    except ValueError:
        print("You did not give me an integer.\n Please try again")
        continue

    #Checks if the entered number is positive
    try:
        choice = int(number)
        assert choice > 0

    #Inform the user that negative numbers aren't valid
    except AssertionError:
        print("Negative numbers do not work here. \n Please try again")
        continue

    #Generates a random integer between 1 and the entered number
    scope = randint(1, number)
    scope = int(scope)

    #Inner loop for guessing the number
    while True:
        #Prompts the user to make a guess (also counts them down)
        guess = input("3,2,1...")

        #Attempts to convert the guess to an integer
        try:
            guess = int(guess)

        #Inform the user of invalid input and restart the inner loop
        except ValueError:
            print("You did not give me an integer.\n Please try again")
            continue

        #Displays the random number generated
        print(scope)

        #Conditions for determining the outcome based on the guess...

        #Script wins
        if guess == scope and guess + scope != number:
            print("Thanks for the A!")

        #Both win
        elif guess + scope == number and guess == scope:
            print("I guess we both get A's??")

        #User wins??
        elif guess + scope == number and guess != scope:
            print("Weird...I guess I'll give you an A on BU Books")

        #No one wins
        else:
            print("Man, I wanted that A")

        #Asks the user if they want to play again
        repeat = input("Do you want to try again? Enter y if you do or n if you don't: ")

        #Exit the game if the user chooses not to play again
        if repeat == 'n':
            print("Thanks for playing!")
            quit()

        #If the user enters an invalid response, still exit the game, but act like it's broken
        if repeat != 'y' and repeat != 'n':
            print("Error you typed the wrong thing....e x i t i n g   n o w")
            quit()

        #If the user wants to continue, break to restart the game
        if repeat == 'y':
            flag = False
            break
    continue
