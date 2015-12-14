#!/usr/bin/python3

import pygame
import os
import random
from Target import *


class Boat(pygame.sprite.Sprite, Target):

    boatLeft = pygame.image.load(os.path.join('Images','boatLeft.png'))
    boatRight = pygame.image.load(os.path.join('Images','boatRight.png'))
    timeShift = 90

    def __init__(self,x,y,pos = 'left'):
        assert pos in ('left', 'right')
        pygame.sprite.Sprite.__init__(self)
        Target.__init__(self, True,'boat')
        if pos == 'left':
            self.image =  Boat.boatLeft
        else:
            self.image = Boat.boatRight
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def display(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))
        if random.random() > 0.99:
            if self.image == Boat.boatLeft:
                self.image =Boat.boatRight
            else:
                self.image = Boat.boatLeft
