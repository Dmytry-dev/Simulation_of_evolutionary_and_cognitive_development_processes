#Dmytry dev
#Cell structure
#27.01.2026
#V 0.1

import math
import pygame

class Cell:
    def __init__(self, name, color):
        self.type = "Cell"
        self.name = name
        self.col = color
        self.X = 0
        self.Y = 0

    def user_spawn(self, X, Y):
        self.X = X
        self.Y = Y        
        
        

            