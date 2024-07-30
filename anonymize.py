import socks
import socket

# Store original socket functions
temp_socket = socket.socket
temp_create_connection = socket.create_connection

def disable_proxy():
    """Restore original socket settings."""
    socket.socket = temp_socket
    socket.create_connection = temp_create_connection

def enable_proxy(host="127.0.0.1", port=9050):
    """Enable SOCKS5 proxy for socket connections."""
    def create_connection(address, timeout=None, source_address=None):
        sock = socks.socksocket()
        sock.connect(address)
        return sock

    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, host, port, True)
    socket.socket = socks.socksocket
    socket.create_connection = create_connection

# Example usage:
# Enable proxy
enable_proxy()

# Now any socket connection will use the proxy
import requests
response = requests.get('http://httpbin.org/ip')
print("IP via proxy:", response.text)

# Disable proxy
disable_proxy()

# Now socket connections will use the original settings
response = requests.get('http://httpbin.org/ip')
print("IP without proxy:", response.text)
