#Dmytry-dev
#30.01.2025

import pygame
import sys

class Button:
    def __init__(self, panel_width, y, text, ui_field, callback):
        self.rect = pygame.Rect(ui_field.x + 10, ui_field.y + 10 + 50*y, panel_width-20, 40)
        self.text = text
        self.font = pygame.font.SysFont(None, 36)
        self.color = (200,200,200)
        self.callback = callback

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

        text_surf = self.font.render(self.text, True, (0,0,0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def handle_event(self, event, ui_field):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ui_field.collidepoint(event.pos):
                if self.rect.collidepoint(event.pos):
                    return self.callback

    





def create_window(width, height, panel_width):
    pygame.init()

    #Window initialization
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Evolution Simulator")

    #Fields
    world_field = pygame.Rect(0, 0, width - panel_width, height)
    ui_field = pygame.Rect(width - panel_width, 0, panel_width, height)

    #Buttons
    spawn_butt = Button(panel_width, 0, "Spawn", ui_field, "SPAWN")
    select_butt = Button(panel_width, 1, "Select", ui_field, "SELECT")
    make_butt = Button(panel_width, 2, "Make", ui_field, "MAKE")

    buttons = [spawn_butt, select_butt, make_butt]





    #Render Fields
    pygame.draw.rect(screen, (255,255,255), world_field)
    pygame.draw.rect(screen, (60, 60, 60), ui_field)
    pygame.draw.line(screen, (0,0,0), (width-panel_width,0), (width-panel_width, height), 2)

    #Render UI
    screen.set_clip(ui_field)
    spawn_butt.draw(screen)
    select_butt.draw(screen)
    make_butt.draw(screen)

    screen.set_clip(None)






    return screen, world_field, ui_field, buttons



