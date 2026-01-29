#Dmytry-dev
#Render part
#28.02.2026

import pygame
import sys

def camera_view_rect(camera, world_field):
    camera_view = pygame.Rect(
        camera.x,
        camera.y,
        world_field.width,
        world_field.height
    )
    return camera_view

def circle_rect(circle_wx, circle_wy, radius):
    circle_world_rect = pygame.Rect(
        circle_wx - radius,
        circle_wy - radius,
        radius * 2,
        radius * 2
    )
    return circle_world_rect


def center_and_borders(screen, world_field, camera):
    screen.set_clip(world_field)

    camera_view = camera_view_rect(camera, world_field)

    circle_wx, circle_wy = 5000, 5000
    radius = 20

    circle_world_rect = circle_rect(circle_wx, circle_wy, radius)

    if circle_world_rect.colliderect(camera_view):
        sx, sy = camera.world_to_screen(circle_wx, circle_wy, world_field)
        pygame.draw.circle(
            screen,
            (0, 0, 0),
            (sx, sy),
            radius,
            3
        )



    sx, sy = camera.world_to_screen(0, 0, world_field)
    world_screen_rect = pygame.Rect(
        sx,
        sy,
        10000,
        10000
    )
    pygame.draw.rect(
        screen,
        (0, 0, 0),
        world_screen_rect,
        10
    )

    screen.set_clip(None)

def render_objects(object):
    pass