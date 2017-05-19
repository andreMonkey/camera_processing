import picamera
import pygame
import os
import os.path
from subprocess import call  



camera = picamera.PiCamera()
camera.capture('test_0004.png')

call(["bash", "processing_kim"])
