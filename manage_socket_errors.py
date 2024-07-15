import socket
import sys

# Set the host and port
host = "domain/ip_address"
port = 80

try:
    # Create a TCP/IP socket
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created:", mysocket)
    mysocket.settimeout(5)  # Set timeout for blocking socket operations
except socket.error as e:
    print("Socket creation error: %s" % e)
    sys.exit(1)

try:
    # Connect the socket to the server
    mysocket.connect((host, port))
    print("Socket connected:", mysocket)
except socket.timeout as e:
    print("Connection timed out: %s" % e)
    sys.exit(1)
except socket.gaierror as e:
    print("Address-related error connecting to server: %s" % e)
    sys.exit(1)
except socket.error as e:
    print("Connection error: %s" % e)
    sys.exit(1)
finally:
    mysocket.close()  # Ensure the socket is closed properly
    print("Socket closed")
