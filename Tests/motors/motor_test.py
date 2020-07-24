import pigpio
import time

pi = pigpio.pi()
pi.set_mode(27, pigpio.OUTPUT)

print ("mode: ", pi.get_mode(27))
print("setting to: ",pi.set_servo_pulsewidth(27, 1500))
print("set to: ",pi.get_servo_pulsewidth(27))

time.sleep(1)
pi.stop()

pi.set_servo_pulsewidth(27, 0)
