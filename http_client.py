# Import everything from socket module for network communication
# Also import 'sys' for command line arguments
from socket import *
import sys

# Set serverName to 'localhost' (this is the same server used by the webserver_skeleton.py file)
# Also set the serverPort to 6789 (again, same as port specified in server file)
serverName = sys.argv[1]
serverPort = int(sys.argv[2])
fileName = sys.argv[3]

# Create socket with AF_INET (IPv4) address family and SOCK_STREAM protocol
clientSocket = socket(AF_INET, SOCK_STREAM)

# Startup TCP connection between client and server - 3 way handshake established
clientSocket.connect((serverName, serverPort))

# Send an HTTP GET request to the server
request = "GET /" + fileName + " HTTP/1.1\r\n"
clientSocket.send(request.encode())

# First get header
# Then take in any file data (up to 1024 bits) from the server through the clientSocket
response = clientSocket.recv(1024)
while '</html' not in response.decode():
    response += clientSocket.recv(1024)

# Print out decoded bit-reponse from server
print("From server:", response.decode())

# Close the socket
clientSocket.close()
