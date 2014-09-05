from pygame.rect import Rect

BASESPEED = 10
SPEEDMODIFIER = 2
JUMPFORCE = -10
CLIMBSPEED = 10
GRAVITY = 2
SCREENRECT = Rect(0,0,680,480) #We should fully figure out how all these values work as its not clear in pygame documentation
BASE_GROUND_Y = 426
PLAYER_IMAGE_LEFT = 0
PLAYER_IMAGE_RIGHT = 1
#Colour constants since we have no images right now
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)