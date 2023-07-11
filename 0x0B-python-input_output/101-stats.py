#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
Total file size: File size: <total size>
where is the sum of all previous
"""


import sys
import signal

# Dictionary to store the count of each status code
status_counts = {}

# Variable to store the total file size
total_file_size = 0

# Counter for the number of lines processed
line_count = 0

def print_statistics():
    print("Total file size:", total_file_size)
    for status_code in sorted(status_counts.keys()):
        print(status_code, ":", status_counts[status_code])

def signal_handler(signal, frame):
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Split the input line into its components
        parts = line.strip().split(" ")
        ip_address = parts[0]
        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update the total file size
        total_file_size += file_size

        # Update the status code count
        if status_code in status_counts:
            status_counts[status_code] += 1
        else:
            status_counts[status_code] = 1

        # Increment the line count
        line_count += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
