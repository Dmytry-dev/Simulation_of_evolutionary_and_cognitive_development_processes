#Dmytry-dev
#Display part
#27.02.2026
#V 0.1


import pygame
import sys
import main

def display_open():
    pygame.init()

    # window and settings
    width = 1200
    height = 800
    panel_width = 300
    world_width = 10000
    world_height = 10000



    # Window initialization
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Evolution Simulator")
    clock = pygame.time.Clock()

    # Fields
    field_rect = pygame.Rect(0, 0, width - panel_width, height)
    ui_rect = pygame.Rect(width - panel_width, 0, panel_width, height)

    # Camera
    camera_x = 0
    camera_y = 0
    zoom = 1.0

    running = True
    objects = []

    while running:
        
        # Events
        for event in pygame.event.get():
            # Close
            if event.type == pygame.QUIT:
                running = False
            # Zoom
            if event.type == pygame.MOUSEWHEEL:
                zoom *= 1.1 if event.y > 0 else 0.9
                zoom = max(0.1, min(zoom, 5))
            # Click
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if field_rect.collidepoint(mouse_x, mouse_y):
                    world_x = (mouse_x - field_rect.x) / zoom + camera_x
                    world_y = (mouse_y - field_rect.y) / zoom + camera_y
                    #-------------------------------------------------
                    objects.append(main.make_cell(world_x, world_y))
                    #-------------------------------------------------

                    

        # Camera move
        keys = pygame.key.get_pressed()
        speed = 10 / zoom

        if keys[pygame.K_a]:
            camera_x -= speed
        if keys[pygame.K_d]:
            camera_x += speed
        if keys[pygame.K_w]:
            camera_y -= speed
        if keys[pygame.K_s]:
            camera_y += speed

        # Camera Limits
        max_x = world_width - field_rect.width / zoom
        max_y = world_height - field_rect.height / zoom

        camera_x = max(0, min(camera_x, max_x))
        camera_y = max(0, min(camera_y, max_y))
        
        screen.fill((30,30,30))

        # Draw fields
        pygame.draw.rect(screen, (255,255,255), field_rect)
        pygame.draw.rect(screen, (60, 60, 60), ui_rect)
        pygame.draw.line(screen, (0,0,0), (width-panel_width,0), (width-panel_width, height), 2)

        # Draw objects in world
        screen.set_clip(field_rect)
        #-----------Test object----------------
        world_x, world_y = 5000, 5000

        screen_x = field_rect.x + (world_x - camera_x) * zoom
        screen_y = field_rect.y + (world_y - camera_y) * zoom

        pygame.draw.circle(
            screen,
            (200,80,80),
            (int(screen_x), int(screen_y)),
            max(2, int(20*zoom))
        )
        #---------------------------------------

        render_object(screen, objects, zoom, field_rect, camera_x, camera_y)

        screen.set_clip(None)
        
        # Frame Drawing
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


def render_object(screen, objects, zoom, field_rect, camera_x, camera_y):
    for object in objects:
        if object.type == "Cell":
            screen_x = field_rect.x + (object.X - camera_x) * zoom
            screen_y = field_rect.y + (object.Y - camera_y) * zoom

            pygame.draw.circle(
                screen,
                object.col,
                (int(screen_x), int(screen_y)),
                max(2, int(20*zoom))
            )



    
    

