import re
from collections import Counter

# Define the log file path
log_file_path = 'web_server.log'

# Define regex for parsing the log lines
log_pattern = re.compile(r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - \[(?P<date>.*?)\] "(?P<request>.*?)" (?P<status>\d{3}) (?P<size>\d+|-) "(?P<referrer>.*?)" "(?P<agent>.*?)"')

# Initialize counters
status_counter = Counter()
page_counter = Counter()
ip_counter = Counter()
not_found_counter = 0

# Read and parse the log file
with open(log_file_path, 'r') as log_file:
    for line in log_file:
        match = log_pattern.match(line)
        if match:
            data = match.groupdict()
            ip = data['ip']
            request = data['request'].split()
            status = data['status']
            page = request[1] if len(request) > 1 else '-'
            
            # Update counters
            status_counter[status] += 1
            page_counter[page] += 1
            ip_counter[ip] += 1
            if status == '404':
                not_found_counter += 1

# Print the summarized report
print("Web Server Log Analysis Report")
print("==============================")
print(f"Total number of requests: {sum(status_counter.values())}")
print(f"Number of 404 errors: {not_found_counter}")
print("\nTop 10 most requested pages:")
for page, count in page_counter.most_common(10):
    print(f"{page}: {count} requests")

print("\nTop 10 IP addresses with the most requests:")
for ip, count in ip_counter.most_common(10):
    print(f"{ip}: {count} requests")
