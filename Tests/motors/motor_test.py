import pigpio
import time

motor_gpios = [17, 27, 22]

pi = pigpio.pi()

for i in motor_gpios:
    pi.set_mode(i, pigpio.OUTPUT)

#pi.set_servo_pulsewidth(27, 2000)
#time.sleep(1)

for i in motor_gpios:
    pi.set_servo_pulsewidth(i, 0)
time.sleep(3)
for i in motor_gpios:
    pi.set_servo_pulsewidth(i, 1000)
time.sleep(3)
#pi.set_servo_pulsewidth(27, 2000)
#time.sleep(3)

for i in range(0, 5):
    for j in motor_gpios:
        pi.set_servo_pulsewidth(j, (1000 + i * 100))
        print("set to: ",pi.get_servo_pulsewidth(27))
    time.sleep(1)
#pi.stop()

for i in motor_gpios:
    pi.set_servo_pulsewidth(i, 0)

