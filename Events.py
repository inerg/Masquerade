import pygame
import constants
import Player

class Events(object):
    player = None

    def __init__(self,player):
        self.player = player

    def player_moves(self,direction):
    #Performs all action need to create player movement
    #input direction indicated by keyboard state
        self.player.move_horizontal(direction)


    def player_jumps(self,delta_time):
    #Calculate delta x/y for current jump
    #Input@ time between last call
        self.player.jump_force -= self.player.gravity * delta_time
        self.player.move_vertical(delta_time)
