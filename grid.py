import pygame
import numpy as np
import random

class Grid:
    def __init__(self, width, height, scale, offset):
        # side of the square  
        self.scale = scale

        self.columns = int(height/scale)
        self.rows = int(width/scale)

        # tuple for Example : (5, 10)
        self.size = (self.rows, self.columns)   

        # cellular automata grid 
        self.grid_array = np.ndarray(shape=(self.size))
        
        self.offset = offset

    # intialize the grid with a random values
    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)


    def Conway(self, off_color, on_color, surface, pause,location):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                if location==(x,y) and self.grid_array[x][y]==0 :
                    self.grid_array[x][y] =1

                    on_color = (random.choice([0, 25]), random.choice([0, 50]), random.choice([0, 75]))
                if self.grid_array[x][y] == 1:
                     pygame.draw.ellipse(surface,on_color,[x_pos, y_pos,self.scale-self.offset,self.scale-self.offset])
                else:

                     pygame.draw.ellipse(surface, off_color,[x_pos, y_pos,self.scale-self.offset,self.scale-self.offset])
        next = np.ndarray(shape=(self.size))
        if pause == False:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid_array[x][y]
                    neighbours = self.get_neighbours( x, y)
                    if state == 0 and neighbours == 3:
                        next[x][y] = np.random.choice([0,1],p=[0.2,0.8])
                        on_color=(random.choice([0,25]),random.choice([0,50]),random.choice([0,75]))
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                        next[x][y] = np.random.choice([0,1],p=[0.6,0.4])
                    else:
                        next[x][y] = state
            self.grid_array = next
        return on_color


    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n) % self.rows
                y_edge = (y+m) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total
