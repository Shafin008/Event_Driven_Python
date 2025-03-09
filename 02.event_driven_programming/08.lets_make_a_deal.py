import simpleguitk as simplegui
import random
import math

# globals
box = 1
switched_box = 1
prize_box = 1
box_choice = True
total_matches = 0
total_wins = 0

# helper function
def initialize():
    global prize_box, box_choice, box, switched_box
    box = 1
    switched_box = 1
    prize_box = random.randrange(1, 4)
    print("\nPlease select a box! Only one contains the prize!")
    box_choice = True

def choice():
    global box, switched_box, box_choice
    if not box_choice:
        if box == 1 and prize_box == 1:
            switched_box = random.randrange(2,4)
        elif box == 1 and prize_box == 2:
            switched_box = 3 
        elif box == 1 and prize_box == 3:
            switched_box = 2

        elif box == 2 and prize_box == 2:
            switched_box = random.randrange(1,4,2) 
        elif box == 2 and prize_box == 1:
            switched_box = 3 
        elif box == 2 and prize_box == 3:
            switched_box = 1
        
        elif box == 3 and prize_box == 3:
            switched_box = random.randrange(1,3) 
        elif box == 3 and prize_box == 1:
            switched_box = 2
        elif box == 3 and prize_box == 2:
            switched_box = 1

        print(f"By the way, box {switched_box} is empty")
        print("Would you like to change your guess?")

def switching():
    global box, switched_box
    if box == 1 and switched_box == 2:
        box = 3
    elif box == 1 and switched_box == 3:
        box = 2
    elif box == 2 and switched_box == 1:
        box = 3
    elif box == 2 and switched_box == 3:
        box = 1
    elif box == 3 and switched_box == 1:
        box = 2
    elif box == 3 and switched_box == 2:
        box = 1

    return box
    
# event handler
def box_one():
    global box, box_choice
    if box_choice:
        print("You chose box one.")
        box = 1
        box_choice = False
        choice()

def box_two():
    global box, box_choice
    if box_choice:
        print("You chose box two.")
        box = 2
        box_choice = False
        choice()

def box_three():
    global box, box_choice
    if box_choice:
        print("You chose box three.")
        box = 3
        box_choice = False
        choice()

def switch():
    global box, box_choice, total_matches, total_wins
    if not box_choice:
        box = switching()
        print("You switched your box.")
        if box == prize_box:
            print("Congratulations!")
            print(f"The prize was in box {box}")
            total_matches += 1
            total_wins += 1
        elif box != prize_box:
            print("Too bad. :(")
            print(f"The prize was in box {prize_box}")  
            total_matches += 1
        win_percentage = math.ceil((total_wins/total_matches)*100)
        print(f"Your win percentage: {win_percentage}%")
        initialize()

def no_switch():
    global box_choice, total_matches, total_wins
    if not box_choice:
        print("You didn't switch your box.")
        if box == prize_box:
            print("Congratulations!")
            print(f"The prize was in box {box}")
            total_matches += 1
            total_wins += 1

        elif box != prize_box:
            print("Too bad :(")
            print(f"The prize was in box {prize_box}")
            total_matches += 1

        win_percentage = math.ceil((total_wins/total_matches)*100)
        print(f"Your win percentage: {win_percentage}%")
        initialize()
            

# frame
frame = simplegui.create_frame("Let's make a deal", 400, 300, 300)

# register event handlers
frame.add_button('Box One', box_one, 50)
frame.add_button('Box Two', box_two, 50)
frame.add_button('Box Three', box_three, 50)
frame.add_button('Switch', switch, 50)
frame.add_button("Don't Switch", no_switch, 50)

# start frame
initialize()
frame.start()