#!/bin/python
import sys
import socket
from datetime import datetime
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

