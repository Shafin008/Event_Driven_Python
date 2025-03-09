# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simpleguitk as simplegui
import random

# global
game = True

# helper
def initialize():
    global game
    game = True

# Functions that compute RPSLS
def number_to_name(num):
    global game
    if game:
        if num == 0:
            return "Spock"
        elif num == 1:
            return "paper"
        elif num == 2:
            return "lizard"
        elif num == 3:
            return "scissors"
        elif num == 4:
            return "rock"
        else:
            game = False


def name_to_number(name):
    global game
    if game:
        if name == "Spock":
            return 0
        elif name == "paper":
            return 1
        elif name == "lizard":
            return 2
        elif name == "scissors":
            return 3
        elif name == "rock":
            return 4
        else:
            game = False
            
        
def rpsls(player_choice):
    global game
    
    print(f"Player chooses {player_choice}")
    player_choice_number = name_to_number(player_choice)

    if game:
        computers_choice = random.randrange(0,5)
        computers_choice = number_to_name(computers_choice)
        print(f"Computer chooses {computers_choice}")
        computers_choice_number = name_to_number(computers_choice)

        diff = computers_choice_number - player_choice_number
        modulo_diff = diff % 5

        if modulo_diff == 1 or modulo_diff == 2:
            print("Computer wins!")
            print()

        elif modulo_diff == 3 or modulo_diff == 4:
            print("Player wins!")
            print()

        elif modulo_diff == 0:
            print("Player and computer tie!")
            print()

    else:
        print()
        print("Error: Bad Input. Please write one of this to enter: rock, paper, scissors, lizard, Spock")
        print()
        initialize()
        
    
# # Handler for input field
def get_guess(guess):
    global game
    if game:
        rpsls(guess)



# # Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 100)


# # Start the frame animation
initialize()
frame.start()


# ###################################################
# Test

# get_guess("Spock")
# get_guess("dynamite")
# get_guess("paper")
# get_guess("lazer")

# ###################################################
# # Sample expected output from test
# # Note that computer's choices may vary from this sample.

# #Player chose Spock
# #Computer chose paper
# #Computer wins!
# #
# #Error: Bad input "dynamite" to rpsls
# #
# #Player chose paper
# #Computer chose scissors
# #Computer wins!
# #
# #Error: Bad input "lazer" to rpsls
# #
