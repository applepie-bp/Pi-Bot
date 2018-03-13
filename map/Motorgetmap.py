from flask import Flask
import RPi.GPIO as gpio
import time

#double check GPIO pins
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
        #self.pwm = gpio.PWM(self.pinEnable, 100)

        #set GPIO Pins
        self.GPIO_TRIGGER = 18
        self.GPIO_ECHO = 24
         
        #set GPIO direction (IN / OUT)
        gpio.setup(self.GPIO_TRIGGER, gpio.OUT)
        gpio.setup(self.GPIO_ECHO, gpio.IN)
    
    def forward(self):
        self.enable()
        gpio.output(self.pin1, gpio.HIGH)
        gpio.output(self.pin2, gpio.LOW)

    def backward(self):
        self.enable()
        gpio.output(self.pin1, gpio.LOW)
        gpio.output(self.pin2, gpio.HIGH)

    def enable(self):
        #self.pwm.start(0)
        #self.pwm.ChangeDutyCycle(self.speed)
        gpio.output(self.pinEnable, gpio.HIGH)
        print ("In Enable")

    def disable(self):
        #self.pwm.ChangeDutyCycle(0)
        #self.pwm.stop()
        gpio.output(self.pinEnable, gpio.LOW)
        print ("In disable")

    def setspeed(self, speed):
        self.speed=speed
        #self.pwm.ChangeDutyCycle(self.speed)
        print ("In setspeed")


class Chassis:
    def __init__(self,speed=50):
        self.leftmotor = Motor(26,13,19)
        self.rightmotor = Motor(21,16,20)
        self.rightmotor.setspeed(speed)
        self.leftmotor.setspeed(speed)
        self.motorms = 1 #time to travel 1,
        self.motorturnms = 1 #time to rotate 45 degrees

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
        print ("In stop")
        
    def changespeed(self, speed):
        self.rightmotor.setspeed(speed)
        self.leftmotor.setspeed(speed)

    def forwarddistance(self, distance):
        self.forward()
        self.start()
        sleepin = distance*self.motorms
        time.sleep(float(sleepin))
        self.stop()

    def backwarddistance(self, distance):
        self.backward()
        self.start()
        sleepin = distance*self.motorms
        time.sleep(float(sleepin))
        self.stop()

    def leftturndeg(self, deg):
        self.leftturn()
        self.start()
        sleepin = deg*self.motorturnms
        time.sleep(float(sleepin))
        self.stop()

    def rightturndeg(self, deg):
        self.rightturn()
        self.start()
        sleepin = deg*self.motorturnms
        time.sleep(float(sleepin))
        self.stop()

    def leftrotadeg(self, deg):
        self.leftrota()
        self.start()
        sleepin = deg*self.motorturnms
        time.sleep(float(sleepin))
        self.stop()

    def rightrotadeg(self, deg):
        self.rightrota()
        self.start()
        sleepin = deg*self.motorturnms
        time.sleep(float(sleepin))
        self.stop()

    def checkdistance(self):
        # set Trigger to HIGH
        #gpio.output(self.GPIO_TRIGGER, True)
        gpio.output(18, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        #gpio.output(self.GPIO_TRIGGER, False)
        gpio.output(18, False)
             
        StartTime = time.time()
        StopTime = time.time()
        # save StartTime
        #while gpio.input(self.GPIO_ECHO) == 0:
        while gpio.input(24) == 0:    
            StartTime = time.time()
                 
        # save time of arrival
        #while gpio.input(self.GPIO_ECHO) == 1:
        while gpio.input(24) == 1:    
            StopTime = time.time()
                 
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
                 
        return distance

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

@app.route('/forward/<dist>', methods=["GET"])
def forward(dist):
    print("starting forward")
    tank.forwarddistance(dist)
    print("ending forward")
    return "Going forward"+dist

@app.route('/backward/<dist>', methods=["GET"])
def backward(dist):
    tank.backwarddistance(dist)
    return "Going backward"

@app.route('/leftturn/<deg>', methods=["GET"])
def leftturn(deg):
    tank.leftturndeg(deg)
    return "Turning left"

@app.route('/leftrotate/<deg>', methods=["GET"])
def leftrotate(deg):
    tank.leftrotadeg(deg)
    return "rotating left"

@app.route('/rightturn/<deg>', methods=["GET"])
def rightturn(deg):
    tank.rightturndeg(deg)
    return "Turning right"

@app.route('/rightrotate/<deg>', methods=["GET"])
def rightrotate(deg):
    tank.rightrotadeg(deg)
    return "Rotating right"

@app.route('/start', methods=["GET"])
def start():
    tank.start()
    return "Tank starting"

@app.route('/stop', methods=["GET"])
def stop():
    tank.stop()
    return "Tank stopping"

@app.route('/dist', methods=["GET"])
def dist():
    #print (type(tank.checkdistance()))
    distance = float(tank.checkdistance())
    return "{}".format(distance)

@app.route('/qr/<num>', methods=["GET"])
def dist(num):
    for x in range(0,10):
        return x


@app.route('/close', methods=["GET"])
def close():
    gpio.cleanup()
    return "End"

app.run(host='0.0.0.0', debug=True)
print ("end of app")

    
tank.stop()

gpio.cleanup()
