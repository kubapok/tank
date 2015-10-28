#!/usr/bin/python3

import pygame
import os
from Target import *
from rot_center import *


class Fence(pygame.sprite.Sprite, Target):
    def __init__(self,x,y,version):
        pygame.sprite.Sprite.__init__(self)
        Target.__init__(self,True)
        image = 'fence' + str(version) + '.png'
        try:
            self.image= pygame.image.load(os.path.join('Images',image)).convert_alpha()
        except pygame.error:
            print("There is no image: " + image + ".\nLoading fence1.png")
            if ERRORDISPLAY:
                self.image= pygame.image.load(os.path.join('Images','fence1.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def display(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))
