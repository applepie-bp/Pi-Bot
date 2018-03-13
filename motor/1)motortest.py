import RPi.GPIO as gpio
import time


# one       three
#   M1       M2
# two       four

one = 13

gpio.setmode(gpio.BCM)
gpio.setup(one, gpio.OUT)

onepwm = gpio.PWM(one,100) #100hz frequency

onepwm.start(0)

onepwm.ChangeDutyCycle(75)
#gpio.output(one,gpio.HIGH)
g = raw_input()

gpio.cleanup()

print("the end")


