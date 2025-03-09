# Echo an input field

###################################################
# Student should add code where relevant to the following.

import simpleguitk as simplegui 

# Handlers for input field
def input_field(echo):
    print(echo)
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Echo input", 200, 200)

# register
frame.add_input("Echo", input_field, 50)

# Start the frame animation
frame.start()


###################################################
# Test

get_input("First test input")
get_input("Second test input")
get_input("Third test input")

###################################################
# Expected output from test

#First test input
#Second test input
#Third test input
