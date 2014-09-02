import os.path
import pygame

import constants
import sys
from pygame.locals import *

main_dir = os.path.split(os.path.abspath(__file__))[0] #Gets working directory program is running in
pygame.init()  # This is needed so that anything with in pygame can be used.




fpsClock = pygame.time.Clock()  # This will allow for us to sleep the games execution to lock it at 60fps.

window = pygame.display.set_mode(constants.SCREENRECT.size, 0, 32)
                                                            #(x, y, windows style (full or windowed), Bit depth)
pygame.display.set_caption('Masquerade')  #Sets the windows text title

#Load and start sound
background_music = os.path.join(main_dir, 'Assets', 'Sound', 'Music', 'background.ogg')
pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1, 0.0) #Starts the music looping indefinitely at the start of the song

position = -100
while True:
    #Read system inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == ord('m'):
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
    key_state = pygame.key.get_pressed()

    window.fill(constants.WHITE)
    pygame.draw.rect(window, constants.RED, Rect(position, 200, 100, 50))
    position += 1
    if position > 740:
        position = -100


    #Make action on player input
    direction = key_state[K_RIGHT] - key_state[K_LEFT]


    pygame.display.update()
    fpsClock.tick(60)
