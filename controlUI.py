import tkinter
from tkinter import *
import djitellopy as tello
import cv2
from PIL import Image, ImageTk


def pilotScreen(drone):
    # drone movement functions
    # movement functions created bc direct implementation into button commmands causes execution on pilotScreen start
    def pilotPatrol(): 
        for _ in range(4):
            drone.move_forward(30)
            drone.rotate_clockwise(90)
    def forward():
        drone.move_forward(30)
    def back():
        drone.move_back(30)
    def left():
        drone.move_left(30)
    def right():
        drone.move_right(30)
    def clockwise():
        drone.rotate_clockwise(30)
    def cclockwise():
        drone.rotate_counter_clockwise(30)
    def up():
        drone.move_up(30)
    def down():
        drone.move_down(30)
    def land():
        drone.land()

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

#initial window
win = Tk(screenName='TrashDrone GUI', baseName=None, className='TrashDrone GUI', useTk=True, sync=False, use=None)
win.geometry("400x400")

#button = Button(win, text='Drone Simulation', width=25, command=test)
button1 = Button(win, text='Pilot Drone', width=25, command=pilotScreen)
button1.pack()
#button.pack()
win.mainloop()