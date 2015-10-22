#!/usr/bin/python3

import pygame
import os
from rot_center import *

class Tank(pygame.sprite.Sprite):
    '''represents a tank,
    allows to move, change direction, shot
    tower moves separatly'''

    toLeft = {  'up' : 'left',
                'left' : 'down',
                'down' : 'right',
                'right' : 'up'  }

    toRight = {  'up' : 'right',
                'right' : 'down',
                'down' : 'left',
                'left' : 'up'  }

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 1
        self.upper = pygame.image.load(os.path.join('Images','tankUpper.png')).convert_alpha()
        self.lower = pygame.image.load(os.path.join('Images','tankLower.png')).convert_alpha()
        self.image = pygame.image.load(os.path.join('Images','tankLower.png')).convert_alpha()
        self.image = pygame.image.load(os.path.join('Images','tankLower.png')).convert_alpha()
        self.rect = self.lower.get_rect()
        self.x = x
        self.y = y
        self.direction = 'up'
        self.target = 'up'

    def turnRight(self):
        self.direction = Tank.toRight[self.direction]
        self.target = Tank.toRight[self.target]
        self.lower = rot_center(self.lower, 270)
        self.upper = rot_center(self.upper, 270)
    def turnLeft(self):
        self.direction = Tank.toLeft[self.direction]
        self.target = Tank.toLeft[self.target]
        self.lower = rot_center(self.lower, 90)
        self.upper = rot_center(self.upper, 90)
    def towerRight(self):
        self.target = Tank.toRight[self.target]
        self.upper = rot_center(self.upper, 270)
    def towerLeft(self):
        self.target = Tank.toLeft[self.target]
        self.upper = rot_center(self.upper, 90)
    def move(self):
        if self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'down':
            self.y += self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        self.rect.x = self.x
        self.rect.y = self.y
    def display(self, display):
        display.blit(self.lower, (self.x, self.y))
        display.blit(self.upper, (self.x, self.y))
