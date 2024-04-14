import csv
import os
import time

def create_csv():
    i = 0
    while True:
        filename = f"run{i}.csv"
        if not os.path.isfile(filename):
            break
        i+= 1
        
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Confidence', 'Time'])
        
    return filename

def log_csv(filename, time_val, confidence):
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_val))
    with open(filename, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([confidence, formatted_time])