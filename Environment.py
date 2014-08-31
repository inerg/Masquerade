import pygame
import Constants
#This may be able to be kept as a Sprite since it doesn't do much special
class Environment(pygame.sprite.Sprite):
    images = []

    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

