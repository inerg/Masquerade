import pygame
import Constants
import Player

class Events('''All game objects'''):

    def player_moves(direction):
    #Performs all action need to create player movement
    #input@ direction indicated by keyboard state
    player.move_horizontal(direction)

    def player_jumps(delta_time):
    #Calculate delta x/y for current jump
    #Input@ time between last call
    player.delta_xy -= player.gravity * delta_time
    player.move_vertical(delta_time)