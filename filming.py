import picamera
import pygame
import time
import get_data
import datetime as dt
import pi3d
 

W, H = 1280, 1020

camera = picamera.PiCamera(resolution=(W, H), framerate=24)
pygame.init()

def film(close):
    if (close):
        print(close)
        camera.stop_preview()
        return camera
    #print("filming")    
    preview = camera.start_preview()
    camera.rotation = 270
    preview.fullscreen = False
    preview.window= (10,20,W,H)
        
    while True:
        print('PULSE: ' + str(get_data.get_pulse_data_from_websocket()))
            

