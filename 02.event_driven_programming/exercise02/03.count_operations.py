# GUI with buttons to manipulate global variable count

###################################################
# Student should enter their code below


import simpleguitk as simplegui

# global
count = 0

# Define event handlers for four buttons
def reset():
    global count
    count = 0

def print_count():
    print(count)

def increment():
    global count
    count += 1

def decrement():
    global count 
    count -= 1

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Simple Counter", 300,300,200)

# register
frame.add_button("Reset", reset, 50)
frame.add_button("Print", print_count, 50)
frame.add_button("Increment", increment, 50)
frame.add_button("Decrement", decrement, 50)

# Start the frame animation
frame.start()

    
###################################################
# Test

# Note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Expected output from test

#1
#2
#-2
