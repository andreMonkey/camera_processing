#!/usr/bin/env python
print("""
This example shows how you can monitor an analog input by attaching a function to its changed event.

You should see the analog value being printed out as it changes.

Try connecting up a rotary potentiometer or analog sensor to input one.

""")

from subprocess import call
import time



while True:
 call(["ls", "-l"])
 call(["python", "camera_test.py"])
 #call(["bash", "processing_kim"])
 
 #time.sleep(0.001) # do not use all the cpu power
 #pressed = 0
 #pressed = read_digital_pin()
 #if pressed:
    #when_pressed = time.time()
    #time_pressed = time.time() - when_pressed
    #while pressed:
      #if time_pressed > 4:
         #call("sudo halt -n") # turn of PI , when pressed for more than 4 seconds
         ##call("sudo shutdown -h now") # turn of PI , when pressed for more than 4 seconds  
