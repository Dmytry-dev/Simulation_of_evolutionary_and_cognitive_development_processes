#Dmytry-dev
#28.01.2025

import pygame
import sys
from display import camera, input, render, window


def main():
    width = 1200
    height = 800
    panel_width = 300
    world_width = 10000
    world_height = 10000
    speed = 500

    screen, world_field, ui_rect = window.create_window(width, height, panel_width)
    camera_obj = camera.Camera(world_width, world_height)
    camera_obj.x = world_width // 2 - world_field.width // 2
    camera_obj.y = world_height // 2 - world_field.height // 2
    
    clock = pygame.time.Clock()

    running = True
    while(running):
        dt = clock.tick(60)
        input_state = input.world_inputs(world_field)
        move_speed = speed * dt / 1000

        #Reaction to actions
        if input_state["quit"]:
            running = False
        if "CAMERA_UP" in input_state["actions"]:
            camera_obj.move(0, -move_speed)
        if "CAMERA_DOWN" in input_state["actions"]:
            camera_obj.move(0, move_speed)
        if "CAMERA_LEFT" in input_state["actions"]:
            camera_obj.move(-move_speed, 0)
        if "CAMERA_RIGHT" in input_state["actions"]:
            camera_obj.move(move_speed, 0)

        camera_obj.clamp(world_field.width, world_field.height)

        #Clearing the world field before a new frame
        screen.set_clip(world_field)
        screen.fill((255, 255, 255)) 
        screen.set_clip(None)

        pygame.display.flip()


    






if __name__ == "__main__":
    main()