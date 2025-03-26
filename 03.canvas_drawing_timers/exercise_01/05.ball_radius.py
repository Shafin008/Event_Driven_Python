# Move a ball

###################################################
# Student should add code where relevant to the following.


import simpleguitk as simplegui 

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    # canvas.draw_circle(center_point, radius, line_width, line_color, fill_color = color)
    canvas.draw_circle([200,200], ball_radius, 2, 'White', 'White')
    
# Event handlers for buttons
def increase_radius():
    global ball_radius
    if ball_radius < (WIDTH//2 - 2): 
        ball_radius += RADIUS_INCREMENT

def decrease_radius():
    global ball_radius
    if ball_radius > RADIUS_INCREMENT:
        ball_radius -= RADIUS_INCREMENT

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)


# Start the frame animation
frame.start()

