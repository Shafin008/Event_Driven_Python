# Convert input text into Pig Latin

###################################################
# Student should add code where relevant to the following.

import simpleguitk as simplegui

# Pig Latin helper function
def pig_latin(word):
    """Returns the (simplified) Pig Latin version of the word."""
    
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    # Student should complete function on the next lines.
    if first_letter == "a" or first_letter == "e" or first_letter == "i" or first_letter == "o" or first_letter == "u":
        word = word + 'way'
    else:
        word = rest_of_word + first_letter + "ay"
    return word

# Handler for input field
def input_field(text):
    text = pig_latin(text)
    print(text)

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Pig Latin translator", 200, 200)

# register
frame.add_input("Enter a word", input_field, 100)

# Start the frame animation
frame.start()



###################################################
# Test

get_input("pig")
get_input("owl")
get_input("tree")

###################################################
# Expected output from test

#igpay
#owlway
#reetay


