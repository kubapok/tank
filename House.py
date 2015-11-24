#!/usr/bin/python3

import pygame
import os
from Target import *


class House(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        Target.__init__(self, False)
        self.image= pygame.image.load(os.path.join('Images','house.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.destroyable = True
    def display(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))
