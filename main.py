import numpy as np
import djitellopy as tello
import cv2 as cv2
import pandas
import torch
import time
from logger import *
from imageCapture import *


# Online dataset 50 epochs, around 1800 images, 12 hours
model = torch.hub.load(r'yolov5', 'custom', path=r'./yolov5/runs/train/trash_results2/weights/best.pt', source='local')

# Our dataset 100 epochs, less than 50 images, 3 hours
custom_model = torch.hub.load(r'yolov5', 'custom', path=r'./yolov5/runs/train/yolov5s_results3/weights/best.pt', source='local')
me = tello.Tello()
me.connect()
if me.get_battery() < 25:
    print(f"Battery is low at: {me.get_battery()}")
    print("Terminating process")
print(me.get_battery())

global img

me.streamon()

while True:
    img = me.get_frame_read().frame
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img_detect = model(img_rgb, size=416)

    for obj in img_detect.xyxy[0]:
        label = int(obj[-1])
        conf = float(obj[4])
        print(f"Label: {label}          Confidence: {conf}")
        if label == 0:
            print("Can detected")
            time.sleep(1)
        if label == 1:
            print("Cardboard detected")
            time.sleep(1)
        if label == 2:
            print("Cigarette detected")
            time.sleep(1)
    img_show = img_detect.render()

    cv2.imshow("Image", img_show[0])
    cv2.waitKey(1)
    