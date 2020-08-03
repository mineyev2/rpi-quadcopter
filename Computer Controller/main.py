import pygame
import time

from controller import Controller
from client_test import Client



if __name__ == "__main__":

    client = Client()
    client.connect()
    time.sleep(1)


    client.send_msg(b'connected')

    pygame.init()
    pygame.joystick.init()

    clock = pygame.time.Clock()

    done = False

    mac_controller = Controller()

    initialized = False
    while not initialized:
        buttons = mac_controller.get_buttons()
        if(buttons[4] == 1):
            print("Initializing...")
            client.send_msg(b'00000000000000')
            initialized = True

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        buttons = mac_controller.get_buttons()

        A = buttons[11]
        B = buttons[12]
        X = buttons[13]
        #Y = buttons[14]

        to_send = b''
        for i in range(3):
            to_send += str(buttons[11 + i]).encode('utf-8')
        #print(to_send)
        client.send_msg(to_send)

        clock.tick(30)

