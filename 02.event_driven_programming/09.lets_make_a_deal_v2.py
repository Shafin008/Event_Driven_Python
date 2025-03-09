import simpleguitk as simplegui
import random
import math

# Global Variables

## frame
frame_name = "Let's make a deal!"
canvas_width = 300
canvas_height = 300

## box
player_choice = 0
revealed = 0
prize_box = 0
in_stage_one = True

## game
wins = 0
attempts = 0

# helper
def initialize():
    global player_choice, revealed, prize_box, in_stage_one
    player_choice = 0
    revealed = 0
    prize_box = random.randrange(0,3)
    in_stage_one = True
    print("Please select a box! Only one contains the prize!")

def open_box():
    global revealed
    # num is either -1 or +1
    num = random.randrange(-1, 3, 2)
    # revealed box is the empty box
    # It can't be equal to player_choice or prize_box
    # making sure it's not equal to player_choice
    revealed = (player_choice + num) % 3
    # making sure it's not equal to prize_box
    if revealed == prize_box:
        revealed = (revealed + num) % 3

    print(f"By the way, box {revealed + 1} is empty")
    print("Would you like to change your guess?")

def get_result():
    global wins, attempts
    attempts += 1
    if player_choice == prize_box:
        wins += 1
        print("Congratulations!")
    else:
        print("Too bad. :(")
    print(f"The prize was in box {prize_box+1}")
    print(f"Your win percentage: {math.floor((wins/attempts) * 100)}%")
    print()
    initialize()

# event handlers
def choose_one():
    global player_choice, in_stage_one
    if in_stage_one:
        player_choice = 0
        in_stage_one = False
        print("You chose box one.")
        open_box()

def choose_two():
    global player_choice, in_stage_one
    if in_stage_one:
        player_choice = 1
        in_stage_one = False
        print("You chose box two.")
        open_box()

def choose_three():
    global player_choice, in_stage_one
    if in_stage_one:
        player_choice = 2
        in_stage_one = False
        print("You chose box three.")
        open_box()

def switch():
    global player_choice, in_stage_one
    if not in_stage_one:
        # Switching player choice
        player_choice = (player_choice+1)%3
        # making sure that player_choice != revealed
        if player_choice == revealed:
            player_choice = (player_choice+1)%3
        print("You switched your box.")
        get_result()

def no_switch():
    if not in_stage_one:
        print("You did not switch your box.")
        get_result()


# Frame
frame = simplegui.create_frame("Let's make a deal!", canvas_width, canvas_height) 

# register
frame.add_button("Box One", choose_one, 100)
frame.add_button("Box Two", choose_two, 100)
frame.add_button("Box Three", choose_three, 100)
frame.add_button("Switch", switch, 100)
frame.add_button("Don't Switch", no_switch, 100)

# Start
initialize()
frame.start()
