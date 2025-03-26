import simpleguitk as simplegui
message = ""

# event handlers
def input_handler(msg):
    global message
    message = msg

def draw_handler(canvas):
    canvas.draw_text(message, [50, 150], 20, "Red")

# frame
frame = simplegui.create_frame("Pictures", 300, 300)

# register
frame.add_input("Echo", input_handler, 100)
frame.set_draw_handler(draw_handler)
frame.set_canvas_background("yellow")

# start
frame.start()