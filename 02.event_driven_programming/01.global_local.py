# The goal of the program is to move an object along a number line using a move method, keep track of its location with the variable loc, and calculate the displacement (always positive) from its starting location with the displacement method.
start = 1
loc = start

def move(x):
    global loc
    print(f"Previous Position: {loc}")
    loc += x
    print(f"New Position: {loc}")
    return loc

def displacement():
    global loc
    return abs(loc-start)

position = move(3)
print(f"Displacement: {displacement()}")
new_position = move(-2)
print(f"Displacement: {displacement()}")