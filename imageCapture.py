import djitellopy as tello
import cv2
import os
import time

def create_run_folders():
    i = 0
    while True:
        folder_name = f"Logs/run{i}/images"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            return folder_name
        else:
            i+=1

def capture_image(drone, time_val, folder):
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_val))
    img = drone.get_frame_read().frame
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite(f'{folder}/{formatted_time}.jpg', img_rgb)