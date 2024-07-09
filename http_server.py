import socket  # Import the socket module

# Create a socket object using IPv4 and TCP
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to localhost on port 8080
mySocket.bind(('localhost', 8080))

# Listen for incoming connections (up to 5 connections in the queue)
mySocket.listen(5)

while True:
    print('Waiting for connections')
    # Accept an incoming connection
    (recvSocket, address) = mySocket.accept()
    
    print('HTTP request received:')
    # Receive the HTTP request from the client (up to 1024 bytes)
    print(recvSocket.recv(1024))
    
    # Send an HTTP response to the client
    response = "HTTP/1.1 200 OK\r\n\r\n<html><body><h1>Hello World!</h1></body></html> \r\n"
    recvSocket.send(bytes(response, 'utf-8'))
    
    # Close the connection with the client
    recvSocket.close()
