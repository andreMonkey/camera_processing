#!/usr/bin/env python

from subprocess import call
import time
import RPi.GPIO as GPIO
import time
import filming
import camera_test
import progress_bar
import display_picture

def setup_gpio():
    # pin-layout
    GPIO.setmode(GPIO.BOARD)
    # Pin 18 (GPIO 24) as input
    GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def setup_oximeter():
    # set up oximeter
    call(["sh", "setup_oximeter.sh"])

def button_event_handler(argument):
    print("button pressed")
    camera = filming.film(True)
    GPIO.cleanup()
    setup_gpio()
    print(camera)
    sensorValue = camera_test.main(camera)
    print("\n \n Transforming picture now. \n \n")
    progress_bar.main()
    call(["bash", "./processing/pixelsorting"])
    time.sleep(2)
    display_picture.displayPicture(sensorValue)
    main()

def main():
    GPIO.add_event_detect(15, GPIO.FALLING)
    GPIO.add_event_callback(15, button_event_handler)

    try:
        filming.film(False)
 
    except KeyboardInterrupt:
        GPIO.cleanup()
        exit()

# actual programme
setup_oximeter() # do this only once
setup_gpio()
main()


# call(["ls", "-l"])
# TODO Python module anschauen, so dass man nicht aus der bash neue scripts ausfuehren muss
#call(["python", "camera_test.py"])
#time.sleep(2)
#call(["bash", "./processing/pixelsorting"])
