#!/usr/bin/python3

import pygame
import os
from Target import *
from rot_center import *


class Tree(pygame.sprite.Sprite):

	def __init__(self,x,y, color = 'dark'):
		assert color in ('dark', 'light')
		pygame.sprite.Sprite.__init__(self)
		Target.__init__(self, True,'tree')
		if color == 'dark':
			self.image =  pygame.image.load(os.path.join('Images','treeDark.png')).convert_alpha()
		elif color == 'light':
			self.image =  pygame.image.load(os.path.join('Images','treeLight.png')).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
	def display(self, display):
		display.blit(self.image, (self.rect.x, self.rect.y))
