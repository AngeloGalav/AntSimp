import pygame
from pygame import time, Rect
import random as r
from math import floor, cos, tan, sin, pi
from pygame import gfxdraw

pygame.init()

SCREEN_X = 1280
SCREEN_Y = 720
AGENT_NUMBER = 100
NEST_RADIUS = 10
speed = 2

myClock = time.Clock()
myClock.tick(60)
 
# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_X, SCREEN_Y])
pygame.display.set_caption('AntSimp')
programIcon = pygame.image.load('res/icon.png')
ant_image = pygame.image.load('res/ant_dm.png')
ant_image = pygame.transform.scale(ant_image, (15, 30))

pygame.display.set_icon(programIcon)

class Ant: 
    def __init__(self):
        self.x = 0
        self.y = 0 
        self.dir_x = 1
        self.dir_y = 1
    
    def render_ant(self): 
        screen.blit(ant_image, (self.x, self.y))

pixels = []


for i in range(AGENT_NUMBER): 
    pixels.append(Ant())

j = 0
for i in pixels :
    j += 1
    t = 2 * pi * j / AGENT_NUMBER 

    i.x = int(NEST_RADIUS * cos(t) + SCREEN_X/2)
    i.y = int(NEST_RADIUS * sin(t) + SCREEN_Y/2)

    i.dir_x = cos(t)
    i.dir_y = sin(t)

# Run until the user asks to quit
running = True
i = 0
screen.fill((0, 0, 50))
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Grid background
    screen.fill((0, 0, 50))

    # Draw a solid blue circle in the center
    for i in pixels :
        i.x += speed * i.dir_x
        i.y += speed * i.dir_y


        if i.x > SCREEN_X - 1 or i.x < 1:
            i.dir_x *= -1 
        if i.y > SCREEN_Y - 1 or i.y < 1:
            i.dir_y *= -1 

        # gfxdraw.pixel(screen, int(i.x), int(i.y), (255,255,255,255))
        i.render_ant()
    
    pygame.draw.circle(screen, (165, 99, 0), (SCREEN_X/2, SCREEN_Y/2), NEST_RADIUS - 2);

    myClock.tick(30)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
