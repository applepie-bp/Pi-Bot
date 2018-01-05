import RPi.GPIO as gpio
import time

#13 -> 1 0
#19 -> 0 1
#26 -> 1 1

gpio.setmode(gpio.BCM)

#gpio.output(19, gpio.LOW)
#gpio.output(26, gpio.HIGH)
#gpio.output(13, gpio.HIGH)

class Motor:
    def __init__(self, pinEnable, pin1, pin2):
        self.pinEnable = pinEnable
        self.pin1 = pin1
        self.pin2 = pin2
        self.speed = 50
        gpio.setup(self.pin1, gpio.OUT)
        gpio.setup(self.pin2, gpio.OUT)
        #gpio.cleanup()
        gpio.setup(self.pinEnable, gpio.OUT)
        gpio.output(pinEnable, gpio.LOW)
        gpio.output(pin1, gpio.LOW)
        gpio.output(pin2, gpio.LOW)
        self.pwm = gpio.PWM(self.pinEnable, 100)
    
    def forward(self):
        self.enable()
        gpio.output(self.pin1, gpio.HIGH)
        gpio.output(self.pin2, gpio.LOW)

    def backward(self):
        self.enable()
        gpio.output(self.pin1, gpio.LOW)
        gpio.output(self.pin2, gpio.HIGH)

    def enable(self):
        self.pwm.start(0)
        self.pwm.ChangeDutyCycle(self.speed)

    def disable(self):
        self.pwm.ChangeDutyCycle(0)

    def setspeed(self, speed):
        self.speed=speed
        self.pwm.ChangeDutyCycle(self.speed)


class Chassis:
    def __init__(self,speed=50):
        self.leftmotor = Motor(26,13,19)
        self.rightmotor = Motor(21,16,20)
        self.rightmotor.setspeed(speed)
        self.leftmotor.setspeed(speed)

    def forward(self):
        self.leftmotor.forward()
        self.rightmotor.forward()

    def backward(self):
        self.leftmotor.backward()
        self.rightmotor.backward()

    def leftturn(self):
        self.leftmotor.forward()
        self.rightmotor.disable()

    def leftrota(self):
        self.rightmotor.backward()
        self.leftmotor.forward()

    def rightturn(self):
        self.rightmotor.forward()
        self.leftmotor.disable()

    def rightrota(self):
        self.leftmotor.backward()
        self.rightmotor.forward()

    def start(self):
        self.leftmotor.enable()
        self.rightmotor.enable()
        
    def stop(self):
        self.leftmotor.disable()
        self.rightmotor.disable()
        
    def changespeed(self, speed):
        self.rightmotor.setspeed(speed)
        self.leftmotor.setspeed(speed)
    
tank = Chassis(speed=21)
print("rotating left")
tank.leftrota()
tank.start()

g = input("")
#time.sleep(10)

print("rotating right")
tank.rightrota()

g = input("")
#time.sleep(10)

print("turning left")
tank.leftturn()

g = input("")

print("turning right")
tank.rightturn()

g = input("")

print("forwards")
tank.forward()

g = input("")

print("backwards")
tank.backward()

g = input("")

tank.stop()

print("end")
gpio.cleanup()
