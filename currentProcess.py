import os
import json

# Empty dictionary to store results in
dict_output = {}

# Get the current PID with the help of OS module, Get the current PID with the help of /proc/self
current_pid = os.getpid()
self_current_pid = f"/proc/self/task"

# Path to fd directory
pid_path_fd = f"/proc/{current_pid}/fd"
self_path_fd = f"/proc/self/fd"

# Path to status file
pid_path_status = f"/proc/{current_pid}/status"
self_path_status = f"/proc/self/status"

# Path to CPU and MEM info
cpuinfo_path = "/proc/cpuinfo"
meminfo_path = "/proc/meminfo"


# grep function, output is what is saved in the dictionary
def grep(path, search, output=None):
    with open(path) as origin_file:
        for line in origin_file:
            if line.startswith(search):
                found = line.split()[1] + line.split()[2]
                print(found)
                if output:
                    dict_output[output] = found
                    break


def print_line():
    print("#######################################################################\n")


################################################
############# CURRENT PROCESS INFO #############
################################################

# Print PID
print(f"The current process ID FROM OS is {current_pid}")
print(f"The current process ID FROM SELF is {os.listdir(self_current_pid)}")
print_line()
dict_output["PID"] = str(current_pid)

# Print FDs
print(f"FD from oslistdir{os.listdir(pid_path_fd)}")
print(f"FD from proc/self {os.listdir(self_path_fd)} ")
print_line()
dict_output["FDs"] = os.listdir(pid_path_fd)


# grep VmRSS from status file (memory that is held in RAM)
print("MEMORY USAGE from /self/status")
grep(self_path_status, "VmRSS:", "Memory used")

print("MEMORY USAGE from /pid/status")
grep(pid_path_status, "VmRSS:")
print_line()


################################################
################ SYSTEM INFO ###################
################################################

print(f"CPU info from /proc/cpuinfo")
with open(cpuinfo_path) as origin_file:
    for line in origin_file:
        if line.startswith("model name"):
            model_name = line.split(":", 1)[1].strip()
            print(model_name)
            dict_output["CPU Model"] = model_name
        if line.startswith("cpu cores"):
            cores = line.split()[3]
            print(f"amount of cores = {cores}")
            dict_output["CPU cores"] = cores
            break

print(f"System Total memory from /proc/meminfo")
grep(meminfo_path, "MemTotal:", "System Total RAM")
print_line()

# Dump results to JSON
json_output = json.dumps(dict_output)
print(json_output)
