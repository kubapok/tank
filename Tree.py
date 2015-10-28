#!/usr/bin/python3

import pygame
import os
from Target import *
from rot_center import *


class Tree(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        Target.__init__(self, True)
        self.image= pygame.image.load(os.path.join('Images','tree.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))
