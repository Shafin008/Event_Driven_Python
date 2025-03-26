import simpleguitk as simplegui

# define draw handler
def draw(canvas):
    # Drawing text on canvas
    # canvas.draw_text(text, point, font_size, font_color, font_face)
    canvas.draw_text("Hello", [100,100], 24, "White")

    # Drawing a circle on the canvas
    # canvas.draw_circle(center_point, radius, line_width, line_color, fill_color = color)
    canvas.draw_circle([100,100], 2, 2, "Red")

# frame
frame = simplegui.create_frame("Text drawing", 300, 200)

# register draw hanlder
frame.set_draw_handler(draw)

# start frame
frame.start()