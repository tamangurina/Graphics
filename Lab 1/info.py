import pygame, sys

pygame.init()

# setup graphics env. and display resolution
package = "pip install pygame"
print("Setup graphics environment by installing pygame module : " + package)

# display resolution using pygame displayInfo() function
screen_resolution = pygame.display.Info()
print("Screen Resolution width * height : " + str(screen_resolution.current_w) + 
    " x " + str(screen_resolution.current_h))


#screen = pygame.display.set_mode((600,600))

#surface = pygame.display.get_surface() #get the surface of the current active display
#x,y = size = surface.get_width(), surface.get_height()#create an array of surface.width and surface.height
#print("Screen Resolution width * height : " + str(x) + " x " + str(y))

#print the name of language and graphics library
language = "Python"
graphics_library = "Pygame"

print("\nName of programming language : " + language)
print("Name of graphics library : " + graphics_library)


