#!/usr/bin/python3

import pygame
import os


class Target():
    targets = []
    def __init__(self,destroyable):
        self.destroyable = destroyable
        Target.targets.append(self)
