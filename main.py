import djitellopy as tello
import cv2 as cv2
import torch
import time
from logger import *
from imageCapture import *
import tkinter as tk
from tkinter import *
from controls import *
from multiprocessing import Process

global img

def detect_obj(drone, filename, image_folder):
    # Online dataset 50 epochs, around 1800 images, 12 hour training
    model = torch.hub.load(r'yolov5', 'custom', path=r'./yolov5/runs/train/trash_results2/weights/best.pt', source='local')

    #Our dataset 100 epochs, less than 50 images, 3 hour training
    #custom_model = torch.hub.load(r'yolov5', 'custom', path=r'./yolov5/runs/train/yolov5s_results3/weights/best.pt', source='local')

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
    p1 = Process(target=create_controls, args=drone)
    p1.start()
    p2 = Process(target=detect_obj, args=(drone, filename, image_folder))
    p2.start()

    p1.join()
    p2.join()
