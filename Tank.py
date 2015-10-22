import pygame
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
        self.upper = pygame.image.load('Images/tankUpper.png').convert_alpha()
        self.lower = pygame.image.load('Images/tankLower.png').convert_alpha()
        self.image = pygame.image.load('Images/tankLower.png').convert_alpha()
        self.image = pygame.image.load('Images/tankLower.png').convert_alpha()
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
            self.y -= 5
        elif self.direction == 'right':
            self.x += 5
        elif self.direction == 'down':
            self.y += 5
        elif self.direction == 'left':
            self.x -= 5
        self.rect.x = self.x
        self.rect.y = self.y
