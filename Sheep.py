#!/usr/bin/python3

import pygame
import os
from Target import *
from rot_center import *


class Sheep(pygame.sprite.Sprite,Target):
    def __init__(self,x,y,direction, speed = 1):
        assert (direction == 'left' or direction == 'right')
        pygame.sprite.Sprite.__init__(self)
        Target.__init__(self,True)
        self.image= pygame.image.load(os.path.join('Images','sheep.png')).convert_alpha()
        if direction == 'left':
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.speed = speed

    def display(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, speed = None):
        if self.direction == 'right':
            if speed == None:
                self.rect.x += self.speed
            else:
                self.rect.x += speed
        elif self.direction == 'left':
            if speed == None:
                self.rect.x -= self.speed
            else:
                self.rect.x -= speed

    def turnIfCollide(self):
        if self.rect.x > 900:
            self.direction = 'left'
            self.image = pygame.transform.flip(self.image, True, False)
            return

        for target in Target.targets:
            if target != self and pygame.sprite.collide_mask(self, target):
                if self.direction == 'right':
                    self.direction = 'left'
                    self.image = pygame.transform.flip(self.image, True, False)
                elif self.direction  == 'left':
                    self.direction = 'right'
                    self.image = pygame.transform.flip(self.image, True, False)
                self.move(10)
