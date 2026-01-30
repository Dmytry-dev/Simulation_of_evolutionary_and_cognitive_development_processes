#Dmytry-dev
#30.01.2025

import pygame
import sys

class Button:
    def __init__(self, width, x, y, text, field, callback):
        self.rect = pygame.Rect(field.x + 10 + 50*x, field.y + 10 + 50*y, width-20, 40)
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
    
    return screen



def simulation_window(screen, width, height, panel_width):
    #Fields
    world_field = pygame.Rect(0, 0, width - panel_width, height)
    ui_field = pygame.Rect(width - panel_width, 0, panel_width, height)

    #Buttons
    spawn_butt = Button(panel_width, 0, 0, "Spawn", ui_field, "SPAWN")
    select_butt = Button(panel_width, 0, 1, "Select", ui_field, "SELECT")
    make_butt = Button(panel_width, 0, 2, "Make", ui_field, "MAKE")

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

    return world_field, ui_field, buttons

def open_editor(screen, width, height):
    #Open Editor Fields
    editor_field = pygame.Rect(0,0,width/2,height)
    visual_field = pygame.Rect(width/2,0,width/2,height)

    #Buttons
    back_butt = Button(width/8, 0, 0, "Back",editor_field, "BACK")
    morph_butt = Button(width/8, 3, 0, "Morphogen", editor_field, "test")
    action_butt = Button(width/8, 6, 0, "Action", editor_field, "test")
    timer_butt = Button(width/8, 9, 0, "Timer", editor_field, "test")

    buttons = [back_butt,morph_butt,action_butt,timer_butt]


    #Render Editor Fields
    pygame.draw.rect(screen, (255,255,255), editor_field)
    pygame.draw.rect(screen, (60,60,60), visual_field)
    pygame.draw.line(screen, (0,0,0), (width/2, 0), (width/2, height), 2)

    #Render Editor UI
    screen.set_clip(editor_field)
    back_butt.draw(screen)
    morph_butt.draw(screen)
    action_butt.draw(screen)
    timer_butt.draw(screen)

    screen.set_clip(None)

    return editor_field, visual_field, buttons
    










