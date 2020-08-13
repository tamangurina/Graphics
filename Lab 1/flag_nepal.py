import pygame, sys
from pygame.locals import *
from sys import exit

import math

pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkblue = (0,0,255)
pi = 3.14

#dimension of pygame window
screen = pygame.display.set_mode((600,600))

#caption
pygame.display.set_caption("Flag of Nepal")

# Loop Switch
done = False

# Screen Update Speed (FPS)
clock = pygame.time.Clock()

#Polygon function to draw triangle
def drawPolygon(screen, points):
    pygame.draw.polygon(screen, white, points, 0)

# ------- Main Program Loop -------
while not done:
    # --- Main Quit Event Loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  
    screen.fill(black)
    # This draws a flag using the polygon command
    pygame.draw.polygon(screen, red, [[90, 143], [400,310], [215, 310],[400, 500],[90, 500]], 0)
    pygame.draw.polygon(screen, darkblue, [[90, 143], [400,310], [215, 310],[401, 500],[90, 500]], 5)

    # Moon draw overlapping two circle and small 12-pointed star 
    pygame.draw.circle(screen, white, (165,264),52, 0)
    pygame.draw.circle(screen, red, (164,244),53, 0)

    pointlist_1 = [(160, 260), (140, 295), (180, 295)]
    drawPolygon(screen, pointlist_1)
    pointlist_2 = [(140, 272), (180, 272), (160, 306)]
    drawPolygon(screen, pointlist_2)
    pointlist_3 = [(137, 283), (172, 263), (172, 303)]
    drawPolygon(screen, pointlist_3)
    pointlist_4 = [(148, 263), (148, 303), (183, 283)]
    drawPolygon(screen, pointlist_4)

    #12-pointed stars using polygon creating triangle shape top bottom left right   
    pointlist_1 = [(175, 355), (130, 433), (220, 433)]
    pygame.draw.polygon(screen, white, pointlist_1, 0)
    pointlist_2 = [(130, 381), (220, 381), (175, 459)]
    pygame.draw.polygon(screen, white, pointlist_2, 0)
    pointlist_3 = [(123, 407), (201, 362), (201, 452)]
    pygame.draw.polygon(screen, white, pointlist_3, 0)
    pointlist_4 = [(149, 362), (227, 407), (149, 452)]
    pygame.draw.polygon(screen, white, pointlist_4, 0)

    pygame.display.flip()
    pygame.display.update()

    #Setting FPS
    clock.tick(60)

#Shutdown
pygame.quit()
sys.exit()
