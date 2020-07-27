# Import socket module
import socket

class Client:
    def __init__(self, name='Roman', ip='192.168.1.159'):
        self.name = name
        self.ip = ip
        self.port = 12346

        self.s = socket.socket()

    def connect(self):
        self.s.connect((self.ip, self.port))

    def send_msg(self, data):
        #make sure data is a byte literal
        self.s.send(data)

    def receive_msg(self):
        data = self.s.recv(1024)
        return data

    def close_port(self):
        self.s.close()


'''
# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12346

# connect to the server on local computer
s.connect(('192.168.1.159', port))

# receive data from the server
print(s.recv(1024))
# close the connection

s.send(b'Hello')

#while True:
    #s.send(b'Hello')
'''