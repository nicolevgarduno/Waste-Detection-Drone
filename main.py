import numpy as np
import djitellopy as tello
import cv2 as cv2
import pandas
import torch
import time
from logger import *
from imageCapture import *
import threading

global img

def detect_objects(drone, filename):
    # Online dataset 50 epochs, around 1800 images, 12 hours
    model = torch.hub.load(r'yolov5', 'custom', path=r'./yolov5/runs/train/trash_results2/weights/best.pt', source='local')

    # Our dataset 100 epochs, less than 50 images, 3 hours
    custom_model = torch.hub.load(r'yolov5', 'custom', path=r'./yolov5/runs/train/yolov5s_results3/weights/best.pt', source='local')

    # Connect to drone and stream
    if drone.get_battery() < 25:
        print(f"Battery is low at: {drone.get_battery()}")
    else:
        print(f"Battery Health at: {drone.get_battery()}")

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
                time.sleep(1)
        img_show = img_detect.render()

        cv2.imshow("Image", img_show[0])
        cv2.waitKey(1)


if __name__ == "__main__":
    drone = tello.Tello()
    drone.connect()
    drone.streamon()
    filename = create_csv()
    detect_objects(drone, filename)