# rpi-quadcopter
Quadcopter completely controlled by a raspberry pi

# Sensor Fusion Stuff
make sure to use pip3 rather than pip as raspberry pi supports python2 as default rather than python3
```console
foo@bar:~$ pip3 install ahrs
```
# Xbox360 controller stuff
If using mac, need to download this driver: https://github.com/360Controller/360Controller

# Server stuff
- getting picam running
- sending signals and stuff

# ESCs controlled by pi
- used PIGPIO because it enables DMA PWM rather than software PWM that RPi.GPIO uses (more precise, which is necessary for a quadcopter running on brushless motors)

# Code
can make a diagram of how the things work or something

for pygame, use conda venv if running code on PyCharm
