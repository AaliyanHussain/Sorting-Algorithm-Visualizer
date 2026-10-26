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
        self.bubble_button_rect = pygame.Rect(20, 20, 130, 35)

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer By Aaliyan Hussain")
        self.reset_img = pygame.image.load("assets/resetbtn.png").convert_alpha()
        button_x = 800 - self.reset_img.get_width() - 20
        button_y = 20
        self.reset_rect = self.reset_img.get_rect(topleft=(button_x, button_y))
        self.set_list(lst)
        self.font = pygame.font.SysFont('arial', 20)
        self.algo_name = "Bubble Sort"
        self.bubble_button_rect = pygame.Rect(20, 20, 130, 35)
        self.insertion_button_rect = pygame.Rect(160, 20, 140, 35)

        self.image_bubble = pygame.transform.scale(pygame.image.load("assets/bubblesort_btn.png").convert_alpha(), (180, 60))
        self.image_insertion = pygame.transform.scale(pygame.image.load("assets/insertionsort_btn.png").convert_alpha(), (180, 60))
        self.image_merge = pygame.transform.scale(pygame.image.load("assets/mergesort_btn.png").convert_alpha(), (180, 60))

        self.rect_bubble = self.image_bubble.get_rect(topleft=(40, 20))
        self.rect_insertion = self.image_insertion.get_rect(topleft=(240,  20))
        self.rect_merge = self.image_merge.get_rect(topleft=(440, 20))
                                                   

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.bar_width = math.floor((self.width - 150) / len(lst))
        self.bar_height_multiplier = (self.height - 150) / (self.max_val - self.min_val)
        self.start_x = 75 
        

def draw(draw_info, algo_ops={}, clear_bg=False):
    draw_info.window.fill(draw_info.Background_color)
    draw_list(draw_info, algo_ops, clear_bg)
    draw_info.window.blit(draw_info.reset_img, draw_info.reset_rect.topleft)

    draw_info.window.blit(draw_info.image_bubble, draw_info.rect_bubble)
    draw_info.window.blit(draw_info.image_insertion, draw_info.rect_insertion)
    draw_info.window.blit(draw_info.image_merge, draw_info.rect_merge)

    mode_text = draw_info.font.render(f"Current Mode: {draw_info.algo_name}", True, (255, 255, 255))
    draw_info.window.blit(mode_text, (40, 90))
    pygame.display.update()

def generate_starting_list(n, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(n)]

def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.start_x, draw_info.min_val, draw_info.width - draw_info.start_x, draw_info.height - draw_info.min_val)
        pygame.draw.rect(draw_info.window, draw_info.Background_color, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.bar_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.bar_height_multiplier
        color = draw_info.Gradients[i % len(draw_info.Gradients)]

        if i in color_positions:
            color = color_positions[i]

        bar_height = draw_info.height - y
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.bar_width, bar_height))

    if clear_bg:
        pygame.display.update()

def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) -1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw(draw_info, {j: draw_info.Green, j + 1: draw_info.Red}, True)
                yield True
    return lst

def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(1, len(lst)):
        current = lst[i]
        j = i - 1

        while j >= 0 and ((lst[j] > current) if ascending else (lst[j] < current)):
            lst[j + 1] = lst[j]
            j -= 1
            yield {j + 1: draw_info.Green, j: draw_info.Red}, True
        lst[j + 1] = current
        yield {j + 1: draw_info.Green}, True

def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst

    def merge(start, mid, end):
        left = lst[start:mid]
        right = lst[mid:end]
        i = j = 0
        k = start

        while i < len(left) and j < len(right):
            if (left[i] <= right[j]) if ascending else (left[i] >= right[j]):
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = left[i]

            draw(draw_info, {k: draw_info.GREEN}, True)
            yield
            k += 1
        while i < len(left):
            lst[k] = left[i]
            draw(draw_info, {k: draw_info.GREEN}, True)
            yield
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            draw(draw_info, {k: draw_info.GREEN}, True)
            yield
            j += 1
            k += 1

    def merge_sort_rec(start, end):
        if end - start > 1:
            mid = (start + end) // 2
            yield from merge_sort_rec(start, mid)
            yield from merge_sort_rec(mid, end)
            yield from merge(start, mid, end)

    yield from merge_sort_rec(0, len(lst))

def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)

    sorting = False
    ascending = True
    sorting_algorithm = bubble_sort
    sorting_algo_generator = None

    while run:
        clock.tick(60)

        if sorting:
            try:
                next(sorting_algo_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if draw_info.reset_rect.collidepoint(event.pos) and not sorting:
                    lst = generate_starting_list(n, min_val, max_val)
                    draw_info.set_list(lst)
                    sorting = False
                elif draw_info.rect_bubble.collidepoint(event.pos) and not sorting:
                    algo_name = "Bubble Start"
                    sorting_algo_generator = bubble_sort(draw_info, ascending)
                elif draw_info.rect_insertion.collidepoint(event.pos) and not sorting:
                    algo_name = "Insertion Sort"
                    sorting_algo_generator = insertion_sort(draw_info, ascending)
                elif draw_info.rect_merge.collidepoint(event.pos) and not sorting:
                    algo_name = "Merge Sort"
                    sorting_algo_generator = merge_sort(draw_info, ascending)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    lst = generate_starting_list(n, min_val, max_val)
                    draw_info.set_list(lst)
                    sorting = False
                elif event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                    sorting_algo_generator = sorting_algorithm(draw_info, ascending)
                elif event.key == pygame.K_a and not sorting:
                    ascending = True
                elif event.key == pygame.K_d and not sorting:
                    ascending = False
                

    pygame.quit()

if __name__ == "__main__":
    main()
