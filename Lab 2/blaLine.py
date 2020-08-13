from graphics import *
import time
import math

# creating the window
win = GraphWin('Brasenham Line', 600, 500)
 
def drawLineBLA(x1, y1, x2, y2):
    
    x, y = x1, y1       
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
        
    putPixel(win, x, y)
    
    if dx > dy:
        p = 2*dy - dx
        for k in range(0, dx):            
            if p > 0:
                y = y + 1 if y < y2 else y - 1
                p = p + 2*(dy - dx)
            else:                
                p = p + 2*dy 

            x = x + 1 if x < x2 else x - 1 
            print(f'x = {x}, y = {y}')
            putPixel(win, x, y)
    else:
        p = 2*dx - dy
        for k in range(0, dy):           
            if p > 0:
                x = x + 1 if x < x2 else x - 1
                p = p + 2*dx - 2*dy
            else:   
                p = p + 2*dx

            y = y + 1 if y < y2 else y - 1
            print(f'x = {x}, y = {y}')      
            putPixel(win, x, y)

    win.getMouse()
    win.close()
     
def putPixel(win, x, y):
    pt = Point(x,y)
    pt.draw(win)
 
def main(): 
    drawLineBLA(120,310,350,138)
        
if __name__ == "__main__":
    main()