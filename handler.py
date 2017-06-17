#!/usr/bin/env python
print("""
This example shows how you can monitor an analog input by attaching a function to its changed event.

You should see the analog value being printed out as it changes.

Try connecting up a rotary potentiometer or analog sensor to input one.

""")

from subprocess import call
import time

# discover bluetooth devices - sh ./discover.sh
call(["sh", "./discover.sh"])

# register oximeter sh ./registerDevice.sh 98:7B:F3:73:80:84 Oximeter
call(["sh", "sh ./registerDevice.sh 98:7B:F3:73:80:84 Oximeter"])

# execute command for websocket subscription - sh ./subscribe.sh  ble987BF3738084 PULSE
call(["sh", "./subscribe.sh ble987BF3738084 PULSE"])


#call(["ls", "-l"])
# TODO Python module anschauen, so dass man nicht aus der bash neue scripts ausführen muss
call(["python", "camera_test.py"])
time.sleep(2)
call(["bash", "./processing/pixelsorting"])


 
 
 # Work the camera with a button! 
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
