import tkinter
from tkinter import *
import random as rand
import djitellopy as tello


stop = False

def drone2can(canvas, drone, can):
    dx1, dy1, dx2, dy2 = canvas.coords(drone)
    tx1, ty1, tx2, ty2 = canvas.coords(can)
    if dx1 > tx1 + 17:
        canvas.move(drone, -1, 0)
        canvas.after(50, drone2can, canvas, drone, can)
    if dy1 > ty1 + 27:
        canvas.move(drone, 0, -1)
        canvas.after(50, drone2can, canvas, drone, can)
    if dx1 < tx1 + 17:
        canvas.move(drone, 1, 0)
        canvas.after(50, drone2can, canvas, drone, can)
    if dy1 < ty1 + 27:
        canvas.move(drone, 0, 1)
        canvas.after(50, drone2can, canvas, drone, can)
    elif dx1 == tx1 + 17 and dy1 == ty1 + 27:
        return

def stop():
    global stop
    stop = True

def start():
    global stop
    stop = False

def dronePatrol(simCanvas, trashDrone, dx, dy, trashCan, trash, trash1, trash2, log_text):
    global stop

    if stop == True:
        return

    simCanvas.move(trashDrone, dx, 0)
    x1, y1, x2, y2 = simCanvas.coords(trashDrone)
    cx1, cy1, cx2, cy2 = simCanvas.coords(trashCan)


    if x2 >= 600:
        dx *= -1
        simCanvas.move(trashDrone, dx, dy)
    if x1 <= 0:
        dx *= -1
        simCanvas.move(trashDrone, dx, dy)
    if y2 >= 500:
        dy *= -1
        simCanvas.move(trashDrone, dx, dy)
    if y1 <= 0:
        dy *= -1
        simCanvas.move(trashDrone, dx, dy)
    simCanvas.move(trashDrone, dx, 0)
    simCanvas.after(50, dronePatrol, simCanvas, trashDrone, dx, dy, trashCan, trash, trash1, trash2, log_text)
    #trash detection
    if trash in simCanvas.find_all():
        tx1, ty1, tx2, ty2 = simCanvas.coords(trash)
        if x1 >= tx1  and x1 <= tx2 and y1 >= ty1  and y1 <= ty2:
            simCanvas.delete(trash)
            log_text.insert(END, "Cigarette picked up\n")
            log_text.see(END)
            drone2can(simCanvas, trashDrone, trashCan)

    if trash1 in simCanvas.find_all():
        t1x1, t1y1, t1x2, t1y2 = simCanvas.coords(trash1)
        if x1 >= t1x1  and x1 <= t1x2 and y1 >= t1y1  and y1 <= t1y2:
            simCanvas.delete(trash1)
            log_text.insert(END, "Can picked up\n")
            log_text.see(END)
            drone2can(simCanvas, trashDrone, trashCan)

    if trash2 in simCanvas.find_all():
        t2x1, t2y1, t2x2, t2y2 = simCanvas.coords(trash2)
        if x1 >= t2x1  and x1 <= t2x2 and y1 >= t2y1  and y1 <= t2y2:
            simCanvas.delete(trash2)
            log_text.insert(END, "Wrapper picked up\n")
            log_text.see(END)
            drone2can(simCanvas, trashDrone, trashCan)



