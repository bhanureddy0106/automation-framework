import csv
import time

def log_performance(test_name, duration):
    with open("performance_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([test_name, duration, time.ctime()])