import picamera
import pygame
import time
import get_data
import datetime as dt

camera = picamera.PiCamera(resolution=(1280, 720), framerate=24)

def film(close):
    if (close):
        print(close)
        camera.stop_preview()
        #camera.close()
        return camera
    print("fliming")    
    camera.rotation = 270
    camera.start_preview()
    camera.annotate_background = picamera.Color('red')
    print(str(get_data.get_pulse_data_from_websocket()))
    camera.annotate_text = 'PULSE: ' + str(get_data.get_pulse_data_from_websocket())
    start = dt.datetime.now()
    while True:
        camera.annotate_text = 'PULSE: ' + str(get_data.get_pulse_data_from_websocket())
