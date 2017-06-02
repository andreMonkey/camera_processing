import picamera
import pygame
import os
import os.path
from subprocess import call  
from websocket import create_connection
import json
import time
import requests
ws = create_connection("ws://agilegw.local:8080/ws/device/dummy001122334455.DummyData/subscribe")

while 1:
	# get data from websocket
	print "Receiving..."
	result =  ws.recv()
	print result
	with open("saving_data", "a") as text_file:
		text_file.write("\n")
		text_file.write(result)
		print("wrote text-file")
	result = json.loads(result)  # result is now a dict
	value = result.get('latestUpdate')
	print value
	ws.close()

	
#camera = picamera.PiCamera()
#camera.capture('test_0004.png')

#call(["bash", "processing_kim"])
