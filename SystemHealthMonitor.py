import psutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Set thresholds
CPU_THRESHOLD = 80.0  # CPU usage percentage
MEMORY_THRESHOLD = 80.0  # Memory usage percentage
DISK_THRESHOLD = 80.0  # Disk usage percentage
PROCESS_THRESHOLD = 100  # Number of running processes

def log_alert(message):
    print(message)
    logging.info(message)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"ALERT: High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"ALERT: High memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"ALERT: High disk usage detected: {disk_usage}%")
    return disk_usage

def check_running_processes():
    processes = len(psutil.pids())
    if processes > PROCESS_THRESHOLD:
        log_alert(f"ALERT: High number of running processes detected: {processes}")
    return processes

def main():
    while True:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cpu_usage = check_cpu_usage()
        memory_usage = check_memory_usage()
        disk_usage = check_disk_usage()
        running_processes = check_running_processes()

        log_alert(f"System Health Check at {current_time}: CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%, Processes: {running_processes}")

if __name__ == '__main__':
    main()
