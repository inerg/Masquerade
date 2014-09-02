import pygame

import constants
import sys
from pygame.locals import *

pygame.init()  # This is needed so that anything with in pygame can be used.




fpsClock = pygame.time.Clock()  # This will allow for us to sleep the games execution to lock it at 60fps.

window = pygame.display.set_mode(constants.SCREENRECT.size, 0, 32)
                                                            #(x, y, windows style (full or windowed), Bit depth)
pygame.display.set_caption('Masquerade')  #Sets the windows text title


position = -100
while True:
    #Read system inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keystate = pygame.key.get_pressed()


    window.fill(constants.WHITE)
    pygame.draw.rect(window, constants.RED, Rect(position, 200, 100, 50))
    position += 1
    if position > 740:
        position = -100


    #Make action on player input
    direction = keystate[K_RIGHT] - keystate[K_LEFT]


    pygame.display.update()
    fpsClock.tick(60)
