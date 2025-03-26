import simpleguitk as simplegui
import random

# globals
width = 500
height = 500
position = [50,50]
interval = 2000
message = "Python is Fun!"

# Helpers

# Event Handlers
def input_handler(msg):
    global message
    message = msg

def draw(canvas):
    canvas.draw_text(message, position, 24, 'Red')

def tick():
    global position
    x = random.randrange(0, width)
    y = random.randrange(0, height)
    position[0] = x
    position[1] = y

# Create frame
frame = simplegui.create_frame("Home", width, height)
timer = simplegui.create_timer(interval, tick)
# Register event handlers
frame.add_input("Message", input_handler, 100)
frame.set_draw_handler(draw)

# Start frame and timer
timer.start()
frame.start()