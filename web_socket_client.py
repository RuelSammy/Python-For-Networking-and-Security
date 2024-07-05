import socketio

# Create a new Client instance
sio = socketio.Client()

# Define event handlers
@sio.event
def connect():
    print('Connection established')

@sio.event
def disconnect():
    print('Disconnected from server')

# Connect to the server
sio.connect('http://localhost:8080')

# Emit a message to the server
sio.emit('message', {'data': 'my_data'})

# Wait for events
sio.wait()
