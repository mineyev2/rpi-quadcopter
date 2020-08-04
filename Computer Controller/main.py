import pygame
import time

from controller import Controller
from client_test import Client



if __name__ == "__main__":

    client = Client()
    client.connect()
    time.sleep(1)


    #client.send_msg(b'connected')

    pygame.init()
    pygame.joystick.init()

    clock = pygame.time.Clock()

    done = False

    mac_controller = Controller()

    initialized = False
    while not initialized:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        buttons = mac_controller.get_buttons()
        if(buttons[4] == 1):
            print("Initializing...")
            client.send_msg(b'00000000000000')
            initialized = True
        clock.tick(30)


    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        left_joystick = mac_controller.get_left_stick()
        right_joystick = mac_controller.get_right_stick()
        #print(left_joystick, " " , right_joystick)

        left_to_send = [format(int((i + 1) * 100), '03d') for i in left_joystick]
        right_to_send = [format(int((i + 1) * 100), '03d') for i in right_joystick]
        to_send = '01'
        to_send += left_to_send[0] + left_to_send[1] + right_to_send[0] + right_to_send[1]
        to_send = to_send.encode()
        #print(to_send)
        client.send_msg(to_send)

        clock.tick(30)

        #done = True
'''
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

'''