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
        (120, 110, 235),
        (140, 130, 245),
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

def draw_list(draw_info):
    lst = draw_info.lst

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.bar_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.bar_height_multiplier
        color = draw_info.Gradients[i % len(draw_info.Gradients)]

        bar_height = draw_info.height - y

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.bar_width, bar_height))

def draw(draw_info):
    draw_info.window.fill(draw_info.Background_color)
    draw_list(draw_info)
    pygame.display.update()

def generate_starting_list(n, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(n)]

def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)

    while run:
        clock.tick(60)
        draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
