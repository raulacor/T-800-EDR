import psutil
import time
import logging

logging.basicConfig(filename="edr_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")
SUSPICIUS_PROCESSES = {"mimikatz.exe", "darkcometer.exe", "meterpreter.exe"}

def get_running_processes ():
    return {p.info['name'] for p in psutil.processes_iter(attrs=['name'])}

def main():
    print("EDR started. Monitoring processes. . . ")
    old_processes = get_running_processes()
    
while True:
    time.sleep(3)
    new_processes = get_running_processes

    started_processes = get_running_processes - old_processes()
    for process in started_processes: 
