import pygame
import random
import math
pygame.init()

class DrawInformation:

    Black = (22, 24, 29)
    White = (240, 240, 240)
    Green = (46, 160, 115)
    Red = (212, 143, 56)
    Grey = (70, 75, 85)
    Background_color = (22, 24, 29)

    Gradients = [
        (120, 110, 235)
        (140, 130, 245)
        (160, 150, 255)
    ]

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer By Aaliyan Hussain")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.bar_width = math.floor((self.width - 150) / len(lst))
        self.bar_height_multiplier = (self.height - 150) / (self.max_val - self.min_val)
        self.start_x = 75 