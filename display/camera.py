#Dmytry-dev
#Display part
#27.02.2026
#V 0.1

import pygame 

class Camera:
    def __init__(self, world_width, world_height):
        self.x = 0
        self.y = 0

        self.world_width = world_width
        self.world_height = world_height

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def clamp(self, view_width, view_height):
        self.x = max(0, min(self.x, self.world_width - view_width))
        self.y = max(0, min(self.y, self.world_height - view_height))

    def world_to_screen(self, wx, wy, field_rect):
        sx = field_rect.x + (wx - self.x)
        sy = field_rect.y + (wy - self.y)
        return int(sx), int(sy)

