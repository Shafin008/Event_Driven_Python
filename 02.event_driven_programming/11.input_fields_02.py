import simpleguitk as simplegui

# globals
frame_name = "Input Field"
canvas_width = 300
canvas_height = 300

# event handlers
def fat_cat(adjective):
    print(f"Fat Cat is {adjective}")

def triangle_type(degrees):
    degrees = float(degrees)
    if 90 < degrees < 180:
        print(f"Triangle type: Obtuse Triangle")
    if degrees == 90:
        print(f"Triangle type: Right Triangle")
    if 0 < degrees < 90:
        print(f"Triangle type: Acute Triangle")

# frame
frame = simplegui.create_frame(frame_name,canvas_width,canvas_height,200)
# register event handlers
cat = frame.add_input("Adjective", fat_cat, 100)
triangle = frame.add_input("Degrees", triangle_type, 50)

# start
frame.start()