# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simpleguitk as simplegui
import random
import math

# globals
num_range = 100
num_guesses = 7

# helper function to start and restart the game
def new_game():
    global secret_number, num_guesses
    # initialize global variables used in your code here
    secret_number = random.randrange(100)
    num_guesses = 7
    print("New game. Range is [0, 100)")
    print("Number of remaining guesses is ", num_guesses, '\n')

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    num_guesses = math.ceil(math.log(num_range - 0 + 1)/(math.log(2)))
    print("New game. Range is [0, 100)")
    print("Number of remaining guesses is ", num_guesses, '\n')


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range, num_guesses
    num_range = 1000
    num_guesses = math.ceil(math.log(num_range - 0 + 1)/(math.log(2)))
    print("New game. Range is [0, 1000)")
    print("Number of remaining guesses is ", num_guesses, '\n')
    
def input_guess(guess):
    # main game logic goes here	
    global num_guesses
    guess = int(guess)
    print("Guess was ", guess)
    
    if guess > secret_number:
        num_guesses -= 1
        if num_guesses == 0:
            print("Number of remaining guesses is ", num_guesses)
            print("You are out of guesses!")
            print("The secret number was,", secret_number, '\n')
            new_game()
        else:
            print("Number of remaining guesses is ", num_guesses)
            print("Lower!", '\n')
    elif guess < secret_number:
        num_guesses -= 1
        if num_guesses == 0:
            print("Number of remaining guesses is ", num_guesses)
            print("You are out of guesses!")
            print("The secret number was,", secret_number, '\n')
            new_game()
        else:
            print("Number of remaining guesses is ", num_guesses)
            print("Higher!", '\n')

    elif guess == secret_number:
        print("Correct!", '\n')
        new_game()
        

# create frame
frame = simplegui.create_frame("Guess The Number!", 300, 300)

# register event handlers for control elements and start frame
frame.add_input("Enter a guess", input_guess, 200)
frame.add_button("Range is [0, 100)", range100, 100)
frame.add_button("Range is [0, 1000)", range1000, 100)

# call new_game 
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
