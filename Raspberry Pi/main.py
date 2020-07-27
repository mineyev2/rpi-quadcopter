from server_test import Server
from motors import Motors
import pygame

if __name__ == "__main__":
    server = Server()
    motors = Motors()
    server.start_server()
    server.accept_connections()
    server.listen_in_parallel()
    print("hello")

    #now here, decipher whatever the client sends so that the pi can run the motors
    initialized = False
    while not initialized:
        if(server.client_msg == b'1000'):
            initialized = True

    print("Initialized!")

    previous_msg = b''
    while True:
        client_msg = server.client_msg
        if(previous_msg != client_msg):
            previous_msg = client_msg



            #reads when the message changes, might not be a good idea but we'll stick w that for now
            print(server.client_msg)
