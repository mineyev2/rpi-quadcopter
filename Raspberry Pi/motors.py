import pigpio
import time

'''
BLHeli firmware settings:
https://github.com/4712/BLHeliSuite/blob/master/Manuals/BLHeli_S%20manual%20SiLabs%20Rev16.x.pdf
'''

class Motors:
    def __init__(self):
        self.motor_gpios = [17, 27, 22, 23]
        self.num_motors = len(self.motor_gpios)
        self.sensitivity = 1
        self.pi = pigpio.pi()

        for i in self.motor_gpios:
            self.pi.set_mode(i, pigpio.OUTPUT)

    def initialize(self):
        '''
        Initializes the ESCs. Without sending set pulse-width signals to the ESCs, the motors will not run
        After running initializations, then the motors can be set to any speed we desire
        :return:
        '''

        print("Initializing motors...")

        # sequence of PWMs required for BLHeli firmware to "unlock" the ESCs
        # turning off once just in case
        self.turn_off()
        time.sleep(3)
        for i in self.motor_gpios:
            self.pi.set_servo_pulsewidth(i, 1000)
        time.sleep(5)
        self.turn_off()
        time.sleep(5)
        for i in self.motor_gpios:
            self.pi.set_servo_pulsewidth(i, 1300)
        time.sleep(2)
        '''
        for i in self.motor_gpios:
            self.pi.set_servo_pulsewidth(i, 1000)
        time.sleep(5)
        '''
        #self.turn_off()
        print("Motors initialized!")

        #listen for beeping to guarantee that the ESCs have initialized

    def calibrate(self, min, max):
        '''
        Calibrates ESCs and sets the minimum and maximum pulse-widths that will be sent over from the raspberry pi
        Will usually set min=1000, max=2000 as default, so not exactly necessary here
        (see the github link at the top for more info on BLHeli firmware configuation)s

        :param min: minimum throttle pulse-width
        :param max: maximum throttle pulse-width
        :return:
        '''

        print("Calibrating motors...")
        # TODO: check if calibration sequence is working

        for i in self.motor_gpios:
            self.pi.set_servo_pulsewidth(i, 1000)
        time.sleep(5)
        for i in self.motor_gpios:
            self.pi.set_servo_pulsewidth(i, max)
        time.sleep(5)
        for i in self.motor_gpios:
            self.pi.set_servo_pulsewidth(i, min)
        time.sleep(5)
        print("Motors calibrated!")




    def set_speeds(self, speeds):
        '''
        function to set speeds of each motor
        Will be called each time there is an update in any of the 3 motor speeds

        :param speeds: array of speeds, element values range from 0-100 (to symbolize percentages of full power)
        :return:
        '''

        # TODO: if only changing one of the motor speeds instead of all 4, this might be inefficient.
        # TODO: Should look into whether there is a way to simplify this or not

        #speeds list must be the same length as the number of motors
        assert(len(speeds) == self.num_motors), "speeds array contains wrong number of elements"


        for i in range(self.num_motors):
            #convert from motor speed percentage to signal PWM
            # 1000 is min thrust, 2000 is max thrust
            pulse_width = 1000 + int(speeds[i] * 10)
            assert(pulse_width <= 2000), "pulse width is too large!"
            self.pi.set_servo_pulsewidth(self.motor_gpios[i], pulse_width)


    def turn_off(self):
        '''
        turns off the motors
        :return:
        '''
        for i in self.motor_gpios:
            self.pi.set_servo_pulsewidth(i, 0)
