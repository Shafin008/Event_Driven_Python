import simpleguitk as simplegui

f_initial = ''
l_initial = ''

#
def initials():
    global f_initial, l_initial
    print(f"Initials: {f_initial}{l_initial}")
# 
def first_name(name):
    global f_initial
    f_initial = name[0].upper()

def last_name(name):
    global l_initial
    l_initial = name[0].upper()

frame = simplegui.create_frame("Initials", 200, 200)
frame.add_input("First Name:", first_name, 200)
frame.add_input("Last Name:", last_name, 200)
frame.add_button("Create Initials", initials, 100)

frame.start()