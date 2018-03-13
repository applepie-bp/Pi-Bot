import RPi.GPIO as gpio

#13 -> 1 0
#19 -> 0 1
#26 -> 1 1

gpio.setmode(gpio.BCM)

#gpio.output(19, gpio.LOW)
#gpio.output(26, gpio.HIGH)
#gpio.output(13, gpio.HIGH)

class Motor:
    def __init__(self, pinEnable, pin1, pin2):
        gpio.setup(13, gpio.OUT)
        gpio.setup(19, gpio.OUT)
        gpio.setup(26, gpio.OUT)
        self.pinEnable = pinEnable
        self.pin1 = pin1
        self.pin2 = pin2
        gpio.output(pinEnable, gpio.LOW)
        gpio.output(pin1, gpio.LOW)
        gpio.output(pin2, gpio.LOW)
    
    def forward(self):
        gpio.output(self.pin1, gpio.HIGH)
        gpio.output(self.pin2, gpio.LOW)

    def backward(self):
        gpio.output(self.pin1, gpio.LOW)
        gpio.output(self.pin2, gpio.HIGH)

    def enable(self):
        gpio.output(self.pinEnable, gpio.HIGH)

    def disable(self):
        gpio.output(self.pinEnable, gpio.LOW)


class Chassis:
    def __init__(self):
        self.leftmotor = Motor(26,13,19)
        self.rightmotor = Motor(21,20,16)

    def forward(self, speed):
        self.leftmotor.forward()
        self.rightmotor.forward()

    def backward(self, speed):
        self.leftmotor.backward()
        self.rightmotor.backward()

    def leftturn(self, speed):
        self.rightmotor.forward()

    def leftrota(self, speed):
        self.rightmotor.forward()
        self.leftmotor.backward()

    def rightturn(self, speed):
        self.leftmotor.forward()

    def rightrota(self, speed):
        self.leftmotor.forward()
        self.rightmotor.backward()
    
leftmotor = Motor(26,13,19)

leftmotor.forward()
leftmotor.enable()
input()
leftmotor.backward()
input()
leftmotor.disable()

rightmotor = Motor(21,20,16)

rightmotor.forward()
rightmotor.enable()
input()
rightmotor.backward()
input()
rightmotor.disable()





gpio.cleanup()
