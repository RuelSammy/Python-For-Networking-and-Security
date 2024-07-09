import socket  # Import the socket module

# Define the web host and port to connect to
webhost = 'localhost'
webport = 8080

# Print a message indicating the target host and port
print("Contacting %s on port %d ..." % (webhost, webport))

# Create a socket object using IPv4 and TCP
webclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the specified web host and port
webclient.connect((webhost, webport))

# Create an HTTP GET request string
request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"

# Send the HTTP GET request to the server
webclient.send(request.encode('utf-8'))

# Receive the response data from the server (up to 4096 bytes)
reply = webclient.recv(4096)

# Print the response from the server
print("Response from %s:" % webhost)
print(reply.decode())

# Close the socket connection
webclient.close()
