import RPi.GPIO as GPIO

class CityLightManager:

	def __init__(self, red, green, yellow):
		#set mode
		GPIO.setmode(GPIO.BOARD)

		#colors
		self.red = red
		self.yellow = yellow
		self.green = green

		#set I/O of pins
		GPIO.setup(self.red, GPIO.OUT)
		GPIO.setup(self.yellow, GPIO.OUT)
		GPIO.setup(self.green, GPIO.OUT)

	def turnOffAll(self):
		print("turning off all lights")
		GPIO.output(self.red, GPIO.LOW)
		GPIO.output(self.yellow, GPIO.LOW)
		GPIO.output(self.green, GPIO.LOW)

	def turnOnRed(self):
		print("turning on red")
		self.turnOffAll()
		GPIO.output(self.red, GPIO.HIGH)

	def turnOnYellow(self):
		print("turning on yellow")
		self.turnOffAll()
		GPIO.output(self.yellow, GPIO.HIGH)

	def turnOnGreen(self):
		print("turning on green")
		self.turnOffAll()
		GPIO.output(self.green, GPIO.HIGH)
