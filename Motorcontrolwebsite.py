from flask import Flask
import RPi.GPIO as gpio
import time

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

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
tank = Chassis(speed=21)
tank.start()

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/changespeed/<s>', methods=["GET"])
def speed(s):
    tank.changespeed(float(s))
    return "Going speed "+ s

@app.route('/forward', methods=["GET"])
def forward():
    tank.forward()
    return "Going forward"

@app.route('/backward', methods=["GET"])
def backward():
    tank.backward()
    return "Going backward"

@app.route('/leftturn', methods=["GET"])
def leftturn():
    tank.leftturn()
    return "Turning left"

@app.route('/leftrotate', methods=["GET"])
def leftrotate():
    tank.leftrota()
    return "rotating left"

@app.route('/rightturn', methods=["GET"])
def rightturn():
    tank.rightturn()
    return "Turning right"

@app.route('/rightrotate', methods=["GET"])
def rightrotate():
    tank.rightrota()
    return "Rotating right"

@app.route('/start', methods=["GET"])
def start():
    tank.start()
    return "Tank starting"

@app.route('/stop', methods=["GET"])
def stop():
    tank.stop()
    return "Tank stopping"

@app.route('/close', methods=["GET"])
def close():
    gpio.cleanup()
    return "End"

app.run(debug=True)
print ("end of app")

    
tank.stop()

gpio.cleanup()
