import picamera
import pygame
import time
import get_data
import datetime as dt
import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD)

#GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#camera = PiCamera()
# pin-layout
GPIO.setmode(GPIO.BOARD)
# Pin 18 (GPIO 24) as input
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# recording flag
isRecording = 0
print(isRecording)

def film(isRecording):
    #GPIO.add_event_detect(15, GPIO.RISING, callback=button_event_handler, bouncetime=300)    
    if (GPIO.input(15) == GPIO.HIGH) and (isRecording == 0):
        isRecording = 1
        camera = picamera.PiCamera(resolution=(1280, 720), framerate=24)
        camera.rotation = 270
        camera.start_preview()
        camera.annotate_background = picamera.Color('red')
        # timestamp camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        camera.annotate_text = 'PULSE: ' + str(get_data.get_pulse_data_from_websocket())
        camera.start_recording('timestamped.h264')
        start = dt.datetime.now()
    if (GPIO.input(15) == GPIO.LOW) and (isRecording == 1):
        # loop waiting for the 'stop signal'
        print("stoop")
        camera.stop_recording
#        isRecording = 0

    #camera.stop_recording()    

def button_event_handler():
    print("button pressed")
    camera.stop_recording()
    exit()    

while True:
    # IDEA : for several sensor flip through the different sensors in a loop
    if (isRecording == 1):
        camera.annotate_text = 'PULSE: ' + str(get_data.get_pulse_data_from_websocket())
        camera.wait_recording(0.2)
    film(isRecording)


#film()
