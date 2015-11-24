#!/usr/bin/python3

import pygame
import os
import random

class Target():
    targets = []

    def __init__(self,destroyable):
        self.targetName = None
        self.destroyable = destroyable
        Target.targets.append(self)


    def delete(target):
        if target.targetName == 'train':
            target.kill()
            flash = Destroyed(target.rect.x + target.image.get_rect().centerx,target.rect.y + target.image.get_rect().centery)
        elif target.targetName == 'sheep':
            blood = Destroyed(target.rect.x + target.image.get_rect().centerx,target.rect.y + target.image.get_rect().centery, blood = True)
            Target.targets.remove(target)
        else:
            flash = Destroyed(target.rect.x + target.image.get_rect().centerx,target.rect.y + target.image.get_rect().centery)
            Target.targets.remove(target)


    def detectCollison(target, tank):
        if (target.destroyable == True) and pygame.sprite.collide_mask(target, tank):
            return True


class Destroyed(pygame.sprite.Sprite,Target):
    destroyed = []
    displayFlashTime = 15
    displayFlashTimeShift = 15
    displayFlashPosShift = 20

    def __init__(self,x,y, blood = False):
        pygame.sprite.Sprite.__init__(self)
        self.displayFlash = Destroyed.displayFlashTime + int(random.random()*2*Destroyed.displayFlashTimeShift)
        if blood == False:
            self.image = pygame.image.load(os.path.join('Images','flash.png')).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join('Images','blood.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x - self.image.get_rect().centerx
        self.rect.y = y - self.image.get_rect().centery
        Destroyed.destroyed.append(self)

    def delete(destroyed):
        Destroyed.destroyed.remove(destroyed)

    def display(self, display):
        if self.displayFlashTime:
            display.blit(self.image, (self.rect.x + int(random.random()*2*Destroyed.displayFlashPosShift) - Destroyed.displayFlashPosShift,
                self.rect.y + int(random.random()*2*Destroyed.displayFlashPosShift) - Destroyed.displayFlashPosShift))
            self.displayFlashTime -= 1
        else:
            Destroyed.delete(self)