#droneSim window
def test():
    global stop
    #sim window settings
    simWin = Tk(screenName='Drone Simulation', baseName=None, className='Drone Simulation', useTk=True, sync=False, use=None)
    simWin.geometry("1100x750")
    #canvas settings
    simCanvas = Canvas(simWin, width=600, height=500, bg='green')
    simCanvas.pack(side=RIGHT)
    #draw Trashcan
    trashCan = simCanvas.create_rectangle(15, 15, 50, 70, fill="grey")
    # define the width and height of the trash
    # generate random coordinates for the top-left corner of the rectangle
    x11 = rand.randint(55, 580)  # ensure that the entire rectangle fits within the canvas
    y11 = rand.randint(55, 480)
    x21 = rand.randint(55, 580)
    y21 = rand.randint(55, 480)
    x31 = rand.randint(55, 580)
    y31 = rand.randint(55, 480)
    # Calculate the coordinates for the other corners of the rectangle
    x12 = x11 + 20
    y12 = y11 + 20
    x22 = x21 + 20
    y22 = y21 + 20
    x32 = x31 + 20
    y32 = y31 + 20
    # Create the rectangle on the canvas
    trash = simCanvas.create_rectangle(x11, y11, x12, y12, fill='red')
    trash1 = simCanvas.create_rectangle(x21, y21, x22, y22, fill='red')
    trash2 = simCanvas.create_rectangle(x31, y31, x32, y32, fill='red')
    # Draw drone
    trashDrone = simCanvas.create_oval(65, 65, 85, 85, fill="orange")
    #frame settings
    sim_frame = Frame(simWin)
    sim_frame.pack(side=LEFT)
    #text box to display trash pick up message
    log_text = Text(sim_frame, height=10, width=50)
    log_text.pack()
    #button settings
    test_button = Button(sim_frame, width = 25, text='Start Patrol', command=lambda: (start(), dronePatrol(simCanvas, trashDrone, 5, 7, trashCan, trash, trash1, trash2, log_text)))
    test_buttonS = Button(sim_frame, width=25, text='Stop Patrol/Land', command=stop)
    test_button1 = Button(sim_frame, width=25, text='Reset Simulation', command=lambda: (test(), simWin.destroy())) #lambda allows us to use multiple functions w 1 button
    test_button3 = Button(sim_frame, width=25, text='Forward', command=lambda: simCanvas.move(trashDrone, 0, 5))
    test_button4 = Button(sim_frame, width=25, text='Back', command=lambda: simCanvas.move(trashDrone, 0, -5))
    test_button5 = Button(sim_frame, width=25, text='Left', command=lambda: simCanvas.move(trashDrone, -5, 0))
    test_button6 = Button(sim_frame, width=25, text='Right', command=lambda: simCanvas.move(trashDrone, 5, 0))
    test_button1.pack()
    test_button.pack()
    test_buttonS.pack()
    test_button3.pack()
    test_button4.pack()
    test_button5.pack()
    test_button6.pack()
   
   
def pilotScreen(): # This pilotScreen GUI is different than the one used in final product
    # drone movement functions
    # movement functions created bc direct implementation into button commmands causes execution on pilotScreen start
    def pilotPatrol(): # movement functions created bc direct implementation into button commmands causes execution on pilotScreen start
        for i in range(4):
            trashDrone.move_forward(200)
            trashDrone.rotate_clockwise(90)
    def forward():
        trashDrone.move_forward(100)
    def back():
        trashDrone.move_back(100)
    def left():
        trashDrone.move_left(100)
    def right():
        trashDrone.move_right(100)
    def clockwise():
        trashDrone.rotate_clockwise(45)
    def cclockwise():
        trashDrone.rotate_counter_clockwise(45)
    def up():
        trashDrone.move_up(50)
    def down():
        trashDrone.move_down(50)
    def land():
        trashDrone.land()
    # drone initialization
    trashDrone = tello.Tello()
    trashDrone.takeoff()
    trashDrone.streamon()

    # pilot screen settings
    pilotScreen = Tk(screenName='Pilot Drone', baseName=None, className='Drone Simulation', useTk=True, sync=False, use=None)
    pilotScreen.geometry("1100x750")
    pilot_frame = Frame(pilotScreen)
    pilot_frame.pack(side=LEFT)
    pilot_button = Button(pilot_frame, width=25, text='Forward', command=forward)
    pilot_button1 = Button(pilot_frame, width=25, text='Left', command=left)
    pilot_button2 = Button(pilot_frame, width=25, text='Right', command=right)
    pilot_button3 = Button(pilot_frame, width=25, text='Back', command=back)
    pilot_button5 = Button(pilot_frame, width=25, text='Patrol', command=pilotPatrol)
    pilot_button6 = Button(pilot_frame, width=25, text='Up', command=up)
    pilot_button7 = Button(pilot_frame, width=25, text='Down', command=down)
    pilot_button8 = Button(pilot_frame, width=25, text='Land', command=land)
    pilot_button.pack()
    pilot_button1.pack()
    pilot_button2.pack()
    pilot_button3.pack()
    pilot_button6.pack()
    pilot_button7.pack()
    pilot_button8.pack()
    pilot_button5.pack()

    #Video feed setup
    trashFeed = Canvas(pilotScreen, width = 600, height = 500)
    trashFeed.pack(side = RIGHT)



#initial window
win = Tk(screenName='TrashDrone GUI', baseName=None, className='TrashDrone GUI', useTk=True, sync=False, use=None)
win.geometry("400x400")

button = Button(win, text='Drone Simulation', width=25, command=test)
button1 = Button(win, text='Pilot Drone', width=25, command=pilotScreen)
button1.pack()
button.pack()
win.mainloop()
