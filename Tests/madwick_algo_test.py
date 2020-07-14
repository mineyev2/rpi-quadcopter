import time
import ahrs
import numpy as np
from ahrs import Quaternion

import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c
i2c = busio.I2C(board.SCL, board.SDA)
fxos = adafruit_fxos8700.FXOS8700(i2c)
fxas = adafruit_fxas21002c.FXAS21002C(i2c)

'''
print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxos.accelerometer))
print('Magnetometer (uTesla): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxos.magnetometer))
print('Gyroscope (radians/s): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*fxas.gyroscope))
'''

madgwick = ahrs.filters.Madgwick()

Q = [1., 0., 0., 0.]

time_passed = 0
d2g = ahrs.common.DEG2RAD

while True:
    start_time = time.time()

    gyroscope_radians = [g * d2g for g in fxas.gyroscope]
    madgwick.Dt = time_passed
    Q = madgwick.updateMARG(Q, gyroscope_radians, fxos.accelerometer, fxos.magnetometer)    

    time.sleep(1)
    end_time = time.time()

    time_passed = end_time - start_time
    
    DCM = Quaternion(Q).to_DCM()
    angles = Quaternion(Q).to_angles()

    print(angles)
    #print("time passed: " + str(time_passed))


