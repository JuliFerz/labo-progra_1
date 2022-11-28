import pygame
from constantes import *


# cosas de la gráfica
class Widget:
    def __init__(self, main_surface, main_rect, x, y, w, h, color_background, color_border=''):
        self.main_surface = main_surface
        self.main_rect = main_rect
        self.color_background = color_background
        self.color_border = color_border
        self.x, self.y, self.w, self.h = x, y, w, h

        # slave_widget_surface
        self.slave_widget_surface = pygame.Surface((self.w, self.h))
        self.slave_widget_rect = self.slave_widget_surface.get_rect(
            center=(self.x, self.y))
        self.slave_widget_rect_collide = self.slave_widget_surface.get_rect(
            center=(
                self.x + self.main_rect.x,
                self.y + self.main_rect.y
            ))

    def render(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.main_surface.blit(
            self.slave_widget_surface,
            self.slave_widget_rect)
