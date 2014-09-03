import pygame

import Player
import Events
import constants
import sys
from pygame.locals import *

pygame.init()  # This is needed so that anything with in pygame can be used.

fpsClock = pygame.time.Clock()  # This will allow for us to sleep the games execution to lock it at 60fps.

window = pygame.display.set_mode(constants.SCREENRECT.size, 0, 32)
                                                            #(x, y, windows style (full or windowed), Bit depth)
pygame.display.set_caption('Masquerade')  #Sets the windows text title

#Hardcoded loading of images
img = pygame.image.load('Images/Tiles/Terrain/AttackDummy1.PNG').convert()

Player.Player.images = [img, pygame.transform.flip(img, 1, 0)]

thePlayer = pygame.sprite.GroupSingle()

Player.Player.containers = thePlayer

player = Player.Player()
eventMaker = Events.Events(player)

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
    eventMaker.player_moves(direction)


    dirty = thePlayer.draw(window)
    pygame.display.update(dirty)
    fpsClock.tick(60)