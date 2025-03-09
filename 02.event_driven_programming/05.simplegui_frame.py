import simpleguitk as simplegui

# frame parameters
window_name = "New Frame"
canvas_width = 200
canvas_height = 300
control_width = 400

# Creating frame
frame = simplegui.create_frame(
    title=window_name,
    canvas_width=canvas_width,
    canvas_height=canvas_height
)

# Setting the canvas background color
# frame.set_canvas_background("Red")
# frame.set_canvas_background("Orange")
# frame.set_canvas_background("DeepSkyBlue")
frame.set_canvas_background("#FF0000")

# start frame
frame.start()