import picamera
import pygame
import time
import get_data
import datetime as dt
import RPi.GPIO as GPIO

camera = picamera.PiCamera(resolution=(1280, 720), framerate=24)

def film(close):
    if (close):
        camera.stop_preview()
        return
    camera.rotation = 270
    camera.start_preview()
    camera.annotate_background = picamera.Color('red')
    camera.annotate_text = 'PULSE: ' + str(get_data.get_pulse_data_from_websocket())
    start = dt.datetime.now()
    while True:
        camera.annotate_text = 'PULSE: ' + str(get_data.get_pulse_data_from_websocket())
