# pythonprocess
Getting some information about the current process, once run in a Linux VM with Vagrant and once in Docker.
Fetching the information using two different methods:
1) using the os library to fetch current PID
2) using /proc/self directory

# Running the script
### With vagrant

cd /vagrant

python3 pythonprocess.py

### With docker
docker build and run

# Results
__Vagrant__
![image](https://github.com/justcallmeRyan/pythonprocess/assets/74745341/775ca8cd-2264-47ff-a635-e14a46c9a778)

__Docker__
![image](https://github.com/justcallmeRyan/pythonprocess/assets/74745341/01ab0e38-a501-47b5-9fc0-0eb7f97b43a4)


