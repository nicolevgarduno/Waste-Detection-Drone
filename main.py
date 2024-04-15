import djitellopy as tello
import cv2 as cv2
import torch
import time
from logger import *
from imageCapture import *
import tkinter as tk
from tkinter import *

global img

def control_drone(drone, filename, image_folder):
    # Online dataset 50 epochs, around 1800 images, 12 hour training
    model = torch.hub.load(r'yolov5', 'custom', path=r'./yolov5/runs/train/trash_results2/weights/best.pt', source='local')

    # Our dataset 100 epochs, less than 50 images, 3 hour training
    #custom_model = torch.hub.load(r'yolov5', 'custom', path=r'./yolov5/runs/train/yolov5_results3/weights/best.pt', source='local')

    root = tk.Tk()
    root.title("Drone Controlls")

    label = tk.Label(root)
    label.pack()

    # Drone controls
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

    # Buttons for each command
    pilot_button = Button(root, width=25, text='Forward', command=forward)
    pilot_button1 = Button(root, width=25, text='Left', command=left)
    pilot_button2 = Button(root, width=25, text='Right', command=right)
    pilot_button3 = Button(root, width=25, text='Back', command=back)
    pilot_button5 = Button(root, width=25, text='Patrol', command=pilotPatrol)
    pilot_button6 = Button(root, width=25, text='Up', command=up)
    pilot_button7 = Button(root, width=25, text='Down', command=down)
    pilot_button8 = Button(root, width=25, text='Land', command=land)
    pilot_button9 = Button(root, width=25, text='Takeoff', command=takeoff)
    pilot_button10 = Button(root, width=25, text='Rotate CCW', command=cclockwise)
    pilot_button11 = Button(root, width=25, text='Rotate CW', command=clockwise)
    pilot_button.pack()
    pilot_button1.pack()
    pilot_button2.pack()
    pilot_button3.pack()
    pilot_button6.pack()
    pilot_button7.pack()
    pilot_button8.pack()
    pilot_button5.pack()
    pilot_button9.pack()
    pilot_button10.pack()
    pilot_button11.pack()    

    # Detection loop
    while True:
        img = drone.get_frame_read().frame
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        img_detect = model(img_rgb, size=416)

        # Detect confidence and log 
        for obj in img_detect.xyxy[0]:
            conf = float(obj[4])
            if conf > 0.9:
                current_time = time.time()
                print(f"Waste detected, logging into: {filename}")
                log_csv(filename, current_time, conf)
                capture_image(drone, current_time, image_folder)
                time.sleep(1)

        # Image feed
        boxed_img = img_detect.render()
        cv2.imshow("Detection", boxed_img[0])
        cv2.waitKey(1)

        root.update_idletasks()
        root.update()


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
    
    control_drone(drone, filename, image_folder)