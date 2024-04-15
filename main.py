import matplotlib.pyplot
import numpy as np
import djitellopy as tello
import cv2 as cv2
import pandas
import torch
import time
from logger import *
from imageCapture import *
from multiprocessing import Process
from threading import Thread
import tkinter as tk
from tkinter import *
import ray
import matplotlib

global img

ray.init()

@ray.remote
def detect_objects(drone, filename, image_folder):
    # Online dataset 50 epochs, around 1800 images, 12 hours
    model = torch.hub.load(r'yolov5', 'custom', path=r'./yolov5/runs/train/trash_results2/weights/best.pt', source='local')

    # Our dataset 100 epochs, less than 50 images, 3 hours
    #custom_model = torch.hub.load(r'yolov5', 'custom', path=r'./yolov5/runs/train/yolov5s_results3/weights/best.pt', source='local')

    while True:
        img = drone.get_frame_read().frame
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img_detect = model(img_rgb, size=416)

        for obj in img_detect.xyxy[0]:
            conf = float(obj[4])
            if conf > 0.9:
                current_time = time.time()
                print(f"Waste detected, logging into: {filename}")
                log_csv(filename, current_time, conf)
                capture_image(drone, current_time, image_folder)
                time.sleep(1)
        img_show = img_detect.render()

        cv2.imshow("Image", img_show[0])
        cv2.waitKey(1)

@ray.remote
def pilotScreen(drone):
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
    def takeoff():
        drone.takeoff()

    # pilot screen settings
    pilotScreen = Tk(screenName='Pilot Drone', baseName=None, className='Drone Simulation', useTk=True, sync=False, use=None)
    pilotScreen.geometry("450x750")
    pilot_frame = Frame(pilotScreen)
    pilot_frame.pack(side=LEFT)

    pilot_button = Button(pilot_frame, width=25, text='Forward', command=forward)
    pilot_button1 = Button(pilot_frame, width=25, text='Left', command=left)
    pilot_button2 = Button(pilot_frame, width=25, text='Right', command=right)
    pilot_button3 = Button(pilot_frame, width=25, text='Back', command=back)
    pilot_button5 = Button(pilot_frame, width=25, text='Patrol', command=pilotPatrol)
    pilot_button6 = Button(pilot_frame, width=25, text='Up', command=up)
    pilot_button7 = Button(pilot_frame, width=25, text='Down', command=down)
    pilot_button9 = Button(pilot_frame, width=25, text='Takeoff', command=takeoff)
    pilot_button8 = Button(pilot_frame, width=25, text='Land', command=land)
    pilot_button.pack()
    pilot_button1.pack()
    pilot_button2.pack()
    pilot_button3.pack()
    pilot_button6.pack()
    pilot_button7.pack()
    pilot_button8.pack()
    pilot_button5.pack()
    pilot_button9.pack()

    pilotScreen.mainloop()

if __name__ == "__main__":
    drone = tello.Tello()
    drone.connect()
    drone.streamon()
    if drone.get_battery() < 25:
        print(f"Battery Health is low at: {drone.get_battery()}")
    else:
        print(f"Battery Health at: {drone.get_battery()}")

    # Create logging folders and csv file
    filename = create_csv()
    image_folder = create_run_folders()


    ray.get([pilotScreen.remote(drone), detect_objects.remote(drone, filename, image_folder)])