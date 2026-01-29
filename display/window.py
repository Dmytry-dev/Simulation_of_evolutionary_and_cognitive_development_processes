#Dmytry-dev
#29.01.2025

import pygame
import sys

class Button:
    def __init__(self, panel_width, y, text, ui_field):
        self.rect = pygame.Rect(ui_field.x + 10, ui_field.y + 10 + 50*y, panel_width-20, 40)
        self.text = text
        self.font = pygame.font.SysFont(None, 36)
        self.color = (70,130,180)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    





def create_window(width, height, panel_width):
    pygame.init()

    #Window initialization
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Evolution Simulator")

    #Fields
    world_field = pygame.Rect(0, 0, width - panel_width, height)
    ui_field = pygame.Rect(width - panel_width, 0, panel_width, height)

    #Buttons
    but1 = Button(panel_width, 0, "Test", ui_field)
    but2 = Button(panel_width, 1, "Test", ui_field)
    but3 = Button(panel_width, 2, "Test", ui_field)
    but4 = Button(panel_width, 3, "Test", ui_field)
    but5 = Button(panel_width, 4, "Test", ui_field)
    but6 = Button(panel_width, 5, "Test", ui_field)



    #Render Fields
    pygame.draw.rect(screen, (255,255,255), world_field)
    pygame.draw.rect(screen, (60, 60, 60), ui_field)
    pygame.draw.line(screen, (0,0,0), (width-panel_width,0), (width-panel_width, height), 2)

    #Render UI
    screen.set_clip(ui_field)
    but1.draw(screen)
    but2.draw(screen)
    but3.draw(screen)
    but4.draw(screen)
    but5.draw(screen)
    but6.draw(screen)

    screen.set_clip(None)






    return screen, world_field, ui_field



