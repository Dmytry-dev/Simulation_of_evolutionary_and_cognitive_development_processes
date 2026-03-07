#Dmytry-dev
#Window Creator
#07.03.2025

import pygame
import sys

    
def create_window(width, height):
    pygame.init()

    #Window initialization
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Evolution Simulator")
    
    return screen


def simulation_window(screen, width, height, debug_panel, information_panel):
    #Fields
    world_field = pygame.Rect(0, 0, width - debug_panel, height - information_panel)
    debug_field = pygame.Rect(width - debug_panel, 0, debug_panel, height - information_panel)
    information_field = pygame.Rect(0, height - information_panel, width, information_panel)

    #Render Fields
    pygame.draw.rect(screen, (255,255,255), world_field)
    pygame.draw.rect(screen, (60, 60, 60), debug_field)
    pygame.draw.rect(screen, (30,30,30), information_field)
    #pygame.draw.line(screen, (0,0,0), (width-debug_panel,0), (width-debug_panel, height - information_panel), 3)
    #pygame.draw.line(screen, (0,0,0), (50,height-information_panel), (width, height - information_panel), 3)

    return world_field, debug_field, information_field