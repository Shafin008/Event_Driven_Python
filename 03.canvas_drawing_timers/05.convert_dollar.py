import simpleguitk as simplegui

result = '0.00'
# Hepler function
def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = str(val) + " " + name + 's'
    return result

def convert(val):
    dollar = int(val)
    cent = int(round(100*(val-dollar)))

    dollar_str = convert_units(dollar, 'dollar')
    cent_str = convert_units(cent, 'cent')

    if dollar == 0 and cent == 0:
        return "Broke!"
    elif dollar == 0:
        return cent_str
    elif cent == 0:
        return dollar_str
    else:
        return f"{dollar_str} and {cent_str}"

# Event handler 
def input_handler(val):
    global result
    val = float(val)
    result = convert(val)

def draw_handler(canvas):
    canvas.draw_text(f"Your balance is: \n{result}", [5, 130], 20, 'Green')

# Create frame
frame = simplegui.create_frame("Money", 300, 300)

# Create a canvas background
frame.set_canvas_background("Yellow") 

# register event handlers
frame.add_input("Money", input_handler, 50)
frame.set_draw_handler(draw_handler)

frame.start()

# print(convert(11.23))
# print(convert(11.20)) 
# print(convert(1.12))
# print(convert(12.01))
# print(convert(1.01))
# print(convert(0.01))
# print(convert(1.00))
# print(convert(0))