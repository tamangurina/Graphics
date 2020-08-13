import pygame
import math
import time

# Ignore these 3 functions. Scroll down for the relevant code.
pygame.init()

green = (0,255,0)
blue = (0,0,255)

width = 400
height = 400
def create_background(width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        background = pygame.Surface((width, height))
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(
                                background, 
                                colors[(row + col) % 2],
                                pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width
        return background

def do_polygon_demo(surface, counter):        
        num_points = 12
        point_list = []
        center_x = surface.get_width() // 2
        center_y = surface.get_height() // 2
        for i in range(num_points * 2):
                radius = 50
                if i % 2 == 0:
                        radius = radius // 2
                ang = i * 3.14159 / num_points + counter * 3.14159 / 45
                x = center_x + int(math.cos(ang) * radius)
                y = center_y + int(math.sin(ang) * radius)
                point_list.append((x, y))
                print(x,y)
        pygame.draw.polygon(surface, green, point_list)

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('press space to see next demo')
background = create_background(width, height)
clock = pygame.time.Clock()
while True:
        screen.blit(background, (0, 0))
        do_polygon_demo(screen, 0)
        pygame.display.flip()



   
