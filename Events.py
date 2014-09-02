import pygame
import constants
import Player

class Events('''All game objects'''):

    def player_moves(direction):
    #Performs all action need to create player movement
    #input@ direction indicated by keyboard state
     Player.move_horizontal(direction)


    def player_jumps(delta_time):
    #Calculate delta x/y for current jump
    #Input@ time between last call
    Player.delta_xy -= Player.gravity * delta_time
    Player.move_vertical(delta_time)
