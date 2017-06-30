import RPi.GPIO as GPIO
import picamera
from time import sleep
import datetime as dt

camera = picamera.PiCamera(resolution=(1280, 720), framerate=24)
# pin-layout
GPIO.setmode(GPIO.BOARD)
# Pin 18 (GPIO 24) as input
GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_UP)
# recording flag
isRecording = 0

# loop
while 1 :
    # read input
    if (GPIO.input(15) == GPIO.HIGH) and (isRecording == 0):
        # if input = high start recording
        
        #camera.start_recording('video.h264')
        camera.rotation = 270
        camera.start_preview()
        camera.annotate_background = picamera.Color('red')
        # timestamp camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        camera.annotate_text = 'PULSE: ' #+ str(get_data.get_pulse_data_from_websocket())
        camera.start_recording('timestamped.h264')
        start = dt.datetime.now()
        isRecording = 1
        print("record")

    if (GPIO.input(15) == GPIO.LOW) and (isRecording == 1):
        # loop waiting for the 'stop signal'
        print("stoop")
        camera.stop_recording()
        #camera_stop_review()
        #exit()
        isRecording = 0
