class IO:
	def getQR():
		print("getting QR")
		#info = open webpage from pi2
		#if info != "noQR"
			#file = openfile(info.txt)
			#spilt up array e.t.c.
			#robot.map = file
		#else:
			#return "noQR"

	def rotate():
		pass

	def forward():
		pass

	def getdistancefront():
		pass
		#distance = urlget(ip+"/frontsensor")
		#return distance

class world:
	def __init__(self):
		self.startrotation = 0
	def say(self, string):
		print(string)

class robot(IO):
	def __init__(self, world, lookforQR, gotoknown, gototarget):
		self.world = world
		self.lookforQR = lookforQR
		self.gotoknown = gotoknown
		self.gototarget = gototarget
	def newbehaviour(self, newbehaviour):
		self.behaviour=newbehaviour
	def handler(self):
		result = self.behaviour.start()
		# if result = "run gototarget"
			#self.newbeaviour
		return result
	def start(self):
		self.newbehaviour(lookforQR)
		# if found:
			#gotoknown()
			#if target:
				#gototarget
		# else
			#searchrandom()
		result = self.handler()

class lookforQR(IO):
	#check if qr available
	#if yes:
	name = "lookforQR"
	def __init__(self):
		pass
	def start(self, targetQR):
		print("staring lookforQR")
		self.QRcode = self.getQR()
		if self.QRcode != "":
			if self.QRcode == self.targetQR:
				pass
				#gotoknow()
		else:
			pass
			#rotate around
			#search for qr
	def getQR(self):
		return 1

	def rotate(self, degrees):
		pass

class gotoknown(IO):
	name = "gotoknown"
	def __init__(self):
		pass
	def start(self):
		print("staring gotoknown")
		#check distance to qr
		#if there: exit("arrived")
		#else: get location on screen
		# rotate until in centre
		# go forward until there
	def exit(self, message):
		return message

class gototarget(IO):
	name = "gototarget"
	def __init__(self):
		pass
	def start(self):
		print("staring gototarget")
		#self.face = robot.getface()
		#if self.face = self.target:
			#notify user
			#start skype
			#
		#else:
			#rotate around
			#return searchrandom()

World=world()
Gototarget=gototarget()
LookforQR=lookforQR()
Gotoknown=gotoknown()
Robot=robot(World, LookforQR, Gotoknown, Gototarget)

Robot.start()
