# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:04:00 2023

@author: laurin
"""

import numpy as np
import pygame
from random import random,sample
from itertools import product

# this class handles the board and everything the needs to be calculated
class board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        # this handles stores a boolean for each cell
        self.board = np.zeros((height,width))
        num_of_cells = height*width
        # between 10% and 20% of the cells are randomly alive in the beginning
        alive = int(0.1*num_of_cells + random()*0.1*num_of_cells)
        alive_array = sample(list(product(range(height), range(width))), k=alive)
        for t in alive_array:
            self.board[t[0]][t[1]] = 1
        
    def __draw__(self):
        BLACK = (0, 0, 0)
        WHITE = (200, 200, 200)
        
        pygame.init()
        SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        w, h = pygame.display.get_surface().get_size()
        SCREEN.fill(BLACK)
        blockSize = int(w/self.width)
        running = True
        
        iterations = 0
        pygame.mouse.set_visible(False)
        while True:
            if iterations < 2:
                iterations +=1 
            for x in range(0, w, blockSize):
                for y in range(0, h, blockSize):
                    rect = pygame.Rect(x, y, blockSize, blockSize)
                    position_y = int(x/blockSize)
                    position_x = int(y/blockSize)
                    value = self.board[position_x][position_y]
                    color = tuple([c*value for c in WHITE])
                    pygame.draw.rect(SCREEN, color, rect, 0)
            self.__update__()

            # this is the only way I found that halts the program on any event which occurs after starting the screensaver
            for _ in pygame.event.get():
                if iterations > 1:
                    running = False
            if not running:
                break
    
            pygame.display.update()
        pygame.quit()

    def __update__(self):
        copied_board = np.copy(self.board)
        for i in range(self.height):
            for j in range(self.width):
                value = self.board[i][j]
                neighbours = [((i+1)%self.height, j), 
                              ((i-1)%self.height, j),
                              (i,(j+1)%self.width),
                              (i,(j-1)%self.width),
                              ((i+1)%self.height,(j+1)%self.width),
                              ((i-1)%self.height,(j+1)%self.width),
                              ((i+1)%self.height,(j-1)%self.width),
                              ((i-1)%self.height,(j-1)%self.width)]
                alive_neighbours = 0
                for n in neighbours:
                    if self.board[n[0]][n[1]] == 1:
                        alive_neighbours += 1
                if (value == 1) and ((alive_neighbours < 2) or (alive_neighbours > 3)):
                    copied_board[i][j] = 0
                elif (value == 1) and ((alive_neighbours == 2) or (alive_neighbours == 3)):
                    copied_board[i][j] = 1
                elif (value == 0) and (alive_neighbours == 3):
                    copied_board[i][j] = 1
                else:
                    copied_board[i][j] = 0
        self.board = copied_board

                
                