import simpleguitk as simplegui

# globals
frame_name = 'Simple Calculator'
canvas_width = 300
canvas_height = 300
control_width = 200

operand = 0
store = 0

# event handlers
def output():
    print(f"\nStore: {store}")
    print(f"Operand: {operand}\n")

def swap():
    global operand, store
    operand, store = store, operand
    output()

def text_input(num_str):
    global operand
    num_str = float(num_str)
    operand = num_str
    output()

def add():
    global store
    store += operand
    output()

def sub():
    global store
    store -= operand
    output()

def mult():
    global store
    store *= operand
    output()

def div():
    global store
    store /= operand
    output()

def clear_operand():
    global operand
    operand = 0
    output()

def clear_all():
    global store, operand
    store = 0
    operand = 0
    output()


# frame
frame = simplegui.create_frame(
    frame_name,
    canvas_width,
    canvas_height,
    control_width
)

# register
frame.add_button("Print", output, 50)
frame.add_button("Swap", swap, 50)
frame.add_button("Add", add, 50)
frame.add_button("Sub", sub, 50)
frame.add_button("Mul", mult, 50)
frame.add_button("Div", div, 50)
frame.add_button("Clear Opearand", clear_operand, 100)
frame.add_button("Clear All", clear_all, 100)
text_input = frame.add_input("Enter a Number", text_input, 100)

# start
frame.start()
