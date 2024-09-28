import re
from datetime import datetime
from collections import defaultdict

# Path to the access log file
log_file_path = 'C:\\xampp\\apache\\logs\\access.log'  # Adjust the path accordingly

def parse_log_file(file_path):
    access_count = defaultdict(int)  # Dictionary to count access by IP

    # Regular expression to match log lines
    log_pattern = re.compile(
        r'(?P<ip>[\d\.]+) - - \[(?P<timestamp>.+?)\] "(?P<method>\w+) (?P<path>.+?) HTTP/\d\.\d" (?P<status>\d+) (?P<size>\d+) "(?P<referrer>[^"]+)" "(?P<user_agent>[^"]+)"'
    )

    with open(file_path, 'r') as file:
        for line in file:
            match = log_pattern.match(line)
            if match:
                ip = match.group('ip')
                timestamp = match.group('timestamp')

                # Increment the count for this IP
                access_count[ip] += 1

    return access_count

if __name__ == '__main__':
    access_logs = parse_log_file(log_file_path)
    
    # Print the counts for each IP
    print("IP Address Access Counts:")
    for ip, count in access_logs.items():
        print(f"IP: {ip}, Access Count: {count}")
