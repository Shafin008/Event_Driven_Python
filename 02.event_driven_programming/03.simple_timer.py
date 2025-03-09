# import
import simpleguitk as simplegui

# Define globals
counter = 0

# define helper funtions 
def increment():
    global counter
    counter += 1
# define class (no class)

# define event handlers
def click():
    increment()

def reset():
    global counter
    counter = 0

def draw(canvas):
    global counter
    canvas.draw_text(text=counter, point=[150, 150], font_size=36, font_color="Red")

# Create frame
frame = simplegui.create_frame(
    title="Simple Counter",
    canvas_width=300,
    canvas_height=300,
    control_width=200
)

# Register event handlers
timer = simplegui.create_timer(interval=1000, timer_handler=click)
frame.add_button(text='Reset', button_handler=reset)
frame.set_draw_handler(draw_handler=draw)

# start the frame and timer
timer.start()
frame.start()
