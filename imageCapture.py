import djitellopy as tello
import cv2
import time


def capture_image(drone, time):
    img = drone.get_frame_read().frame
    cv2.imwrite(f'{time}.jpg', img)