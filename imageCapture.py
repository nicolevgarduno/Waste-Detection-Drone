import djitellopy as tello
import cv2
import time

class imageCapture:
    def __init__(self, drone, time):
        self.drone = drone
        self.time = time

    def capture_image(self):
        img = self.drone.get_frame_read().frame
        cv2.imwrite(f'{self.time}.jpg', img)
