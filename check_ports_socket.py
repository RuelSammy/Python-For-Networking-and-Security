import socket
import sys

def check_ports_socket(ip, portlist):
    """
    Check the status of multiple ports on a given IP address.
    
    Args:
    ip (str): The IP address to check.
    portlist (list): A list of ports to check.
    """
    for port in portlist:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port}: \t Open")
            else:
                print(f"Port {port}: \t Closed")
        except socket.error as error:
            print(f"Error checking port {port}: {error}")
        finally:
            sock.close()

# Example usage
check_ports_socket('localhost', [21, 22, 80, 8080, 443])
