# Register three buttons

###################################################
# Student should add code where relevant to the following.

import simpleguitk as simplegui

# global
color = None

# Handlers for buttons
def set_red():
    global color
    color = "red"
    
def set_blue():
    global color
    color = "blue"
    
def print_color():
    print(color)

# Create frame
frame = simplegui.create_frame("Set and print colors", 200, 200)

# register
frame.add_button("Red", set_red, 50)
frame.add_button("Blue", set_blue, 50)
frame.add_button("Print Color", print_color, 50)

# Start the frame animation
frame.start()


###################################################
# Test

set_red()
print_color()
set_blue()
print_color()
set_red()
set_blue()
print_color()

###################################################
# Expected output from test

#red
#blue
#blue
