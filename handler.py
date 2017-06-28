#!/usr/bin/env python

from subprocess import call
import time
import RPi.GPIO as GPIO
import time
import filming

GPIO.setmode(GPIO.BCM)

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def main():
    GPIO.add_event_detect(15,GPIO.FALLING)
    GPIO.add_event_callback(15,buttonEventHandler,100)
    filming.film()

def buttonEventHandler():
    filming.stop_filming()
    call(["python", "camera_test.py"])
    main()

main()
except KeyboardInterrupt:  
    GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
#GPIO.cleanup()           # clean up GPIO on normal exit  


# set up oximeter
#call(["sh", "setup_oximeter.sh"])

## TODO: ADD multi thread processing!!!
#while True:
    #time.sleep(0.001) # do not use all the cpu power
    ## The button has not been pressed - we are in filming mode
    #if (GPIO.input(18) == True):
        #filming.film()
        #continue
    ## Button has been pressed - we take a picture
    #elif (GPIO.input(18) == False):
        ## run script to take picture and save data
        ## display foto and pixelsort (parallel??) 
        ## run script to pixelsort
        ## run script to display pixelsorted picture
        ## run script to print picture
        #call(["python", "camera_test.py"])
##         call(["python", "filming.py"])



# call(["ls", "-l"])
# TODO Python module anschauen, so dass man nicht aus der bash neue scripts ausfuehren muss
#call(["python", "camera_test.py"])
#time.sleep(2)
#call(["bash", "./processing/pixelsorting"])
