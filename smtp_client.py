# Import everything from socket module for network communication
from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server)
mailServer = "localhost"
serverPort = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailServer, serverPort))

# ===================================================
# CONNECTION REPLY
# ===================================================
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
    clientSocket.close()

# ===================================================
# HELO COMMAND REQUEST (send) & RESPONSE (recv)
# ===================================================
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())

recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')
    clientSocket.close()

# ===================================================
# MAIL FROM COMMAND REQUEST (send) & RESPONSE (recv)
# ===================================================
MAIL_FROM = 'MAIL FROM: galac@uci.edu\r\n'
clientSocket.send(MAIL_FROM.encode())

recv2 = clientSocket.recv(1024).decode()
print(recv2)

if recv2[:3] != '250':
    print('250 reply not received from server.')
    clientSocket.close()

# ===================================================
# RCPT TO COMMAND REQUEST (send) & RESPONSE (recv)
# ===================================================
RCPT_TO = 'RCPT TO: galac@uci.edu\r\n'
clientSocket.send(RCPT_TO.encode())

recv3 = clientSocket.recv(1024).decode()
print(recv3)

if recv3[:3] != '250':
    print('250 reply not received from server.')
    clientSocket.close()

# ===================================================
# DATA COMMAND REQUEST (send) & RESPONSE (recv)
# ===================================================
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())

recv4 = clientSocket.recv(1024).decode()
print(recv4)

if recv4[:3] != '354':
    print('354 reply not received from server.')
    clientSocket.close()

# ===================================================
# MESSAGE + END MESSAGE (period)
# COMMAND REQUEST (send) & RESPONSE (recv)
# ===================================================
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())

recv5 = clientSocket.recv(1024).decode()
print(recv5)

if recv5[:3] != '250':
    print('250 reply not received from server.')
    clientSocket.close()

# ===================================================
# QUIT COMMAND REQUEST (send) & RESPONSE (recv)
# ===================================================
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())

recv6 = clientSocket.recv(1024).decode()
print(recv6)

if recv6[:3] != '221':
    print('221 reply not received from server.')
    clientSocket.close()
