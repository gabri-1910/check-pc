import psutil
import socket
import csv
from datetime import datetime

# Obtain CPU temperature, memory usage percentage and PC Name

mem_usage = psutil.virtual_memory().percent
pc_name = socket.getfqdn()
disk = psutil.disk_usage('/')
disk_round = round((disk[2] / disk[0]) * 100)
cpu_usage = psutil.cpu_percent()
now = datetime.now()
date = now.strftime("%d/%m/%Y %H:%M:%S")

# Adding the data into a list
data = [pc_name, disk_round, mem_usage, cpu_usage, date]

# Open a file with the absolute path and writing the data into it
file_path = (r'\\kyvia\Intalação\testes\updates.csv')
with open(file_path, 'a') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(data)