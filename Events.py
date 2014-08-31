import pygame
import constant

class Events(#All game objects
								):

	def player_moves(direction):
	#Performs all action need to create player movement
		player.move_horizontal(direction)

	def player_jumps(delta_time):
	#Calculate delta x/y for current jump
		player.delta_xy -= player.gravity * delta_time
		player.move_vertical(delta_time)