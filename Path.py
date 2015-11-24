#!/usr/bin/python3

import pygame
import os
from Target import *


class Path(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        Target.__init__(self, False)
        self.image= pygame.image.load(os.path.join('Images','path.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))
