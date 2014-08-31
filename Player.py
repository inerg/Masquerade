import pygame
import constants

class Player(pygame.sprite.Sprite):
	base_speed = BASESPEED
	speed_modifier = SPEEDMODIFIER
	climb_speed = CLIMBSPEED
	jump_force = JUMPFORCE
	delta_xy = 0
	gravity = BASEGRAVITY
	hasJumped = False
	curr_ground_y = BASE_GROUND_Y
	images = []
	
	def __init__(self):
		pygame.sprite.Sprite(self, self.containers)
		self.image = self.images[0]
		self.rect = self.image.rect.get_rect(midbottom-SCREENRECT.midbottom)
	
	def move_horizontal(self,direction):
	# Moves character based on the given direction
		if direction > 0:
			self.image = images[PLAYER_RIGHT_IMAGE]
		else
			self.image = images[PLAYER_LEFT_IMAGE]

		self.rect.move_ip(base_speed*direction,0)
		self.rect.clamp(SCREENRECT)

	def move_vertical(self,delta_time):
	# Moves character by the given delta x/y coordinates
		self.rect.move_ip(0,sel.rect.y + (delta_xy*delta_time))
		self.rect.clamp(SCREENRECT)

		if self.rect.y <= curr_ground_y
			self.rect.move_ip(0,curr_ground_y)
			delta_xy = 0

	def jump():
		hasJumped = True

	def isJumping():
		return hasJumped




	
	
