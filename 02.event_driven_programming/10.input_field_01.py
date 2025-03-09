import simpleguitk as simplegui
# Input fields allow the user to give data to the program.Input fields pass data that is typed into the control area to designated event handlers in the program. It is important to note that this information is always given as a string.

# global
width = 50

# event handler (input handler)
def input_handler(string_input):
    print(string_input)

# frame
frame = simplegui.create_frame('Input Field', 300, 300, 200)

# register event handler
text_input = frame.add_input("Echo", input_handler, width)

# start
frame.start()