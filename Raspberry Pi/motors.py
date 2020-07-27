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

    def initialize_motors(self):
        for i in self.motor_gpios:
            self.pi.set_servo_pulsewidth(i, 0)
        time.sleep(3)

        for i in self.motor_gpios:
            self.pi.set_servo_pulsewidth(i, 1000)
        time.sleep(3)
        print("Motors initialized!")

        #listen for beeping to guarantee that the ESCs have initialized

    def set_motor_speeds(self, speeds):
        #speeds list must be the same size as the number of motors
        assert(len(speeds) == self.num_motors)

    def turn_motors_off(self):
        for i in self.motor_gpios:
            self.pi.set_servo_pulsewidth(i, 0)

    def calibrate(self):
        # need to figure out how to calibrate eventually, keeping blank for now
        return
