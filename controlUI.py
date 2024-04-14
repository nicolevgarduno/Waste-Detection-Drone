import tkinter
from tkinter import *
import djitellopy as tello


def pilotScreen():
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