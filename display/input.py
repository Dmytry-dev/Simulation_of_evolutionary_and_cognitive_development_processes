#Dmytry-dev
#30.01.2026

import pygame

def world_inputs(events, world_field):
    actions = set()
    quit_requested = False
    mouse_pos = pygame.mouse.get_pos()

    #Quit
    for event in events:
        if event.type == pygame.QUIT:
            quit_requested = True

    #Keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        actions.add("CAMERA_UP")
    if keys[pygame.K_s]:
        actions.add("CAMERA_DOWN")
    if keys[pygame.K_a]:
        actions.add("CAMERA_LEFT")
    if keys[pygame.K_d]:
        actions.add("CAMERA_RIGHT")



    

    return {"quit": quit_requested, "actions": actions, "mouse_pos": mouse_pos}

def ui_inputs(events, ui_field, buttons):
    ui_inputs = set()
    mouse_pos = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in buttons:
                ui_inputs.add(button.handle_event(event, ui_field))
    return(ui_inputs)


