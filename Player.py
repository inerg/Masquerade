import pygame
import constants

class Player(pygame.sprite.Sprite):
	base_speed = BASESPEED
	speed_modifier = SPEEDMODIFIER
	climb_speed = CLIMBSPEED
	jump_force = JUMPFORCE
	gravity = BASEGRAVITY
	images = []
	
	def __init__(self):
		pygame.sprite.Sprite(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.rect.get_rect(midbottom-SCREENRECT.midbottom)
	
	def move(self,direction):
	# Moves character based on the given direction

	def jump(self):
	# Moves character in uniform arch, based on gravity
	# Allow movement in air?
	# Can't remeber the formula for that stuff
	
	
