import picamera
import pygame
import os
import os.path
from subprocess import call  
from websocket import create_connection
import json
import time
import requests
import datetime
import get_data

pictureFileType = '.png'
picturePath = '/home/pi/camera_processing/processing/pictures/'
sensorDataFile = '/home/pi/camera_processing/processing/data_for_processing'
nameOfTheLatestPicFile = '/home/pi/camera_processing/processing/name_of_the_pic'
logFileAllData = '/home/pi/camera_processing/processing/pictures/project_log_file'


def logSensorData(sensorValue):
	
	with open(sensorDataFile, "w") as text_file: # use option "a" for adding instead of overwriting
		text_file.write(sensorValue)
		
		print("did logging to data-text-file")

def getNameOfThePic(): 
	
	
	# Scan for next available image slot
	# TODO use time stamp as name of the pic!  string=time.strftime('%H:%M:%S', time.gmtime())
	
	saveIdx = 1
	while True:
		nameOfThePic =  'test_' + '%04d' % saveIdx # trying to save in png so that pixelsorting goes automatically
		print ("looking for filename:" ,nameOfThePic)
		if not os.path.isfile(picturePath + nameOfThePic + pictureFileType): break
		saveIdx += 1
		
	return nameOfThePic

def takePicture(nameOfThePic):
	print("taking picture #", nameOfThePic)
	camera = picamera.PiCamera()
	camera.resolution = (1920, 1080)
	camera.start_preview()
	camera.capture(picturePath + nameOfThePic + pictureFileType)

def logNameOfThePicture(nameOfThePic):
	with open(nameOfTheLatestPicFile, "w") as text_file: # use option "a" for adding instead of overwriting
		text_file.write(nameOfThePic)
		
		#timeStamp = datetime.datetime.now()	
		#text_file.write("time:".format(timeStamp))

		print("did logging of picture name")

def logAllData(nameOfThePic, sensorValue):
	with open(logFileAllData, "a") as text_file: # use option "a" for adding instead of overwriting
		text_file.write(nameOfThePic + pictureFileType)
		text_file.write(' => ')
		text_file.write(sensorValue)
		text_file.write(',')
		text_file.write('\n')

		#timeStamp = datetime.datetime.now()	
		#text_file.write("time:".format(timeStamp))

		print("did logging of picture name")


def main():
    # actual programme
    sensorValue = get_data.get_pulse_data_from_websocket()
    logSensorData(sensorValue)

    nameOfThePic = getNameOfThePic()
    print(nameOfThePic)

    takePicture(nameOfThePic)
    logNameOfThePicture(nameOfThePic)
    logAllData(nameOfThePic, sensorValue)
