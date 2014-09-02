import pygame
import constants
import Player

class Events(player):
    player = Player()

    def __init__(player):
        self.player = player

    def player_moves(direction):
    #Performs all action need to create player movement
    #input@ direction indicated by keyboard state
        player.move_horizontal(direction)


    def player_jumps(delta_time):
    #Calculate delta x/y for current jump
    #Input@ time between last call
        player.delta_xy -= Player.gravity * delta_time
        player.move_vertical(delta_time)
