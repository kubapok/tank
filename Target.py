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
    def delete(self):
        Target.targets.remove(self)
