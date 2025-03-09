import simpleguitk as simplegui

'''
This program changes text in the canvas.
There will be a simple text(message) when the frame starts,
if we click the button, previous message will be replaced by a new message.
'''
# define globals
message = "Welcome!"

# define helpers
# define class

# define event handlers
def draw(canvas):
    canvas.draw_text(text=message, point=[50,112], font_size=36, font_color="Red")

def change_message():
    global message
    message = "Good Job!"

# create frame
frame = simplegui.create_frame(title="Simple Canvas",canvas_height=200, canvas_width=300, control_width=200)

# register event handler
frame.set_draw_handler(draw_handler=draw)
frame.add_button(text="Click Me!", button_handler=change_message)

# start frame
frame.start()