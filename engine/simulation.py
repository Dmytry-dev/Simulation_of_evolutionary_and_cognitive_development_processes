
import pygame
from multiprocessing.connection import Client
from engine.display import camera, inputs, render, window


def simulation_start():
    width = 1200
    height = 1000
    debug_panel = 300
    information_panel = 200
    world_width = 10000
    world_height = 10000
    speed = 500

    conn_sim = Client(('localhost', 6001))


    screen = window.create_window(width, height)
    world_field, debug_field, information_panel = window.simulation_window(screen, width, height, debug_panel, information_panel)

    camera_obj = camera.Camera(world_width, world_height)
    camera_obj.x = world_width // 2 - world_field.width // 2
    camera_obj.y = world_height // 2 - world_field.height // 2
    
    clock = pygame.time.Clock()


    while True:
        dt = clock.tick(60)
        events = pygame.event.get()

        world_input = inputs.world_inputs(events, world_field)

        move_speed = speed * dt / 1000

        #Listening main process
        if conn_sim.poll():
            msg = conn_sim.recv()
            if msg == "e":
                break

        #Reaction to world actions
        if world_input["quit"]:
            break
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

