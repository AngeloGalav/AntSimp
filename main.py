import pygame
from pygame import time, transform, image, display, gfxdraw, draw
import random as r
from math import floor, cos, tan, sin, pi, sqrt
import numpy as np

pygame.init()

SCREEN_X = 800
SCREEN_Y = 600
CELLSIZE = 4
ANT_SIZE = (15, 30)
AGENT_NUMBER = 1000
NEST_RADIUS = 10
timeout = 10
speed = 2

myClock = time.Clock()
# Set up the drawing window
screen = display.set_mode([SCREEN_X, SCREEN_Y])
display.set_caption('AntSimp')
programIcon = image.load('res/icon.png')
display.set_icon(programIcon)
ant_image = image.load('res/ant_dm.png')
ant_image = transform.scale(ant_image, ANT_SIZE)

class Grid:
    def __init__(self) :
        self.grid = np.zeros((SCREEN_X//CELLSIZE, SCREEN_Y//CELLSIZE))

class PixelAnt: 
    def __init__(self):
        self.x = 0
        self.y = 0 
        self.dir_x = 1
        self.dir_y = 1
        self.trail = Trail()
        self.timeout = 10
        self.current = 0

    def render_ant(self): 
        gfxdraw.pixel(screen, int(self.x), int(self.y), (255,255,255,255))

class PixelTrail: 
    def __init__(self):
        self.x = 0
        self.y = 0 
        self.color = ()
    
    def __init__(self, x, y, color):
        self.x = x
        self.y = y 
        self.color = color
    
    def __str__(self):
        return self.x + ", " + self.y
    
    def render(self) :
        gfxdraw.pixel(screen, int(self.x), int(self.y), self.color)

class Trail:
    def __init__(self):
        self.steps = []
        self.timeout = 10
        self.current = 0

    def insert(self, x):
        self.steps.append(x)

    def __str__(self):
        return self.steps.__str__()

    def render(self): 
        if (self.current >= self.timeout and len(self.steps) > 8) : 
            self.steps.pop(0)
            self.current = 0
        else :
            self.current += 1

        for i in self.steps:
            i.render()

trail_food = Trail()

pixels = []

for i in range(AGENT_NUMBER): 
    pixels.append(PixelAnt())

j = 0
for i in pixels :
    j += 1
    t = 2 * pi * j / AGENT_NUMBER 

    # position ants around the nest
    i.x = int(NEST_RADIUS * cos(t) + SCREEN_X/2)
    i.y = int(NEST_RADIUS * sin(t) + SCREEN_Y/2)

    # spread them out as a circle by setting the direction
    i.dir_x = cos(t)
    i.dir_y = sin(t)

world = Grid()
running = True

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Grid background
    screen.fill((0,0,0))
    for (x,y), value in np.ndenumerate(world.grid):
        if value < 255 : 
            pygame.draw.rect(screen, (0, 0, min(value, 255)), (x*CELLSIZE, y*CELLSIZE, CELLSIZE-1, CELLSIZE-1)) 
        else :
            pygame.draw.rect(screen, (min(value - 255, 255), min(value - 255, 255), 255), (x*CELLSIZE, y*CELLSIZE, CELLSIZE-1, CELLSIZE-1)) 

    # Draw each ant
    for i in pixels :
        # i.dir_x = cos()
        # i.dir_y = sqrt(1 - i.dir_x**2)

        i.x += speed * i.dir_x
        i.y += speed * i.dir_y

        if i.x > SCREEN_X - 1 or i.x < 1:
            i.dir_x *= -1 
        if i.y > SCREEN_Y - 1 or i.y < 1:
            i.dir_y *= -1 

        world.grid[floor(i.x/CELLSIZE) - 1][floor(i.y/CELLSIZE) - 1] += 10

        i.render_ant()

    # Draw nest
    pygame.draw.circle(screen, (165, 255, 0), (SCREEN_X/2, SCREEN_Y/2), NEST_RADIUS - 2);

    myClock.tick(120)
    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
