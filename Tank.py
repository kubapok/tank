#!/usr/bin/python3

import pygame
import os
from rotate_center import *

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
        self.speed = 2
        self.upper = pygame.image.load(os.path.join('Images','tankUpper.png')).convert_alpha()
        self.lower = pygame.image.load(os.path.join('Images','tankLower.png')).convert_alpha()
        self.image = pygame.image.load(os.path.join('Images','tankLower.png')).convert_alpha()
        self.rect = self.lower.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = 'up'
        self.aim = 'up'
        self.rush = False

    def turnRight(self):
        self.direction = Tank.toRight[self.direction]
        self.aim = Tank.toRight[self.aim]
        self.lower = rotate_center(self.lower, 270)
        self.upper = rotate_center(self.upper, 270)
    def turnLeft(self):
        self.direction = Tank.toLeft[self.direction]
        self.aim = Tank.toLeft[self.aim]
        self.lower = rotate_center(self.lower, 90)
        self.upper = rotate_center(self.upper, 90)
    def towerRight(self):
        self.aim = Tank.toRight[self.aim]
        self.upper = rotate_center(self.upper, 270)
    def towerLeft(self):
        self.aim = Tank.toLeft[self.aim]
        self.upper = rotate_center(self.upper, 90)
    def move(self):
        if self.direction == 'up':
            self.rect.y -= self.speed
        elif self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'down':
            self.rect.y += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed
    def display(self, display):
        display.blit(self.lower, (self.rect.x, self.rect.y))
        display.blit(self.upper, (self.rect.x, self.rect.y))

    def setRush(self, value):
        assert value in (True, False)
        self.rush = value

    def shoot(self):
        shoot = Bullet(self.rect.x, self.rect.y, self.aim)

class Bullet(pygame.sprite.Sprite):
    bullets = []
    speed = 15
    existTime = 10000

    def __init__(self,x,y, aim):
        self.image = pygame.image.load(os.path.join('Images','bullet.png')).convert_alpha()
        print(aim)
        if aim == 'up':
            pass
        elif aim == 'right':
            self.image = rotate_center(self.image, 270)
        elif aim == 'down':
            self.image = rotate_center(self.image, 180)
        elif aim == 'left':
            self.image = rotate_center(self.image, 90)
        else:
            assert False

        self.lifeTime = Bullet.existTime
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = aim

        Bullet.bullets.append(self)

    def move(self):
        if self.direction == 'up':
            self.rect.y -= Bullet.speed
        elif self.direction == 'right':
            self.rect.x += Bullet.speed
        elif self.direction == 'down':
            self.rect.y += Bullet.speed
        elif self.direction == 'left':
            self.rect.x -= Bullet.speed
        else:
            assert False

    def display(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))
        self.existTime -= 1
        if self.existTime <=0:
            self.remove()


    def remove(self):
        Bullet.bullets.remove(self)
