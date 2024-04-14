import csv
import os

class logger:
    def __init__(self, confidence, time):
        self.confidence = confidence
        self.time = time

    def create_csv(self, base_filename):
        i = 0
        while True:
            filename = f"{base_filename}{i}.csv"
            if not os.path.isfile(filename):
                break
            i+= 1
        
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Confidence', 'Time'])
        
        return filename

    def log(self, filename):
        with open(filename, 'a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([self.confidence, self.time])