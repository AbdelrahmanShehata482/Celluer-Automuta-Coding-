import pygame
import time
import random
import numpy as np
import os
import grid

os.environ["SDL_VIDEO_CENTERED"]='1'

#resolution
width, height = 1000,800
size = (width, height)

pygame.init()

pygame.display.set_caption("GAME OF LIFE")

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 10

black = (0, 0, 0)
blue = (0, 121, 150)
purple = (255,0,255)
white = (255, 255, 255)


scaler = 50
offset = 1

Grid = grid.Grid(width,height, scaler, offset)
Grid.random2d_array()

pause = False
run = True
location=()
while run:
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                pause = not pause
        if event.type==pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos=pygame.mouse.get_pos()
                location=(pos[0]//scaler,int(pos[1]/scaler))
    purple= Grid.Conway(off_color=white, on_color=purple, surface=screen, pause=pause,location=location)

   


    pygame.display.update()

pygame.quit()
