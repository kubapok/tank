#!/usr/bin/python3
import pygame

def rotate_center(image, angle):
    center_of_image = image.get_rect().center
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image.get_rect().center = center_of_image
    return rotated_image
