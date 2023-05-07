#!/bin/python
import sys
import socket
from datetime import datetime
from colorama import Fore, Back
# print("hello git test")

#Define Target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate host name to ipv4
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 scanner.py <ip>")

# python3 scanner.py <ip>

#add a pretty banner

print('-' * 50)
print('Scanning Target' + target)
print("Time Started:" + str(datetime.now()))
print('-' * 50)

try:
    for port in range(1,250):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns an error indicator
        print(f"Scanning port {port}")
        if result == 0:
            print(Fore.RED + f"Port {port} is open" + Fore.RESET)
        s.close()

except KeyboardInterrupt:
    print("Scan interrupted")
    print("Exiting Program")
    sys.exit()

except socket.gaierror:
    print("Hostname was not resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()