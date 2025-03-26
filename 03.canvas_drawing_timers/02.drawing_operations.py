import simpleguitk as simplegui

# draw handler
def draw(canvas):
    canvas.draw_text("An example of drawing", [60,385], 24, "Black")
    canvas.draw_circle([300,300], 50, 2, "Red", "Pink")

    # Draw line
    # canvas.draw_line(point1, point2, line_width, line_color)
    canvas.draw_line([100, 100],[300, 300], 2, "Black")
    canvas.draw_circle([100,100], 80, 5, "Green", "Lime")

    # Draw polygon
    # canvas.draw_polygon(point_list, line_width, line_color, fill_color = color)
    canvas.draw_polygon([[150, 150], [250,150], [250, 250], [150, 250]], 2, "Blue", "Aqua")

# Create frame
frame = simplegui.create_frame("Home", 400, 400)

# Register
frame.set_draw_handler(draw)
frame.set_canvas_background("Yellow")

# start frame
frame.start()