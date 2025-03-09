# import
import simpleguitk as simplegui

# globals
store = 12
operand = 3

# event handlers
def output():
    '''prints contents of the store and operand'''
    print(f"Store = {store}")
    print(f"Operand = {operand}")

def swap():
    '''swaps the value of store and operand'''
    global store, operand
    store, operand = operand, store
    print("\nAfter swapping values\n")
    output()

def add():
    '''adds operand to store'''
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

# frame
frame = simplegui.create_frame(
    title='Calculator',
    canvas_width=300,
    canvas_height=300
)

# register the event handlers
frame.add_button(text='Print', button_handler=output, width=100)
frame.add_button(text='Swap', button_handler=swap, width=100)
frame.add_button(text='Add', button_handler=add, width=100)
frame.add_button(text='Sub', button_handler=sub, width=100)
frame.add_button(text='Mul', button_handler=mult, width=100)
frame.add_button(text='Div', button_handler=div, width=100)

# start frame
frame.start()