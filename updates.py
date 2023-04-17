import psutil
import socket
import csv

def updates():

# Obtain CPU temperature, memory usage percentage and PC Name
    cpu_temp = psutil.sensors_temperatures()['coretemp'][0].current
    mem_usage = psutil.virtual_memory().percent
    pc_name = socket.getfqdn()

# Adding the data into a list
    data = [pc_name, cpu_temp, mem_usage]

# Open a file with the absolute path and writing the data into it
    file_path = "/Users/username/Documents/my_file.csv"
    with open(file_path, 'a') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

