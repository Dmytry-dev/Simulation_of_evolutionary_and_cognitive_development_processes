#Dmytry-dev
#07.03.2025

import pygame, os, json, colorama
from colorama import Fore, Style
from multiprocessing import Process, Pipe

from display import camera, inputs, render, window

from engine.saves import save_load
from engine.structures import Cells, Gen
from engine.world import world 
from engine.genetic_editor import editor_shell


def main():
    
    menu_text = Fore.YELLOW + "======================\nMENU\n======================\n" + Style.RESET_ALL

    main_conn, simulation_conn = Pipe()

    simulation_process = False

    print(menu_text)

    while True:
        cmd = input("User: > ")
        
        if cmd == "-e":
            break
        elif cmd == "-s":
            p = Process(target=simulation)
            simulation_process = True
            p.start()
        elif cmd == "-ed":
            editor_shell.start_window()

        else:
            print(f"Unknown command: {cmd}")
    if simulation_process == True:
        p.join()

    return 0


def simulation():
    width = 1200
    height = 1000
    debug_panel = 300
    information_panel = 200
    world_width = 10000
    world_height = 10000
    speed = 500


    screen = window.create_window(width, height)
    world_field, debug_field, information_panel = window.simulation_window(screen, width, height, debug_panel, information_panel)

    camera_obj = camera.Camera(world_width, world_height)
    camera_obj.x = world_width // 2 - world_field.width // 2
    camera_obj.y = world_height // 2 - world_field.height // 2
    
    clock = pygame.time.Clock()

    running = True
    while(running):
        dt = clock.tick(60)
        events = pygame.event.get()

        world_input = inputs.world_inputs(events, world_field)

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
        

        camera_obj.clamp(world_field.width, world_field.height)

        #Clearing the world field before a new frame
        screen.set_clip(world_field)
        screen.fill((255, 255, 255)) 
        screen.set_clip(None)

        #Rendering objects
        render.center_and_borders(screen, world_field, camera_obj)

        pygame.display.flip()


    
if __name__ == "__main__":
    main()