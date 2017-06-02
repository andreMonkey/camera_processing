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
#	try websocket
	#print "Receiving..."
	#result =  ws.recv()
	#print result
	#with open("saving_data", "a") as text_file:
		#text_file.write("\n")
		#text_file.write(result)
		#print("wrote text-file")
	#result = json.loads(result)  # result is now a dict
	#value = result.get('latestUpdate')
	#print value
#	ws.close()

	#try latest update http request	
	#print "request to latest update url"
	result = requests.get("http://agilegw.local:2000/api/device/dummy001122334455/lastUpdate").text  # try string replace for the "["
	#print "Received '%s'" % result
	#resultValue = result[0][4]
	#resultValue = result[0][5]
	
	result = json.loads(result)
	print result[0]['value']
	
	#result = json.loads(result)  # result is now a dict
	#value = result.get('value')
	#timestamp = time.time()
	#print value, timestamp
	#print '"data":', result['value']
	#Received '{"deviceID":"dummy001122334455","componentID":"DummyData","value":"24","unit":"dum","format":"","lastUpdate":1495723678802}'






#camera = picamera.PiCamera()
#camera.capture('test_0004.png')

#call(["bash", "processing_kim"])
