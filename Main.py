import pygame, sys
from pygame.locals import *
pygame.init()
FPS = 3 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
DISPLAYSURF = pygame.display.set_mode((900, 700), 0, 32)
pygame.display.set_caption('tank game')
WHITE = (255, 255, 255)
tank = pygame.image.load('Images/tank.png')
tank = pygame.image.load('Images/tank.png')
tankx = 100
tanky = 100
direction = 'right'

def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    loc = image.get_rect().center
    rot_sprite = pygame.transform.rotate(image, angle)
    rot_sprite.get_rect().center = loc
    return rot_sprite

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if direction == 'right':
        tankx += 5
        if tankx == 300:
            direction = 'down'
    elif direction == 'down':
        tanky += 5
        if tanky == 300:
            direction = 'left'
    elif direction == 'left':
        tankx -= 5
        if tankx == 100:
            direction = 'up'
    elif direction == 'up':
        tanky -= 5
        if tanky == 100:
            direction = 'right'

    tank = rot_center(tank, 90)
    DISPLAYSURF.blit(tank, (tankx, tanky))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
