#Dmytry-dev
#30.01.2025

import pygame
import sys
from enum import Enum
from display import camera, input, render, window

class State(Enum):
    VIEW = "VIEW"
    EDITOR = "EDITOR"


def main():
    width = 1200
    height = 800
    panel_width = 300
    world_width = 10000
    world_height = 10000
    speed = 500

    screen = window.create_window(width, height, panel_width)
    world_field, ui_field, buttons = window.simulation_window(screen, width, height, panel_width)
    focus_field = ui_field
    screen_state = State.VIEW

    camera_obj = camera.Camera(world_width, world_height)
    camera_obj.x = world_width // 2 - world_field.width // 2
    camera_obj.y = world_height // 2 - world_field.height // 2
    
    clock = pygame.time.Clock()

    running = True
    while(running):
        dt = clock.tick(60)
        events = pygame.event.get()

        world_input = input.world_inputs(events, world_field)
        ui_inputs = input.ui_inputs(events, focus_field, buttons)
        print(ui_inputs)


        move_speed = speed * dt / 1000

        #Reaction to world actions
        if world_input["quit"]:
            running = False
        if "CAMERA_UP" in world_input["actions"]:
            camera_obj.move(0, -move_speed)
        if "CAMERA_DOWN" in world_input["actions"]:
            camera_obj.move(0, move_speed)
        if "CAMERA_LEFT" in world_input["actions"]:
            camera_obj.move(-move_speed, 0)
        if "CAMERA_RIGHT" in world_input["actions"]:
            camera_obj.move(move_speed, 0)


        #Reactions to UI actions
        if "MAKE" in ui_inputs:
            editor_field, visual_field, buttons = window.open_editor(screen, width, height)
            focus_field = editor_field
            screen_state = State.EDITOR

        if "BACK" in ui_inputs:
            world_field, ui_field, buttons = window.simulation_window(screen, width, height, panel_width)
            focus_field = ui_field
            screen_state = State.VIEW



        camera_obj.clamp(world_field.width, world_field.height)

        #Clearing the world field before a new frame
        if screen_state == "VIEW":
            screen.set_clip(world_field)
            screen.fill((255, 255, 255)) 
            screen.set_clip(None)

            #Rendering objects
            render.center_and_borders(screen, world_field, camera_obj)

        pygame.display.flip()


    
if __name__ == "__main__":
    main()