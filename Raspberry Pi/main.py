from server_test import Server
from motors import Motors
import pygame

def message_to_motor_speeds(msg):
    speeds = []
    if(len(msg) != 4):
        return
    for i in msg:
        if(i ==49):
            speeds.append(1)
        else:
            speeds.append(0)
    print(speeds)
    return speeds

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

    motors.initialize()

    previous_msg = b''
    while True:
        client_msg = server.client_msg
        if(previous_msg != client_msg):
            previous_msg = client_msg



            #reads when the message changes, might not be a good idea but we'll stick w that for now
            print(server.client_msg)
