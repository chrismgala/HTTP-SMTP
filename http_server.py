# Import everything from socket module for network communication
# Also import 'threading' to allow multithreading
from socket import *
import threading

# Create socket with AF_INET (IPv4) address family and SOCK_STREAM protocol
serverSocket = socket(AF_INET, SOCK_STREAM)

# Set serverName to 'localhost'
# Also set the serverPort to 6789
# Then tell the socket to start listening for incoming connections
serverPort = 6789
serverSocket.bind(('localhost', serverPort))
serverSocket.listen(1);

## Threading target function that will run when there is an incoming connection
def service_Request(connectionSocket, addr):
	try:
		# Decode bits received from the connectionSocket and allow at most 1024 bits from the incoming connection
		message = connectionSocket.recv(1024).decode()

		# Extract the filename (if there is one) in message
		# If there is no filename, then 'IOError' will get raised
		filename = message.split()[1]

		# If there was indeed a file, open it
		f = open(filename[1:], "rb")

		# Read the file contents
		outputdata = f.read()

		# Send one HTTP header line response back into socket
		connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n'.encode())

		# Send the content of the requested file to the client as a response
		for i in range(0,len(outputdata)):
			connectionSocket.send(outputdata[i:i+1])
		connectionSocket.send(b'\r\n\r\n')

		print('Data sent')

		# Close the connected socket
		connectionSocket.close()

	except IOError:

		# Send response message for file not found
		connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())

		# Open the go-to HTML file for '404 - Not Found' errors
		f = open("404.html", "rb")

		# Read the contents of '404.html' file
		errorMessage = f.read()

		# Output the contents of '404.html' to the client as a response
		for i in range(0,len(errorMessage)):
			connectionSocket.send(errorMessage[i:i+1])
		connectionSocket.send(b'\r\n\r\n')

		# Close client socket
		connectionSocket.close()

while True:
	# Establish the connection and let user know server is ready
	print ("Ready to serve...")

	# Setup TCP connection using accept()
	connectionSocket, addr = serverSocket.accept()

	# Create new Thread with the target function 'service_Request' and its corresponding parameters
	t = threading.Thread(target=service_Request, args = (connectionSocket, addr))
	t.daemon = True

	# Start the thread
	t.start()

# Close the main server socket
serverSocket.close()
