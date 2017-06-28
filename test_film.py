import RPi.GPIO as GPIO
from picamera import PiCamera
from time import sleep

camera = PiCamera()
# pin-layout
GPIO.setmode(GPIO.BOARD)
# Pin 18 (GPIO 24) as input
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
# recording flag
isRecording = 0

# loop
while 1 :
    # read input
    if (GPIO.input(18) == GPIO.HIGH) and (isRecording == 0):
        # if input = high start recording
        camera.start_recording('video.h264')
        isRecording = 1

    if (GPIO.input(18) == GPIO.LOW) and (isRecording == 1):
        # loop waiting for the 'stop signal'
        camera.stop_recording
        isRecording = 0
