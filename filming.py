import picamera
import pygame
import time
import get_data
import datetime as dt
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



def film():
    GPIO.add_event_detect(15, GPIO.RISING, callback=button_event_handler, bouncetime=300)    
    camera = picamera.PiCamera(resolution=(1280, 720), framerate=24)
    camera.rotation = 270
    camera.start_preview()
    camera.annotate_background = picamera.Color('red')
    # timestamp camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.annotate_text = 'PULSE: ' + str(get_data.get_pulse_data_from_websocket())
    camera.start_recording('timestamped.h264')
    start = dt.datetime.now()
    while True:
        # IDEA : for several sensor flip through the different sensors in a loop
        camera.annotate_text = 'PULSE: ' + str(get_data.get_pulse_data_from_websocket())
        camera.wait_recording(0.2)
    #camera.stop_recording()    

def button_event_handler():
    print("button pressed")
    camera.stop_recording()
    exit()    



film()
