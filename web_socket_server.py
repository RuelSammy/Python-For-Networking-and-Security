from aiohttp import web
import socketio

# Create a new AsyncServer instance
socket_io = socketio.AsyncServer()

# Create a new web application instance
app = web.Application()

# Attach the socket.io server to the web application
socket_io.attach(app)

# Define an asynchronous function to handle requests to the root URL
async def index(request):
    return web.Response(text='Hello world from socketio', content_type='text/html')

# Define an event handler for the 'message' event
@socket_io.on('message')
def print_message(socket_id, data):
    print("Socket ID:", socket_id)
    print("Data:", data)

# Add a route to the web application to handle GET requests to the root URL
app.router.add_get('/', index)

# Run the web application if this script is executed directly
if __name__ == '__main__':
    web.run_app(app)
