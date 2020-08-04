#from motors import Motors
#from marg import MARG
from server_test import Server

'''
This Quadcopter class will combine all the code running on the pi into one so everything is more manageable
'''
class Quadcopter:
    def __init__(self):
        #self.motors = Motors()
        #self.marg = MARG()
        # not sure if I want this here, but will add for now
        self.server = Server()

        self.prev_msg = b''

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
        #TODO: set it so same messages don't get repeated

        if(self.prev_msg != self.server.client_msg):
            self.prev_msg = self.server.client_msg

            if(self.server.client_msg[:2] == b'01'):
                status = self.motor_command(self.server.client_msg[2:])
                return status
            elif(self.server.client_msg[:2] == b'02'):
                status = self.sensitivity_update(self.server.client_msg[2:])
                return status
            elif(self.server.client_msg == b''):
                return
            else:
                print("invalid message")
                return
        # once the message is read, set it so that it doesn't get read again
        #self.server.new_msg = False

    def motor_command(self, joystick_readings):
        print("running motor command:", joystick_readings)
        return

    def sensitivity_update(self, sensitivity_value):
        print("running sensitivity update: ", sensitivity_value)
        return