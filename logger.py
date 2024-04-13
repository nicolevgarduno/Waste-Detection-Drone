import csv
import logging
import logging.handlers
import os

class logger:
    def __init__(self, type, confidence, time):
        self.type = type
        self.confidence = confidence
        self.time = time

    def create_csv(filename):
        shoudl_roll_over = os.path.isfile(filename)
        handler = logging.handlers.RotatingFileHandler(filename, mode='w', backupCount=5)
        if shoudl_roll_over:
            handler.doRollover()