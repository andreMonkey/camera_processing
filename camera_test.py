import picamera
import pygame
import os
import os.path
from subprocess import call  
import json
import time
import requests

while 1:
	#try latest update http request	
	result = requests.get("http://agilegw.local:2000/api/device/dummy001122334455/lastUpdate").text  # try string replace for the "["
		
	#Data Format '[{"deviceID":"dummy001122334455","componentID":"DummyData","value":"24","unit":"dum","format":"","lastUpdate":1495723678802}]'
	result = json.loads(result)
	print result[0]['value']
	

#camera = picamera.PiCamera()
#camera.capture('test_0004.png')

#call(["bash", "processing_kim"])
