# Open a frame

###################################################
# Open frame
# Student should add code where relevant to the following.

import simpleguitk as simplegui 

message = "My second frame!"

# Handler for mouse click
def click():
    print(message)

# Create frame
frame = simplegui.create_frame(message, 200, 100)

# Assign callbacks to event handlers
frame.add_button("Click me", click)

# Start the frame animation
frame.start()

