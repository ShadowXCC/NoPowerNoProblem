#This program has been built to run on raspberry pis loaded up 32 bit linux operating systems

#linux dependencies: python3

#python dependencies: pyserial, paramiko

import paramiko
import serial
import os.path
from datetime import datetime

#open serial connection
"""ser = serial.Serial() #open serial port
"""
#loop until command gets sent over serial, and break out of the loop when it does

file = open("parameters.txt", "r")
#print(file.read() + "\n")

#read parameters.txt file, and save values
hostNames = []
ports = []
usernames = []
passwords = []

for line in file:
    #print(line)
    if "host=" in line:
        hostNames.append(line.split("=")[1].strip().strip('"'))
    if "port=" in line:
        ports.append(line.split("=")[1].strip().strip('"'))
    if "username=" in line:
        usernames.append(line.split("=")[1].strip().strip('"'))
    if "password=" in line:
        passwords.append(line.split("=")[1].strip().strip('"'))


hostNames = list(filter(None, hostNames))
ports = list(filter(None, ports))
usernames = list(filter(None, usernames))
passwords = list(filter(None, passwords))

#check if all lists have the same amount of values stored
hostNamesLength = len(hostNames)
portsLength = len(ports)
unLength = len(usernames)
passLength = len(passwords)
listAve = int((hostNamesLength + portsLength + unLength + passLength)/4)

if (listAve != hostNamesLength) or (listAve != portsLength) or (listAve != unLength) or (listAve != passLength):
    exit("There is an issue with \"parameters.txt\"")

#generate logs on shutdowns
"""
cwd = os.getcwd()
if os.path.isdir(cwd + "/logs") == False:
    os.mkdir(cwd + "/logs")

for i in range(0, listAve):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostNames[i], ports[0], usernames[i], passwords[i])
    
    ssh.exec_command(shutdownCommand)
    transport = ssh.get_transport()
    session = transport.open_session()
    stdin = session.makefile('wb', -1)
    stdout = session.makefile('rb', -1)
    try:
        stdin.write(passwords[0] +'\n')
    except OSError:
        #write to log
        logfile = open("logs/" + datetime.now().strftime(hostNames[i] + "_%d-%m-%Y-%H:%M:%S") + ".log", "w")
        logfile.write("\"" + hosts[i] + "\" shutdown successfully")
"""