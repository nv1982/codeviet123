import time
import re
from datetime import datetime

# Path to the Apache access log file
log_file_path = r'C:\xampp\apache\logs\access.log'  # Adjust the path as necessary

def parse_apache_log(file_path):
    connections = {}

    with open(file_path, 'r') as file:
        # Move the cursor to the end of the file
        file.seek(0, 2)
        while True:
            line = file.readline()
            if not line:
                # Sleep for a bit before checking for new lines
                time.sleep(1)
                continue
            
            # Adjusted regex to capture IP, timestamp, and URL accessed
            match = re.match(r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d+)', line)
            if match:
                ip_address = match.group(1)
                timestamp_str = match.group(2)
                request_line = match.group(3)  # This will capture the HTTP request line
                status_code = match.group(4)

                # Extract the requested URL from the request line (it may contain the HTTP method)
                requested_url = request_line.split(' ')[1]  # Split by space and take the second part (the URL)
                
                # Convert the timestamp to a datetime object (optional)
                timestamp = datetime.strptime(timestamp_str, "%d/%b/%Y:%H:%M:%S %z")

                # Log connection details
                if ip_address not in connections:
                    connections[ip_address] = (0, [], [])
                
                connections[ip_address] = (
                    connections[ip_address][0] + 1, 
                    connections[ip_address][1] + [timestamp],
                    connections[ip_address][2] + [requested_url]
                )
                
                # Print out the connection info
                print(f"IP: {ip_address}, Connections: {connections[ip_address][0]}, "
                      f"Last Access: {timestamp}, Last URL Accessed: {requested_url}")

if __name__ == "__main__":
    print("Monitoring access log for connections...")
    parse_apache_log(log_file_path)
