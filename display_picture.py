import glob
import os
import pygame
import time

pygame.init()
white = (255,255,255)
black = (0,0,0)

#c = pygame.time.Clock() # create a clock object for timing

def getNameOfTheTransformedPic(): 
    list_of_files = glob.glob('/home/pi/camera_processing/processing/transformed_pictures/*')
    latest_file = max(list_of_files, key = os.path.getctime)
    print(latest_file)
    return latest_file

def displayPicture(value):
    os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
    w, h = 1120, 1000
    size=(w,h)
    screen = pygame.display.set_mode(size) 
    filename = getNameOfTheTransformedPic()
    img=pygame.image.load(filename)
    img = pygame.transform.scale(img, (1080,800)) 
    screen.blit(img,(20,20))
    
    font = pygame.font.Font('Monotxt.ttf', 55)
    screen.blit(font.render('PULSE:' + str(value), True, (255,255,255)), (20,850))
    pygame.display.update() 
    time.sleep(5)  
    
