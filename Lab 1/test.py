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

#def degreesToRadians(deg):
 #   return deg/180.0 * math.pi

# Loop Switch
done = False

# Screen Update Speed (FPS)
clock = pygame.time.Clock()

# ------- Main Program Loop -------
while not done:
    # --- Main Quit Event Loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  
    screen.fill(white)
    # This draws a flag using the polygon command
    pygame.draw.polygon(screen, red, [[90, 143], [400,310], [215, 310],[400, 500],[90, 500]], 0)
    pygame.draw.polygon(screen, darkblue, [[90, 143], [400,310], [215, 310],[401, 500],[90, 500]], 5)

    pygame.draw.circle(screen, white, (165,264),52, 0)
    pygame.draw.circle(screen, red, (164,244),53, 0)
    pointlist_1 = [(160, 260), (140, 295), (180, 295)]
    pygame.draw.polygon(screen, white, pointlist_1, 0)
    pointlist_2 = [(140, 272), (180, 272), (160, 306)]
    pygame.draw.polygon(screen, white, pointlist_2, 0)
    pointlist_3 = [(137, 283), (172, 263), (172, 303)]
    pygame.draw.polygon(screen, white, pointlist_3, 0)
    pointlist_4 = [(148, 263), (148, 303), (183, 283)]
    pygame.draw.polygon(screen, white, pointlist_4, 0)

    #stars top bottom left
    #pointlist_1 = [(175, 355), (130, 440), (220, 440)]
    #pygame.draw.polygon(screen, white, pointlist_1, 0)
    #pointlist_2 = [(130, 380), (220, 380), (175, 465)]
    #pygame.draw.polygon(screen, white, pointlist_2, 0)
    #pointlist_3 = [(120, 410), (205, 455), (205, 365)]
    #pygame.draw.polygon(screen, white, pointlist_3, 0)
    #pointlist_4 = [(145, 365), (230, 410), (145, 455)]
    #pygame.draw.polygon(screen, white, pointlist_4, 0)
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
