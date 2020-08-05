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
        In charge of all the messages sent to the quadcopter
        :return:
        '''

        '''
        If message starts with:
            • 01: send data to motor
            • 02: update sensitivity of motors (values are from 1-10)
            • blank message: do nothing
            • else: print "message is invalid"
        '''
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

    def motor_command(self, joystick_readings):
        '''
        Convert the joystick readings to specific speed updates for each motor
        :param joystick_readings:
        :return:
        '''

        #dont forget each joystick reading is incremented by 100

        print("running motor command:", joystick_readings)
        return

    def sensitivity_update(self, sensitivity_value):
        print("running sensitivity update: ", sensitivity_value)
        return