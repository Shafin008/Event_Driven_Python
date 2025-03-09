import simpleguitk as simplegui

# event(in this case 'button') handler
def button_handler():
    pass

def print_hi():
    print('Hi')

# create frame
frame = simplegui.create_frame('Buttons', 300, 300)

# adding button
frame.add_button('Press', button_handler, 100)
frame.add_button("'Hi' button", print_hi, 200)

frame.start()