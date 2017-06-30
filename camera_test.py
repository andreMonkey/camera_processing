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
		#print ("looking for filename:" ,nameOfThePic)
		if not os.path.isfile(picturePath + nameOfThePic + pictureFileType): break
		saveIdx += 1
		
	return nameOfThePic

def takePicture(camera, nameOfThePic):
	print("taking picture #", nameOfThePic)
	camera.capture(picturePath + nameOfThePic + pictureFileType)

def logNameOfThePicture(nameOfThePic):
	with open(nameOfTheLatestPicFile, "w") as text_file: # use option "a" for adding instead of overwriting
		text_file.write(nameOfThePic)

def logAllData(nameOfThePic, sensorValue):
	with open(logFileAllData, "a") as text_file: # use option "a" for adding instead of overwriting
		text_file.write(nameOfThePic + pictureFileType)
		text_file.write(' => ')
		text_file.write(sensorValue)
		text_file.write(',')
		text_file.write('\n')


def main(camera):
    # actual programme
#    print("taking picture now")
    sensorValue = get_data.get_pulse_data_from_websocket()
    logSensorData(sensorValue)

    nameOfThePic = getNameOfThePic()
    print(nameOfThePic)

    takePicture(camera, nameOfThePic)
    logNameOfThePicture(nameOfThePic)
    logAllData(nameOfThePic, sensorValue)
