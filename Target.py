#!/usr/bin/python3

import pygame
import os

class Target():
    targets = []

    def remove(target):
        Target.targets.remove(target)

    def __init__(self,destroyable):
        self.destroyable = destroyable
        Target.targets.append(self)

    def delete(target):
        Target.targets.remove(target)
        center = target.image.get_rect().center
        target.image = pygame.image.load(os.path.join('Images','flash.png'))
        target.image.get_rect().center = center


    def detectCollison(target, tank):
        if (target.destroyable == True) and pygame.sprite.collide_mask(target, tank):
            Target.delete(target)
