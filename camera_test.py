import picamera
import pygame
import os
import os.path
from subprocess import call  
import json
import time
import requests
import datetime

pictureId = 0
 
def get_sensor_data():
	#try latest update http request	
	result = requests.get("http://agilegw.local:2000/api/device/dummy001122334455/lastUpdate").text
	
	try:
		result = json.loads(result)
	except ValueError:
		print("No data available got Message:", result)
		exit()
	else:
		#Data Format '[{"deviceID":"dummy001122334455","componentID":"DummyData","value":"24","unit":"dum","format":"","lastUpdate":1495723678802}]'
		value = result[0]['value']
		print("Sensor value:")
		print value
		
		return value

def logSensorData(sensorValue):
	
	with open("data_for_processing", "w") as text_file: # use option "a" for adding instead of overwriting
		text_file.write(sensorValue)
		
		#timeStamp = datetime.datetime.now()	
		#text_file.write("time:".format(timeStamp))

		print("did logging to data-text-file")

def getNameOfThePic(): 
	
	# Scan for next available image slot
	saveIdx = 1
	while True:
		filename =  'test_' + '%04d' % saveIdx + '.png' # trying to save in png so that pixelsorting goes automatically
		print ("looking for filename:" ,filename)
		if not os.path.isfile(filename): break
		saveIdx += 1
		
	return filename

def takePicture(nameOfThePic):
	print("taking picture #", nameOfThePic)
	camera = picamera.PiCamera()
	camera.start_preview()
	time.sleep(2)
	camera.capture(nameOfThePic)

def logNameOfThePicture(nameOfThePic):
	with open("name_of_the_pic", "w") as text_file: # use option "a" for adding instead of overwriting
		text_file.write(nameOfThePic)
		
		#timeStamp = datetime.datetime.now()	
		#text_file.write("time:".format(timeStamp))

		print("did logging of picture name")

def pixelsortPicture():
	call(["bash", "processing_kim"])

	
	
# actual programme
while 1:
	sensorValue = get_sensor_data()
	logSensorData(sensorValue)

	#pictureId = pictureId + 1
	nameOfThePic = getNameOfThePic()
	
	print(nameOfThePic)
	takePicture(nameOfThePic)
	logNameOfThePicture(nameOfThePic)
	#pixelsortPicture()

	time.sleep(5)
	
	
	
