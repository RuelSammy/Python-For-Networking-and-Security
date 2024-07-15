import socket
import sys
from datetime import datetime
import errno

# Get user input for remote host and port range
remote_server = input("Enter a remote host to scan: ")

# Resolve the remote host to an IP address
try:
    remote_server_ip = socket.gethostbyname(remote_server)
except socket.gaierror:
    print("Hostname could not be resolved. Exiting.")
    sys.exit()

# Get the range of ports to scan
while True:
    try:
        start_port = int(input("Enter a start port: "))
        end_port = int(input("Enter an end port: "))
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            raise ValueError
        break
    except ValueError:
        print("Please enter valid port numbers (1-65535) and ensure the start port is less than or equal to the end port.")

print(f"Please wait, scanning remote host {remote_server_ip} from port {start_port} to {end_port}")
time_init = datetime.now()

# Function to scan ports
def scan_ports(remote_server_ip, start_port, end_port):
    try:
        for port in range(start_port, end_port + 1):
            print(f"Checking port {port} ...")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((remote_server_ip, port))
            if result == 0:
                print(f"Port {port}: \t Open")
            else:
                print(f"Port {port}: \t Closed")
                if result in errno.errorcode:
                    print("Reason:", errno.errorcode[result])
            sock.close()
    except KeyboardInterrupt:
        print("\nYou pressed Ctrl+C")
        sys.exit()
    except socket.error as e:
        print(f"Socket error: {e}")
        sys.exit()

# Perform the scan
scan_ports(remote_server_ip, start_port, end_port)

# Measure and print the duration of the scan
time_finish = datetime.now()
total = time_finish - time_init
print('Port Scanning Completed in:', total)
