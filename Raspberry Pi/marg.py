import time
import ahrs
import numpy as np
from ahrs import Quaternion

import board
import busio
import adafruit_fxos8700
import adafruit_fxas21002c

import threading

'''
Class for reading 9-dof sensor values
The sensor we are using is the "Adafruit Precision NXP 9-DOF Breakout Board - FXOS8700 + FXAS21002"
'''
class MARG:
    def __init__(self):
        self.Q = [1., 0., 0., 0.]
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # fxos contains data of the accelerometer and the magnetometer
        self.fxos = adafruit_fxos8700.FXOS8700(self.i2c)
        self.fxas = adafruit_fxas21002c.FXAS21002C(self.i2c)
        self.d2g = ahrs.common.DEG2RAD

        # TODO: make sure the correct frequency is set here
        self.madgwick = ahrs.filters.Madgwick(frequency=10.0)

    def read_raw_data(self):
        '''
        reads the data of gyroscope, accelerometer, and magnetometer in that order
        :return: tuple of 3 tuples (with 3 elements each for x, y, and z axes)
        '''

        gyroscope = self.fxas.gyroscope
        acceleromter = self.fxos.accelerometer
        magnetometer = self.fxos.magnetometer


        return [gyroscope, acceleromter, magnetometer]

    def start_AHRS(self):
        '''
        starts the madgwick algorithm to calculate the absolute orientation of the quadcopter
        ultimately updates the quaternions (self.Q) of the quadcopter
        '''

        quaternion_thread = threading.Thread(target=self.calculate_Quaternion)
        quaternion_thread.start()

    def calculate_Quaternion(self):

        while True:
            start_time = time.time()
            gyroscope_radians = [g * self.d2g for g in self.fxas.gyroscope]

            # updates the quaternion value, which we can later change to euler angles or other
            self.Q = self.madgwick.updateMARG(self.Q, gyroscope_radians, self.fxos.accelerometer, self.fxos.magnetometer)

            # tries to adjust the sleep time so it is as close to 0.1 as possible
            # later should change it so that it's more exact, but for now this seems good enough
            time.sleep(0.1 - (time.time() - start_time))

    def to_angles(self):
        '''
        convert quaternions to angle
        :return: euler angles in a list (?)
        '''

        angles = Quaternion(self.Q).to_angles()

        return (angles)

    def to_DCM(self):
        '''
        convert quaternions to DCM (I have no idea what DCM means as of now)
        :return:
        '''

        DCM = Quaternion(self.Q).to_DCM()
        return (DCM)