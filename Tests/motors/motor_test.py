import pigpio
import time

pi = pigpio.pi()
pi.set_mode(27, pigpio.OUTPUT)

#pi.set_servo_pulsewidth(27, 2000)
#time.sleep(1)
pi.set_servo_pulsewidth(27, 0)
time.sleep(3)
pi.set_servo_pulsewidth(27, 1000)
time.sleep(3)
#pi.set_servo_pulsewidth(27, 2000)
#time.sleep(3)
pi.set_servo_pulsewidth(27, 1200)
print("set to: ",pi.get_servo_pulsewidth(27))

time.sleep(5)
#pi.stop()

pi.set_servo_pulsewidth(27, 0)
