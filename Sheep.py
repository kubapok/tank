#!/usr/bin/python3

import pygame
import os
from rot_center import *


class Sheep():
    def __init__(self,x,y):
        super().__init__()
        self.image= pygame.image.load(os.path.join('Images','sheep.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))
