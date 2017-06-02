import picamera
import pygame
import os
import os.path
from subprocess import call  
import json
import time
import requests

pictureId = 0

while 1:
	pictureId = pictureId + 1
	sensorValue = get_sensor_data()
	logSensorData(sensorValue)
	takePicture(pictureId)
	#pixelsortPicture()


  
def get_sensor_data():
	#try latest update http request	
	result = requests.get("http://agilegw.local:2000/api/device/dummy001122334455/lastUpdate").text  # try string replace for the "["
		
	#Data Format '[{"deviceID":"dummy001122334455","componentID":"DummyData","value":"24","unit":"dum","format":"","lastUpdate":1495723678802}]'
	result = json.loads(result)
	value = result[0]['value']
	print("Sensor value")
	print value
	
	return (value)

def takePicture(pictureId):
	fileName = 'test_000'+ pictureId + 'png'
	print("taking picture #", fileName)
	camera = picamera.PiCamera()
	camera.capture('test_0004.png')
	
def logSensorData(sensorValue):
	with open("data_for_processing", "w") as text_file:
		text_file.write( "value: {0}".sensorValue)
		print("did logging to text-file")

def pixelsortPicture():
	call(["bash", "processing_kim"])
	
