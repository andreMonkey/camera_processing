import picamera
import pygame
import os
import os.path
from subprocess import call  
from websocket import create_connection

ws = create_connection("ws://agilegw.local:8080/ws/device/dummy001122334455.DummyData/subscribe")
print "Receiving..."
result =  ws.recv()
print "Received '%s'" % result
ws.close()





#camera = picamera.PiCamera()
#camera.capture('test_0004.png')

#call(["bash", "processing_kim"])
