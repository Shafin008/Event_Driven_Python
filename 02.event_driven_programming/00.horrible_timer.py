import simpleguitk as simplegui

# event handler
def tick():
    print('tick')

# Register handler
timer = simplegui.create_timer(
    interval=1000,
    timer_handler=tick
)

# start timer
timer.start()