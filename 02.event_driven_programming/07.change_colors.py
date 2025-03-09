import simpleguitk as simplegui
# globals
canvas_color = 'black' # default
canvas_width = 300
canvas_height = 300

# helper
def change_canvas_color():
    frame.set_canvas_background(canvas_color)

# event handlers
def blue():
    global canvas_color
    canvas_color = 'blue'
    change_canvas_color()

def red():
    global canvas_color
    canvas_color = 'red'
    change_canvas_color()

def green():
    global canvas_color
    canvas_color = 'green'
    change_canvas_color()

def yellow():
    global canvas_color
    canvas_color = 'yellow'
    change_canvas_color()

def black():
    global canvas_color
    canvas_color = 'black'
    change_canvas_color()

def white():
    global canvas_color
    canvas_color = 'white'
    change_canvas_color()


# frame
frame = simplegui.create_frame('Color Change', canvas_width, canvas_height, 300)

# register event handlers: adding buttons
frame.add_button('Blue', blue, 100)
frame.add_button('Red', red, 100)
frame.add_button('Green', green, 100)
frame.add_button('Yellow', yellow, 100)
frame.add_button('Black', black, 100)
frame.add_button('White', white, 100)

# start frame
frame.start()