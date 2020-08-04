# first of all import the socket library
import socket
import threading


class Server:
    def __init__(self, name="rpi-quadcopter", ip='192.168.1.159'):
        self.msg_size = 14
        self.name = name
        self.ip = ip
        self.port = 12344
        self.s = socket.socket()
        self.client_msg = b''
        self.prev_msg = b''
        self.new_msg = True

    def start_server(self):
        # Next bind to the port
        # we have not typed any ip in the ip field
        # instead we have inputted an empty string
        # this makes the server listen to requests
        # coming from other computers on the network
        self.s.bind(('', self.port))
        print("socket binded to %s" % (self.port))

        # put the socket into listening mode
        self.s.listen(1)
        print("socket is listening")

    def accept_connections(self):
        self.c, self.addr = self.s.accept()
        print('Got connection from', self.addr)

    def listen_in_parallel(self):
        listen_thread = threading.Thread(target=self.listen)
        listen_thread.start()

    def listen(self):

        #change this later so that the messages aren't combined (specify message size)
        print("Socket is now waiting for message")
        while True:
            client_text = self.c.recv(self.msg_size)
            if (client_text != b''):
                # updates the client message
                self.client_msg = client_text
                if(self.prev_msg != self.client_msg):
                    self.prev_msg = self.client_msg
                    self.new_msg = True
                else:
                    self.new_msg = False

