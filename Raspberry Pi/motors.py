import pigpio
import time

class Motors:
    def __init__(self):
        self.motor_gpios = [17, 27, 22]
        self.num_motors = len(self.motor_gpios)
        self.sensitivity = 1
        self.pi = pigpio.pi()

        for i in self.motor_gpios:
            self.pi.set_mode(i, pigpio.OUTPUT)

    def initialize(self):
        print("Initializing motors...")
        for i in self.motor_gpios:
            self.pi.set_servo_pulsewidth(i, 0)
        time.sleep(3)

        for i in self.motor_gpios:
            self.pi.set_servo_pulsewidth(i, 1000)
        time.sleep(3)
        for i in self.motor_gpios:
            self.pi.set_servo_pulsewidth(i, 0)
        print("Motors initialized!")

        #listen for beeping to guarantee that the ESCs have initialized

    def set_motor_speeds(self, speeds):
        '''
        function to set speeds of each motor

        :param speeds: array of speeds, element values range from 0-100 (to symbolize percentages)
        :return: nothing
        '''

        #speeds list must be the same size as the number of motors
        assert(len(speeds) == self.num_motors)

        for i in range(self.num_motors):
            #convert from percentage to signal PWM
            # 1000 is min thrust, 2000 is max thrust
            pulse_width = 1000 + speeds[i] * 10
            self.pi.set_servo_pulsewidth(self.motor_gpios[i], pulse_width)


    def turn_motors_off(self):
        for i in self.motor_gpios:
            self.pi.set_servo_pulsewidth(i, 0)

    def calibrate(self):
        # need to figure out how to calibrate eventually, keeping blank for now
        return
