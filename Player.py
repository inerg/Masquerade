import pygame
import constants


class Player(pygame.sprite.Sprite):
    base_speed = constants.BASESPEED
    speed_modifier = constants.SPEEDMODIFIER
    climb_speed = constants.CLIMBSPEED
    jump_force = constants.JUMPFORCE
    delta_xy = 0
    gravity = constants.GRAVITY
    hasJumped = False
    curr_ground_y = constants.BASE_GROUND_Y
    images = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.rect.get_rect(midbottom - constants.SCREENRECT.midbottom)

    def move_horizontal(self, direction):
        # Moves character based on the given direction
        if direction > 0:
            self.image = images[1]
        else:
            self.image = images[0]

        self.rect.move_ip(constants.BASESPEED * direction, 0)
        self.rect.clamp(constants.SCREENRECT)


def move_vertical(self, delta_time):
    # Moves character by the given delta x/y coordinates
    self.rect.move_ip(0, sel.rect.y + (delta_xy * delta_time))
    self.rect.clamp(constants.SCREENRECT)

    if self.rect.y <= curr_ground_y
        self.rect.move_ip(0, curr_ground_y)
        delta_xy = 0


def jump():
    hasJumped = True  # while not important right now I've read use 1 and 0 is faster for execution although minorly for true false checks


def isJumping():
    return hasJumped

