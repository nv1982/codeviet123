import re

# Path to the Apache access log file
log_file_path = 'C:/xampp/apache/logs/access.log'  # Adjust the path as necessary

def parse_apache_log(file_path):
    connections = {}
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Regex to match IP addresses
                match = re.match(r'(\d+\.\d+\.\d+\.\d+)', line)
                if match:
                    ip_address = match.group(1)
                    if ip_address not in connections:
                        connections[ip_address] = 0
                    connections[ip_address] += 1
    except FileNotFoundError:
        print(f"Log file not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return connections

# Parse the Apache log and print the IP connections
connections = parse_apache_log(log_file_path)
print("IP Addresses accessing phpMyAdmin:")
for ip, count in connections.items():
    print(f"IP: {ip}, Access Count: {count}")
