import numpy as np
import djitellopy as tello
import cv2 as cv2
import pandas
import torch
import time

model = torch.hub.load('ultralytics/yolov5', 'yolov5s.pt')
