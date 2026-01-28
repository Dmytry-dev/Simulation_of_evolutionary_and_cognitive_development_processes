#Dmytry-dev
#28.01.2025

import pygame
import sys

def create_window(width, height, panel_width):
    pygame.init()

    #Window initialization
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Evolution Simulator")

    #Fields
    world_field = pygame.Rect(0, 0, width - panel_width, height)
    ui_field = pygame.Rect(width - panel_width, 0, panel_width, height)

    pygame.draw.rect(screen, (255,255,255), world_field)
    pygame.draw.rect(screen, (60, 60, 60), ui_field)
    pygame.draw.line(screen, (0,0,0), (width-panel_width,0), (width-panel_width, height), 2)

    return screen, world_field, ui_field



