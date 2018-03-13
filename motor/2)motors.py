import RPi.GPIO as gpio
import time


# one       three
#   M1       M2
# two       four

one = 6
two = 13
three = 19
four = 26

gpio.setmode(gpio.BCM)
gpio.setup(one, gpio.OUT)
gpio.setup(two, gpio.OUT)
gpio.setup(three, gpio.OUT)
gpio.setup(four, gpio.OUT)

onepwm = gpio.PWM(one,100) #100hz frequency
twopwm = gpio.PWM(two,100)
threepwm = gpio.PWM(three,100)
fourpwm = gpio.PWM(four,100) 

onepwm.start(0)#duty cycle
#twopwm.start(0)
#threepwm.start(0)
#fourpwm.start(0)

def forward(speed):
    onepwm.ChangeDutyCycle(speed)
    threepwm.ChangeDutyCycle(speed)
    time.sleep(3)
    onepwm.stop()
    threepwm.stop()
    
def backward(speed):
    twopwm.ChangeDutyCycle(speed)
    fourpwm.ChangeDutyCycle(speed)
    time.sleep(3)
    twopwm.stop()
    fourpwm.stop()

def leftturn(speed):
    onepwm.ChangeDutyCycle(speed)
    time.sleep(1)
    onepwm.stop()

def rightturn(speed):
    threepwm.ChangeDutyCycle(speed)
    time.sleep(1)
    threepwm.stop()

def leftrota(speed):
    twopwm.ChangeDutyCycle(speed)
    threepwm.ChangeDutyCycle(speed)
    time.sleep(1)
    twopwm.stop()
    threepwm.stop()

def rightrota(speed):
    onepwm.ChangeDutyCycle(speed)
    fourpwm.ChangeDutyCycle(speed)
    time.sleep(1)
    onepwm.stop()
    fourpwm.stop()


forward(50)

    

onepwm.stop()
twopwm.stop()
threepwm.stop()
fourpwm.stop()

gpio.cleanup()

print("the end")



