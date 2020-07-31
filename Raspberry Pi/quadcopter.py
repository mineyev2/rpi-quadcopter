from motors import Motors
from marg import MARG
from server_test import Server

'''
This Quadcopter class will combine all the code running on the pi into one so everything is more manageable
'''
class Quadcopter:
    def __init__(self):
        self.motors = Motors()
        self.marg = MARG()
        # not sure if I want this here, but will add for now
        self.server = Server()

    def decipher_msg(self):
        '''
        runs certain functions depending on message type
        :return:
        '''

        '''
        If message starts with:
            • 0: idk
            • 1: send data to motor
            • 2: update sensitivity of motors (values are from 1-10)
        '''
        #TODO: figure out key and sending scheme and header size and message sizes

        return