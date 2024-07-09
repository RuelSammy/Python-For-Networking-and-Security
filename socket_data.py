import socket  # Import the socket module

print('creating socket ...')
# Create a socket object using IPv4 and TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')

print("connection with remote host")
# Define the target host and port
target_host = "www.google.com"
target_port = 80

# Connect to the target host and port
s.connect((target_host, target_port))
print('connection ok')

# Create an HTTP GET request string
request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target_host
# Send the request to the server, encoding it to bytes
s.send(request.encode())

# Receive the response data from the server (up to 4096 bytes)
data = s.recv(4096)
# Print the received data and its length
print("Data:", str(bytes(data)))
print("Length:", len(data))

print('closing the socket')
# Close the socket connection
s.close()
